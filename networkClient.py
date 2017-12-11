#!/usr/bin/python           # or wherever your python execs live on unix derivatives

import os, platform, sys, telnetlib, textwrap, threading

import options

class networkClient(telnetlib.Telnet):

    def __init__( self, address, port ):
        telnetlib.Telnet.__init__( self, host = address, port = port )
        rt = threading.Thread( target = self.doRead )
        rt.daemon = True  # setting as background thread
        rt.start( )

    def telnetNegotiationCallback( self, socket, command, option ):
        # command will be DO DONT WILL WONT
        pass

    def isConsoleANSI( self ):
        # sufficient for unix derivatives if the user deliberately disabled ANSI display
        r = (os.getenv( 'ANSI_COLORS_DISABLED' ) is None) and not (platform.system( ) == r"Windows")
        # if r is false then test if the system is windows and also 10 or better
        if not r:
            r = (platform.system( ) == r"Windows") and (int( platform.version( ).split( r"." )[ 0 ] ) >= 10)
        return r

    def deColorize( self, data ):
        r = []
        if not (data == None):
            incolor = False
            for i in range( len( data ) ):
                thischar = data[i]
                thisord = ord(data[ i ])
                #
                # pass through data as a byte array, seeking ANSI color codes
                # ANSI/XTERM color codes are in the form 0x1b (ESC) - 0x5b ([) - (variable) - 0x6d (m)
                # where (variable) is typically an ASCII numeric value representing a color code, highlight, etc
                #
                if not incolor:
                    # not currently processing ansi/xterm
                    if ( ord( data[i] ) == 0x1b ): # the escape character means we're beginning a color sequence
                        # toggle our selector on and don't add the character to output
                        incolor = True
                    else:
                        # good to go - add character to output
                        r.append( data[i] )
                else:
                    # we are currently processing ansi/xterm
                    # don't add the color sequence to output
                    if ( ord( data[i] ) == 0x6d ): # the m character terminates an escape sequence
                        # toggle the selector off but don't add the character to output
                        incolor = False
                # no matter what else we did here, continue on
                continue
        # cut return value back into a string before actually returning it
        return ''.join( r )

    def doRead( self ):
        while True:
            data = self.read_very_eager()
            if not (data == r""):
                # test for and perhaps strip ANSI if the platform doesn't support console colorization
                if ( not self.isConsoleANSI() ):
                    data = self.deColorize( data )
                # kick out tabstops because they're impossible to intelligently wrap with in any font
                # * data should still be a string from self.read
                data = data.replace('\t','' * options.tabWidth)
                # python's textwrap really is pointless - by the time we do all this other stuff we may as well do the
                # rest ourselves too - especially if we're wrapping ANSI escape codes (which we will be eventually)
                # FIRST SPLIT THE STRING ON ITS ORIGINAL USER-DEFINED LINEBREAKS
                # network lineterms should always be 0x0d 0x0a just like windows
                data = data.split( '\r\n' )
                for p in data:
                    # now we can wrap each individual paragraph
                    print ( textwrap.fill( p, options.screenWidth ) )
                #for i in range( len( data ) ):
                    #
                    # keeping the next (commented) line for future debugging purposes
                    #
                    # sys.stdout.write( str(ord(data[i])) + " " + str(data[i]) + os.linesep )
                    #
                #    sys.stdout.write( data )



