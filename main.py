#!/usr/bin/python           # or wherever your python execs live on unix derivatives

import os, sys, time
import appCommandProcessor, networkClient, appVariables
from _getch import getch

nc = networkClient.networkClient()
acp = appCommandProcessor.appCommandProcessor( nc )

print("Welcome to pyMuClient!  You may type /connect host:port to connect to a MU, /disconnect to disconnect, or "
      "/exitclient to disconnect and exit immediately at any time.")

#
# A line of characters that may be passed on to client commands processing or networkClient transmission
#
chrline = [ ]
#
# The main app loop
#
while not appVariables.appExiting:
    #
    # This reads each character individually from stdin as the user types, and echoes it to the screen, while
    # storing it for further processing
    #
    inChr = getch()
    #
    # This converts each character to its ordinal/numeric value for easier handling in if/else tests
    #
    inOrd = ord( inChr )
    #
    # testing if inChr is printable...
    #
    # I'm actually extremely confused as to how and why backspace works at all, since stdin.read doesn't actually
    # return anything when I hit backspace.  There is literally no event where inOrd == 0x08
    #
    # HOWEVER... under Windows 7 with Python 2.7?  THIS WORKS JUST FINE.  It not only works fine in the console,
    # it also updates into the chrline[] array even though I'm constantly doing appends and never actually doing
    # any pops or removes at any point.  So.  Whiskey Tango Foxtrot?!
    #
    # I think, perhaps, that stdin.read doesn't actually return anything at all until or unless the user actually
    # presses the return key, at which point stdin.read actually returns the entire line 1 character at a time,
    # which is a little less handy for low-level operations (macroing) but perfectly serviceable anyway.
    #
    if (inOrd > 0x1f) and (inOrd < 0x7e):
        chrline.append( inChr )
        sys.stdout.write( inChr )
        sys.stdout.flush()
    # testing if inChr is enter key - using custom getch this may be 0d in Windows or 0a in unix
    elif (inOrd == 0x0d) or (inOrd == 0x0a):
        #
        # Windows for some reason doubles-up on enter keypresses - the regular sys.stdin.read does a 0x0d-0x0a while msvcrt does
        # a 0x0d-0x0d so we need to make sure we're not trapping 2 keypresses for no good reason
        #   * We should probably just ignore the end-user if they want to hit enter on empty lines anyway, eh
        #
        if len( chrline ) > 0:
            # get the full text
            fullText = ''.join( chrline )
            # break on line separator
            sys.stdout.write( os.linesep )
            sys.stdout.flush( )
            #
            # clear the chrline after fully processing it with the user's enter-keypress
            #
            chrline = [ ]
            if not acp.processCommmand( fullText ):
                # there may be some error handling sometime in the future if we ever make appCommandProcessor
                # return a false value
                pass
    elif inOrd == 0x08:
        if ( len( chrline ) > 0 ):
            chrline.pop( len(chrline) - 1 )
            #
            # for each backspace keystroke we must instruct stdout to cursor backward, print one whitespace over the
            # existing character, and backspace the cursor back into that location again
            #
            sys.stdout.write("\b \b")
            sys.stdout.flush()
    #
    # finally let the while continue
    #
    continue

networkClient.doDisconnect()

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
