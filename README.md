# Support tekmunkey via Patreon

If you'd like to support my free software developments, my patreon can be found at:

https://www.patreon.com/tekmunkey

# pyMuClient

A telnet/MUSH Client done up in Python.  Nothing special, really, just an input loop built on Python's telnetlib.  It either passes ANSI escape sequences through 
directly to the console or strips them out if your terminal option is set to disable ANSI, or if you're on a Windows version that's too old to offer ANSI support.

Built on a Sunday afternoon as a gift for a friend who sits in a workplace all day, where the only whitelisted apps for WIndows are puTTY, pyCharm, and Python.exe 
but where they don't do any network traffic monitoring

More to come, maybe, maybe not.  

## ... the cat came back the very next day


Check out:

###### /connect deepshadowsmush.com : 6250

You can also:

###### /disconnect

And you can:

###### /exitclient

If you're running on Linux or Windows 10 and you have ANSI enabled in your terminal then ANSI codes from the MUSH should automagically work just fine from the MUSH.

If ANSI codes are disabled in your terminal or if you're on any version of Windows < 10, then this product will automagically strip ANSI codes even if your MUSH 
charbit has ANSI/COLOR/XTERM flags enabled on it.  Very fancy.

You can always use a 3rd Party terminal like MinGW, git Bash, or some other TTY under Windows < 10 to achieve ANSI fancy if you like.

Still just one connection at a time for now, and if you want to change out the number of screen columns (which is defaulted to 160) or the width of a horizontal 
tabstop (which is defaulted to 4 spaces) you'll need to manually edit appOptions.py for yourself.