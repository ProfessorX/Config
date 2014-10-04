# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


class QAbstractFileEngine(): # skipped bases: <class 'sip.wrapper'>
    """ QAbstractFileEngine() """
    def atEnd(self): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.atEnd() -> bool """
        return False

    def beginEntryList(self, QDir_Filters, list_of_str): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.beginEntryList(QDir.Filters, list-of-str) -> QAbstractFileEngineIterator """
        return QAbstractFileEngineIterator

    def caseSensitive(self): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.caseSensitive() -> bool """
        return False

    def close(self): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.close() -> bool """
        return False

    def copy(self, p_str): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.copy(str) -> bool """
        return False

    def create(self, p_str): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.create(str) -> QAbstractFileEngine """
        return QAbstractFileEngine

    def entryList(self, QDir_Filters, list_of_str): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.entryList(QDir.Filters, list-of-str) -> list-of-str """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.error() -> QFile.FileError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.errorString() -> str """
        return ""

    def fileFlags(self, QAbstractFileEngine_FileFlags_type=None): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.fileFlags(QAbstractFileEngine.FileFlags type=QAbstractFileEngine.FileInfoAll) -> QAbstractFileEngine.FileFlags """
        pass

    def fileName(self, QAbstractFileEngine_FileName_file=None): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.fileName(QAbstractFileEngine.FileName file=QAbstractFileEngine.DefaultName) -> str """
        return ""

    def fileTime(self, QAbstractFileEngine_FileTime): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.fileTime(QAbstractFileEngine.FileTime) -> QDateTime """
        return QDateTime

    def flush(self): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.flush() -> bool """
        return False

    def handle(self): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.handle() -> int """
        return 0

    def isRelativePath(self): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.isRelativePath() -> bool """
        return False

    def isSequential(self): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.isSequential() -> bool """
        return False

    def link(self, p_str): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.link(str) -> bool """
        return False

    def map(self, p_int, p_int_1, QFile_MemoryMapFlags): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.map(int, int, QFile.MemoryMapFlags) -> sip.voidptr """
        pass

    def mkdir(self, p_str, bool): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.mkdir(str, bool) -> bool """
        return False

    def open(self, QIODevice_OpenMode): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.open(QIODevice.OpenMode) -> bool """
        return False

    def owner(self, QAbstractFileEngine_FileOwner): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.owner(QAbstractFileEngine.FileOwner) -> str """
        return ""

    def ownerId(self, QAbstractFileEngine_FileOwner): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.ownerId(QAbstractFileEngine.FileOwner) -> int """
        return 0

    def pos(self): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.pos() -> int """
        return 0

    def read(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.read(int) -> bytes """
        return b""

    def readLine(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.readLine(int) -> bytes """
        return b""

    def remove(self): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.remove() -> bool """
        return False

    def rename(self, p_str): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.rename(str) -> bool """
        return False

    def rmdir(self, p_str, bool): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.rmdir(str, bool) -> bool """
        return False

    def seek(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.seek(int) -> bool """
        return False

    def setError(self, QFile_FileError, p_str): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.setError(QFile.FileError, str) """
        pass

    def setFileName(self, p_str): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.setFileName(str) """
        pass

    def setPermissions(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.setPermissions(int) -> bool """
        return False

    def setSize(self, p_int): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.setSize(int) -> bool """
        return False

    def size(self): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.size() -> int """
        return 0

    def unmap(self, sip_voidptr): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.unmap(sip.voidptr) -> bool """
        return False

    def write(self, p_str): # real signature unknown; restored from __doc__
        """ QAbstractFileEngine.write(str) -> int """
        return 0

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AbsoluteName = 3
    AbsolutePathName = 4
    AccessTime = 2
    BaseName = 1
    BundleName = 8
    BundleType = 524288
    CanonicalName = 6
    CanonicalPathName = 7
    CreationTime = 0
    DefaultName = 0
    DirectoryType = 262144
    ExeGroupPerm = 16
    ExeOtherPerm = 1
    ExeOwnerPerm = 4096
    ExeUserPerm = 256
    ExistsFlag = 4194304
    FileFlag = None # (!) real value is ''
    FileFlags = None # (!) real value is ''
    FileInfoAll = 268435455
    FileName = None # (!) real value is ''
    FileOwner = None # (!) real value is ''
    FileTime = None # (!) real value is ''
    FileType = 131072
    FlagsMask = 267386880
    HiddenFlag = 1048576
    LinkName = 5
    LinkType = 65536
    LocalDiskFlag = 2097152
    ModificationTime = 1
    OwnerGroup = 1
    OwnerUser = 0
    PathName = 2
    PermsMask = 65535
    ReadGroupPerm = 64
    ReadOtherPerm = 4
    ReadOwnerPerm = 16384
    ReadUserPerm = 1024
    Refresh = 16777216
    RootFlag = 8388608
    TypesMask = 983040
    WriteGroupPerm = 32
    WriteOtherPerm = 2
    WriteOwnerPerm = 8192
    WriteUserPerm = 512


