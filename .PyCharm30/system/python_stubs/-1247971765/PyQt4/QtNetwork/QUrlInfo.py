# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt4/QtNetwork.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QUrlInfo(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QUrlInfo()
    QUrlInfo(QUrlInfo)
    QUrlInfo(str, int, str, str, int, QDateTime, QDateTime, bool, bool, bool, bool, bool, bool)
    QUrlInfo(QUrl, int, str, str, int, QDateTime, QDateTime, bool, bool, bool, bool, bool, bool)
    """
    def equal(self, QUrlInfo, QUrlInfo_1, p_int): # real signature unknown; restored from __doc__
        """ QUrlInfo.equal(QUrlInfo, QUrlInfo, int) -> bool """
        return False

    def greaterThan(self, QUrlInfo, QUrlInfo_1, p_int): # real signature unknown; restored from __doc__
        """ QUrlInfo.greaterThan(QUrlInfo, QUrlInfo, int) -> bool """
        return False

    def group(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.group() -> str """
        return ""

    def isDir(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.isDir() -> bool """
        return False

    def isExecutable(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.isExecutable() -> bool """
        return False

    def isFile(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.isFile() -> bool """
        return False

    def isReadable(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.isReadable() -> bool """
        return False

    def isSymLink(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.isSymLink() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.isValid() -> bool """
        return False

    def isWritable(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.isWritable() -> bool """
        return False

    def lastModified(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.lastModified() -> QDateTime """
        pass

    def lastRead(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.lastRead() -> QDateTime """
        pass

    def lessThan(self, QUrlInfo, QUrlInfo_1, p_int): # real signature unknown; restored from __doc__
        """ QUrlInfo.lessThan(QUrlInfo, QUrlInfo, int) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.name() -> str """
        return ""

    def owner(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.owner() -> str """
        return ""

    def permissions(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.permissions() -> int """
        return 0

    def setDir(self, bool): # real signature unknown; restored from __doc__
        """ QUrlInfo.setDir(bool) """
        pass

    def setFile(self, bool): # real signature unknown; restored from __doc__
        """ QUrlInfo.setFile(bool) """
        pass

    def setGroup(self, p_str): # real signature unknown; restored from __doc__
        """ QUrlInfo.setGroup(str) """
        pass

    def setLastModified(self, QDateTime): # real signature unknown; restored from __doc__
        """ QUrlInfo.setLastModified(QDateTime) """
        pass

    def setLastRead(self, QDateTime): # real signature unknown; restored from __doc__
        """ QUrlInfo.setLastRead(QDateTime) """
        pass

    def setName(self, p_str): # real signature unknown; restored from __doc__
        """ QUrlInfo.setName(str) """
        pass

    def setOwner(self, p_str): # real signature unknown; restored from __doc__
        """ QUrlInfo.setOwner(str) """
        pass

    def setPermissions(self, p_int): # real signature unknown; restored from __doc__
        """ QUrlInfo.setPermissions(int) """
        pass

    def setReadable(self, bool): # real signature unknown; restored from __doc__
        """ QUrlInfo.setReadable(bool) """
        pass

    def setSize(self, p_int): # real signature unknown; restored from __doc__
        """ QUrlInfo.setSize(int) """
        pass

    def setSymLink(self, bool): # real signature unknown; restored from __doc__
        """ QUrlInfo.setSymLink(bool) """
        pass

    def setWritable(self, bool): # real signature unknown; restored from __doc__
        """ QUrlInfo.setWritable(bool) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QUrlInfo.size() -> int """
        return 0

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
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


    ExeGroup = 8
    ExeOther = 1
    ExeOwner = 64
    PermissionSpec = None # (!) real value is ''
    ReadGroup = 32
    ReadOther = 4
    ReadOwner = 256
    WriteGroup = 16
    WriteOther = 2
    WriteOwner = 128
    __hash__ = None


