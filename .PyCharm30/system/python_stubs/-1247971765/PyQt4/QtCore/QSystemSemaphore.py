# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


class QSystemSemaphore(): # skipped bases: <class 'sip.simplewrapper'>
    """ QSystemSemaphore(str, int initialValue=0, QSystemSemaphore.AccessMode mode=QSystemSemaphore.Open) """
    def acquire(self): # real signature unknown; restored from __doc__
        """ QSystemSemaphore.acquire() -> bool """
        return False

    def error(self): # real signature unknown; restored from __doc__
        """ QSystemSemaphore.error() -> QSystemSemaphore.SystemSemaphoreError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QSystemSemaphore.errorString() -> str """
        return ""

    def key(self): # real signature unknown; restored from __doc__
        """ QSystemSemaphore.key() -> str """
        return ""

    def release(self, int_n=1): # real signature unknown; restored from __doc__
        """ QSystemSemaphore.release(int n=1) -> bool """
        return False

    def setKey(self, p_str, int_initialValue=0, QSystemSemaphore_AccessMode_mode=None): # real signature unknown; restored from __doc__
        """ QSystemSemaphore.setKey(str, int initialValue=0, QSystemSemaphore.AccessMode mode=QSystemSemaphore.Open) """
        pass

    def __init__(self, p_str, int_initialValue=0, QSystemSemaphore_AccessMode_mode=None): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AccessMode = None # (!) real value is ''
    AlreadyExists = 3
    Create = 1
    KeyError = 2
    NoError = 0
    NotFound = 4
    Open = 0
    OutOfResources = 5
    PermissionDenied = 1
    SystemSemaphoreError = None # (!) real value is ''
    UnknownError = 6


