# pyMuClient

A telnet/MUSH Client done up in Python.  Nothing special, really, just an input loop built on Python's telnetlib.  It either passes ANSI escape sequences through 
directly to the console or strips them out if your terminal option is set to disable ANSI, or if you're on a Windows version that's too old to offer ANSI support.

Built on a Sunday afternoon as a gift for a friend who sits in a workplace all day, where the only whitelisted apps for WIndows are puTTY, pyCharm, and Python.exe 
but where they don't do any network traffic monitoring

More to come, maybe, maybe not.  