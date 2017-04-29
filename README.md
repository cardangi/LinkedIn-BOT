# LinkedIn BOT
![Yeah bro, it works!](poc.png)

## Requirements
 - Firefox Mozilla 47 (download link: https://releases.mozilla.org/pub/firefox/releases/48.0.2/win32/pt-BR/) (newer options dont work)
 - Python 3.4+ (optional)
 - iMacros installed on Mozilla (download link: https://addons.mozilla.org/pt-br/firefox/addon/imacros-for-firefox/)
 
## Configuration
### Automatic Way (With Python)
(Download all files)

1 - Move the file MacroLinkedin.iim to C:\Users\Computador\Documents\iMacros\Macros

2 - Open Firefox 47

3 - Open iMacros

4 - You will see MacroLinkedin.iim, right click, "Add to Bookmark / Adicionar aos favoritos"

5 - Click in OK

6 - Access https://www.linkedin.com/mynetwork/

7 - Login in your account

8 - Close Firefox

9 - py BotdoLinkedin.py

### Manually Way (Without Python)
(Download all files) (Maybe not work without python calling the params, because this uses !loop -9999. Use if python, if you have installed it on computer.)

1 - Move the file MacroLinkedin.iim to C:\Users\Computador\Documents\iMacros\Macros

2 - Open Firefox 47

3 - Open iMacros

4 - Access https://www.linkedin.com/mynetwork/ and login in your linkedin account

5 - Click in MacroLinkedin.iim, and then "USE"


### Issues
This is on beta test, any issue or problem, tell me with github issues options. Thanks.

Known issue: Sometimes it will appear always the same friends. Just clean the cache, logout and login again and it will works.

### Liability
I don't take no liability for the usage of this. At LinkedIn terms, they say that's prohibited the use of BOTS. I think you are not going to get problems, because the macro recuse some requests, and accept some others, wait 1.5 seconds for clicking in add friend, and refresh like 3 or 4 times (Made for getting friends at normal-human speed). But I give no guarantee that you won't get some 24 to 48 hours block, or any bigger problem. Careful usage, please!
