# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


from .QAbstractFileEngine import QAbstractFileEngine

class QFSFileEngine(QAbstractFileEngine):
    """
    QFSFileEngine()
    QFSFileEngine(str)
    """
    def caseSensitive(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.caseSensitive() -> bool """
        return False

    def close(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.close() -> bool """
        return False

    def copy(self, p_str): # real signature unknown; restored from __doc__
        """ QFSFileEngine.copy(str) -> bool """
        return False

    def currentPath(self, str_fileName=''): # real signature unknown; restored from __doc__
        """ QFSFileEngine.currentPath(str fileName='') -> str """
        return ""

    def drives(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.drives() -> list-of-QFileInfo """
        pass

    def entryList(self, QDir_Filters, list_of_str): # real signature unknown; restored from __doc__
        """ QFSFileEngine.entryList(QDir.Filters, list-of-str) -> list-of-str """
        pass

    def fileFlags(self, QAbstractFileEngine_FileFlags): # real signature unknown; restored from __doc__
        """ QFSFileEngine.fileFlags(QAbstractFileEngine.FileFlags) -> QAbstractFileEngine.FileFlags """
        pass

    def fileName(self, QAbstractFileEngine_FileName): # real signature unknown; restored from __doc__
        """ QFSFileEngine.fileName(QAbstractFileEngine.FileName) -> str """
        return ""

    def fileTime(self, QAbstractFileEngine_FileTime): # real signature unknown; restored from __doc__
        """ QFSFileEngine.fileTime(QAbstractFileEngine.FileTime) -> QDateTime """
        return QDateTime

    def flush(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.flush() -> bool """
        return False

    def handle(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.handle() -> int """
        return 0

    def homePath(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.homePath() -> str """
        return ""

    def isRelativePath(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.isRelativePath() -> bool """
        return False

    def isSequential(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.isSequential() -> bool """
        return False

    def link(self, p_str): # real signature unknown; restored from __doc__
        """ QFSFileEngine.link(str) -> bool """
        return False

    def mkdir(self, p_str, bool): # real signature unknown; restored from __doc__
        """ QFSFileEngine.mkdir(str, bool) -> bool """
        return False

    def open(self, QIODevice_OpenMode, p_int=None, QFile_FileHandleFlags=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFSFileEngine.open(QIODevice.OpenMode) -> bool
        QFSFileEngine.open(QIODevice.OpenMode, int, QFile.FileHandleFlags) -> bool
        QFSFileEngine.open(QIODevice.OpenMode, int) -> bool
        """
        return False

    def owner(self, QAbstractFileEngine_FileOwner): # real signature unknown; restored from __doc__
        """ QFSFileEngine.owner(QAbstractFileEngine.FileOwner) -> str """
        return ""

    def ownerId(self, QAbstractFileEngine_FileOwner): # real signature unknown; restored from __doc__
        """ QFSFileEngine.ownerId(QAbstractFileEngine.FileOwner) -> int """
        return 0

    def pos(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.pos() -> int """
        return 0

    def read(self, p_int): # real signature unknown; restored from __doc__
        """ QFSFileEngine.read(int) -> bytes """
        return b""

    def readLine(self, p_int): # real signature unknown; restored from __doc__
        """ QFSFileEngine.readLine(int) -> bytes """
        return b""

    def remove(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.remove() -> bool """
        return False

    def rename(self, p_str): # real signature unknown; restored from __doc__
        """ QFSFileEngine.rename(str) -> bool """
        return False

    def rmdir(self, p_str, bool): # real signature unknown; restored from __doc__
        """ QFSFileEngine.rmdir(str, bool) -> bool """
        return False

    def rootPath(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.rootPath() -> str """
        return ""

    def seek(self, p_int): # real signature unknown; restored from __doc__
        """ QFSFileEngine.seek(int) -> bool """
        return False

    def setCurrentPath(self, p_str): # real signature unknown; restored from __doc__
        """ QFSFileEngine.setCurrentPath(str) -> bool """
        return False

    def setFileName(self, p_str): # real signature unknown; restored from __doc__
        """ QFSFileEngine.setFileName(str) """
        pass

    def setPermissions(self, p_int): # real signature unknown; restored from __doc__
        """ QFSFileEngine.setPermissions(int) -> bool """
        return False

    def setSize(self, p_int): # real signature unknown; restored from __doc__
        """ QFSFileEngine.setSize(int) -> bool """
        return False

    def size(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.size() -> int """
        return 0

    def tempPath(self): # real signature unknown; restored from __doc__
        """ QFSFileEngine.tempPath() -> str """
        return ""

    def write(self, p_str): # real signature unknown; restored from __doc__
        """ QFSFileEngine.write(str) -> int """
        return 0

    def __init__(self, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass


