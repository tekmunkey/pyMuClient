# pyMuClient

A telnet/MUSH Client done up in Python.  Nothing special, really, just an input loop built on Python's telnetlib.  It either passes ANSI escape sequences through directly to the console or strips them out if your terminal option is set to disable ANSI, or if you're on a Windows version that's too old to offer ANSI support.

More to come, maybe, maybe not.  