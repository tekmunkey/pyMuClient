#!/usr/bin/python           # or wherever your python execs live on unix derivatives

import  re, sys, threading
import appVariables

class appCommandProcessor:

    #
    # A regular expression providing command capture
    #   * \0 will contain the /command itself if there is any match at all with no parameters
    #   * \0 contains the whole string when there is a match with command and parameters
    #   * \1 contains only the command itself when there are parameters
    #   * \2 will contain any command parameters, if there are any
    #
    commandRegEx = r"^(/\S+)(.*)$"

    #
    # A regular expression providing sub-parameter capture specific to the /connect command
    #   * \0 will contain the host
    #   * \1 will contain the port
    #
    connectParameterRegEx = r"^\s+(\S+)\s*:\s*(\d+)$"


    def __init__( self, networkclient ):
        self.networkClient = networkclient

    #
    # Processes the specified userstring and returns a boolean value indicating whether it is or is not in fact a
    # defined application command.
    #
    def processCommmand( self, userstring ):
        r = False
        if (not (userstring == None)) and isinstance( userstring, ( str, unicode ) ):
            reMatch = re.match( appCommandProcessor.commandRegEx, userstring, re.IGNORECASE )
            r = not ( reMatch == None )
            if r:
                #
                # This means that we have caught a defined command
                #
                if len( reMatch.groups() ) > 1:
                    # some commands have parameters
                    command = reMatch.group(  1).strip().lower()
                else:
                    # some commands have no parameters
                    command = reMatch.group( 0 ).strip( ).lower( )
                if command == "/exitclient":
                    self.networkClient.doDisconnect( )
                    appVariables.appExiting = True
                elif command == "/disconnect":
                    self.networkClient.doDisconnect()
                elif command == "/connect":
                    # reset the reMatch object to the connect subparameters
                    test = reMatch.group(2)
                    reMatch = re.match( appCommandProcessor.connectParameterRegEx, reMatch.group( 2 ) )
                    test = reMatch.groups( )
                    host = reMatch.group( 1 ).strip().lower()
                    port = reMatch.group( 2 ).strip().lower()
                    self.networkClient.doConnect( host, port )
            else:
                # if we didn't process a client command, pass on to the network client
                # must append \r\n for network lineterm
                userstring = userstring + "\r\n"
                self.networkClient.doWrite( userstring )
                # go ahead and set r to true indicating that we did in fact process the command
                r = True
        return r