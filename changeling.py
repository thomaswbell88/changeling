import urllib.request, os, difflib

# Global variables:
from time import gmtime, strftime
url = ""
folder = ""
time = ""
surl = url.replace("http://","")

def whaturl():
	# Get the user to enter URL
	global url	
	url = input('What URL? ')
	return url
def freq():
	global freq
	freq = input('How often shall we check this page? (in seconds) ')
	return freq
def checkexists():
# Check if dir exists, return True / False
	global folder# @todo Need correcting if global is wrong and or dangerous
	surl = url.replace("http://","")
	folder = "tmp/" + surl[:24]
	if os.path.exists(folder):
		print("We've done this before, let me just check something.. ")
		return True
	else:
		print("No folder here .. ")
		return False
def createdir():
# Create the directory
	print("gonna try to make a folder!")
	surl = url.replace("http://","")
	global folder# @todo Need correcting if global is wrong and or dangerous
	folder = "tmp/" + surl[:24] 
	os.makedirs(folder + "/grabs", exist_ok=True)
	print("We've made a new folder for you")
def grabpage():
	surl = url.replace("http://","")
	global time
	time = strftime("%Y%m%d_%H%M%S", gmtime())
	filename = surl + time + ".html"
	global folder# @todo Need correcting if global is wrong and or dangerous
	folder = "tmp/" + surl[:24] 
# Retrieve the URL
	urllib.request.urlretrieve(url, folder  + "/grabs/" + filename )
	print('File created.. ')
def cleanup():
# Let's list the current files in the relevant data directory
	ls = os.walk(folder + '/')
	sortedls = sorted(ls)
# @todo If there are more than 2 files, lets just get rid of them as we won't need them
	print(sortedls[1:])
#	for sortedls[1:] in sortedls
#		os.remove("data/thomaswbell.co.uk/" + sortedls
def comparepages():
# Compare current with most recent page
	lsfiles = os.listdir(folder + '/grabs/')
	if not os.path.exists(folder + "/diff"):
		print('Making a diff data dir..')
		os.makedirs(folder + "/diff", exist_ok=True)
	print('	Done.. ')
# Turn the two most recent (according to sorting) files into strings to use as the filename to open
	a = str(lsfiles[0])
	b = str(lsfiles[1])
	print("We're looking at these two: " + a + " & " + b)
# Open the tow latest files
	bread = open(folder + "/grabs/" + b, "r")
	aread = open(folder + "/grabs/" + a, "r")
	previousstate = bread.readlines()
	currentstate = aread.readlines()
# Start comparing two most recent
	print('Start comparing two most recent')
	d = difflib.Differ()
	diff = d.compare(previousstate, currentstate)
	diffcontents = '\n'.join(diff)
	time = strftime("%Y%m%d_%H%M%S", gmtime())
	print("Lets try to save the diff file")
	difffile = open(folder + "/diff/diff_" + surl + "_" + time, "w")
	difffile.write(diffcontents)
	difffile.close()
	print("	Done.")
	
# Run the app..

whaturl()
freq()
if checkexists() == True:
	grabpage()
	comparepages()
elif checkexists() == False:
	createdir()
	grabpage()
cleanup()