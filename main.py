#!/usr/bin/python           # or wherever your python execs live on unix derivatives

import os, networkClient, sys, threading

exiting = False

client = networkClient.networkClient( r"deepshadowsmush.com", 6250 )

def getInput():
    global exiting
    chrline = []
    while True:
        #
        # This reads each character individually from stdin as the user types, and echoes it to the screen, while
        # storing it for further processing
        #
        inChr = sys.stdin.read( 1 )
        #
        # This converts each character to its ordinal/numeric value for easier handling in if/else tests
        #
        inOrd = ord(inChr)
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
        if ( inOrd > 0x1f ) and ( inOrd < 0x7e ):
            chrline.append( inChr )
        # testing if inChr is enter key
        elif inOrd == 0x0d:
            # must append \r\n for network lineterm
            chrline.append( chr(0x0d) )
            chrline.append( chr(0x0a) )
            if ''.join( chrline ) != "/exitclient\r\n":
                client.write( ''.join( chrline ) )
            else:
                exiting = True
                client.close()
                break
            chrline = [ ]

uit = threading.Thread( target = getInput )
uit.daemon = True # setting as background thread
uit.start()

while not exiting:
    continue

client.close()