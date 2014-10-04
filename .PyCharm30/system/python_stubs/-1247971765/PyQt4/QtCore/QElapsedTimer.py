# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


class QElapsedTimer(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QElapsedTimer()
    QElapsedTimer(QElapsedTimer)
    """
    def clockType(self): # real signature unknown; restored from __doc__
        """ QElapsedTimer.clockType() -> QElapsedTimer.ClockType """
        pass

    def elapsed(self): # real signature unknown; restored from __doc__
        """ QElapsedTimer.elapsed() -> int """
        return 0

    def hasExpired(self, p_int): # real signature unknown; restored from __doc__
        """ QElapsedTimer.hasExpired(int) -> bool """
        return False

    def invalidate(self): # real signature unknown; restored from __doc__
        """ QElapsedTimer.invalidate() """
        pass

    def isMonotonic(self): # real signature unknown; restored from __doc__
        """ QElapsedTimer.isMonotonic() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QElapsedTimer.isValid() -> bool """
        return False

    def msecsSinceReference(self): # real signature unknown; restored from __doc__
        """ QElapsedTimer.msecsSinceReference() -> int """
        return 0

    def msecsTo(self, QElapsedTimer): # real signature unknown; restored from __doc__
        """ QElapsedTimer.msecsTo(QElapsedTimer) -> int """
        return 0

    def nsecsElapsed(self): # real signature unknown; restored from __doc__
        """ QElapsedTimer.nsecsElapsed() -> int """
        return 0

    def restart(self): # real signature unknown; restored from __doc__
        """ QElapsedTimer.restart() -> int """
        return 0

    def secsTo(self, QElapsedTimer): # real signature unknown; restored from __doc__
        """ QElapsedTimer.secsTo(QElapsedTimer) -> int """
        return 0

    def start(self): # real signature unknown; restored from __doc__
        """ QElapsedTimer.start() """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, QElapsedTimer=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ClockType = None # (!) real value is ''
    MachAbsoluteTime = 3
    MonotonicClock = 1
    PerformanceCounter = 4
    SystemTime = 0
    TickCounter = 2
    __hash__ = None


