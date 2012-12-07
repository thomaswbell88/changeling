changeling
==========

My first attempt at a Python script/app. Looking for feedback and guidance. The purpose is to monitor changes in websites and report back to a user.

The script currently performs the following functions:
 * Asks you what URL you want to monitor
 * Removes a specific set of characters
 * Validates and corrects given URL (adds http:// if omitted)
 * Grabs a local copy of the webpage given in a file
 * Makes a diff between last grabbed webpage and current one and store it in a file
 

 
What I want to do next:
 * Make cleanchars() more efficient, maybe by forcing characters that aren't in the alphabet to be removed rather than specifying a limited set of chars in a table...?
 * Ask the user how often they want to check the webpage
 * Clean up the tmp directory so that after each iteration, we only leave 1 file (previous diff)
 * Loop the script every "freq" set by user
 