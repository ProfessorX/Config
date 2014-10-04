# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


from .QObject import QObject

class QSharedMemory(QObject):
    """
    QSharedMemory(QObject parent=None)
    QSharedMemory(str, QObject parent=None)
    """
    def attach(self, QSharedMemory_AccessMode_mode=None): # real signature unknown; restored from __doc__
        """ QSharedMemory.attach(QSharedMemory.AccessMode mode=QSharedMemory.ReadWrite) -> bool """
        return False

    def constData(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.constData() -> sip.voidptr """
        pass

    def create(self, p_int, QSharedMemory_AccessMode_mode=None): # real signature unknown; restored from __doc__
        """ QSharedMemory.create(int, QSharedMemory.AccessMode mode=QSharedMemory.ReadWrite) -> bool """
        return False

    def data(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.data() -> sip.voidptr """
        pass

    def detach(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.detach() -> bool """
        return False

    def error(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.error() -> QSharedMemory.SharedMemoryError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.errorString() -> str """
        return ""

    def isAttached(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.isAttached() -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.key() -> str """
        return ""

    def lock(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.lock() -> bool """
        return False

    def nativeKey(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.nativeKey() -> str """
        return ""

    def setKey(self, p_str): # real signature unknown; restored from __doc__
        """ QSharedMemory.setKey(str) """
        pass

    def setNativeKey(self, p_str): # real signature unknown; restored from __doc__
        """ QSharedMemory.setNativeKey(str) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.size() -> int """
        return 0

    def unlock(self): # real signature unknown; restored from __doc__
        """ QSharedMemory.unlock() -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AccessMode = None # (!) real value is ''
    AlreadyExists = 4
    InvalidSize = 2
    KeyError = 3
    LockError = 6
    NoError = 0
    NotFound = 5
    OutOfResources = 7
    PermissionDenied = 1
    ReadOnly = 0
    ReadWrite = 1
    SharedMemoryError = None # (!) real value is ''
    UnknownError = 8


