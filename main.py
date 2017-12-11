#!/usr/bin/python           # or wherever your python execs live on unix derivatives

import os, sys, time
import appCommandProcessor, networkClient, appVariables
from _getch import getch

nc = networkClient.networkClient()
acp = appCommandProcessor.appCommandProcessor( nc )

print("Welcome to pyMuClient!  You may type /connect host:port to connect to a MU, /disconnect to disconnect, or "
      "/exitclient to disconnect and exit immediately at any time.")

#
# The main app loop
#
while not appVariables.appExiting:
    inStr = raw_input("").strip( "\n" ).strip( "\r" )
    if not acp.processCommmand( inStr ):
        # we may add some additional processing later if appCommandProcessor.processCommand ever returns false
        pass
    continue

nc.doDisconnect()

#
# Check out:
# /connect deepshadowsmush.com : 6250
#
# You can also:
# /disconnect
#
# And you can:
# /exitclient
#
# If you're running on Linux or Windows 10 and you have ANSI enabled in your terminal then ANSI codes from the MUSH
# should automagically work just fine from the MUSH.
#
# If ANSI codes are disabled in your terminal or if you're on any version of Windows < 10, then this product will
# automagically strip ANSI codes even if your MUSH charbit has ANSI/COLOR/XTERM flags enabled on it.  Very fancy.
#
# You can always use a 3rd Party terminal like MinGW, git Bash, or some other TTY under Windows < 10 to achieve
# ANSI fancy if you like.
#
