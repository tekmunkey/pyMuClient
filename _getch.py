#!/usr/bin/python           # or wherever your python execs live on unix derivatives

#
# This is NOT my own original code.  I found it on stack overflow, where it was copied from (but there was a link to) an
# article where it may or may not have originated. - tekmunkey
#
class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys
    # You'll need to set a PyCharm (or if you use an IDE, then whatever IDE you use) ignore on the termios import error
    #  if you're a Windows developer, because termios is NOT available for Windows systems.
    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()