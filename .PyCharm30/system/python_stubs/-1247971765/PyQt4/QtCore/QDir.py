# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


class QDir(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDir(QDir)
    QDir(str path='')
    QDir(str, str, QDir.SortFlags sort=QDir.Name|QDir.IgnoreCase, QDir.Filters filters=QDir.AllEntries)
    """
    def absoluteFilePath(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.absoluteFilePath(str) -> str """
        return ""

    def absolutePath(self): # real signature unknown; restored from __doc__
        """ QDir.absolutePath() -> str """
        return ""

    def addResourceSearchPath(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.addResourceSearchPath(str) """
        pass

    def addSearchPath(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QDir.addSearchPath(str, str) """
        pass

    def canonicalPath(self): # real signature unknown; restored from __doc__
        """ QDir.canonicalPath() -> str """
        return ""

    def cd(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.cd(str) -> bool """
        return False

    def cdUp(self): # real signature unknown; restored from __doc__
        """ QDir.cdUp() -> bool """
        return False

    def cleanPath(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.cleanPath(str) -> str """
        return ""

    def convertSeparators(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.convertSeparators(str) -> str """
        return ""

    def count(self): # real signature unknown; restored from __doc__
        """ QDir.count() -> int """
        return 0

    def current(self): # real signature unknown; restored from __doc__
        """ QDir.current() -> QDir """
        return QDir

    def currentPath(self): # real signature unknown; restored from __doc__
        """ QDir.currentPath() -> str """
        return ""

    def dirName(self): # real signature unknown; restored from __doc__
        """ QDir.dirName() -> str """
        return ""

    def drives(self): # real signature unknown; restored from __doc__
        """ QDir.drives() -> list-of-QFileInfo """
        pass

    def entryInfoList(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDir.entryInfoList(QDir.Filters filters=QDir.NoFilter, QDir.SortFlags sort=QDir.NoSort) -> list-of-QFileInfo
        QDir.entryInfoList(list-of-str, QDir.Filters filters=QDir.NoFilter, QDir.SortFlags sort=QDir.NoSort) -> list-of-QFileInfo
        """
        pass

    def entryList(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDir.entryList(QDir.Filters filters=QDir.NoFilter, QDir.SortFlags sort=QDir.NoSort) -> list-of-str
        QDir.entryList(list-of-str, QDir.Filters filters=QDir.NoFilter, QDir.SortFlags sort=QDir.NoSort) -> list-of-str
        """
        pass

    def exists(self, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDir.exists() -> bool
        QDir.exists(str) -> bool
        """
        return False

    def filePath(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.filePath(str) -> str """
        return ""

    def filter(self): # real signature unknown; restored from __doc__
        """ QDir.filter() -> QDir.Filters """
        pass

    def fromNativeSeparators(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.fromNativeSeparators(str) -> str """
        return ""

    def home(self): # real signature unknown; restored from __doc__
        """ QDir.home() -> QDir """
        return QDir

    def homePath(self): # real signature unknown; restored from __doc__
        """ QDir.homePath() -> str """
        return ""

    def isAbsolute(self): # real signature unknown; restored from __doc__
        """ QDir.isAbsolute() -> bool """
        return False

    def isAbsolutePath(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.isAbsolutePath(str) -> bool """
        return False

    def isReadable(self): # real signature unknown; restored from __doc__
        """ QDir.isReadable() -> bool """
        return False

    def isRelative(self): # real signature unknown; restored from __doc__
        """ QDir.isRelative() -> bool """
        return False

    def isRelativePath(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.isRelativePath(str) -> bool """
        return False

    def isRoot(self): # real signature unknown; restored from __doc__
        """ QDir.isRoot() -> bool """
        return False

    def makeAbsolute(self): # real signature unknown; restored from __doc__
        """ QDir.makeAbsolute() -> bool """
        return False

    def match(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDir.match(list-of-str, str) -> bool
        QDir.match(str, str) -> bool
        """
        return False

    def mkdir(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.mkdir(str) -> bool """
        return False

    def mkpath(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.mkpath(str) -> bool """
        return False

    def nameFilters(self): # real signature unknown; restored from __doc__
        """ QDir.nameFilters() -> list-of-str """
        pass

    def nameFiltersFromString(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.nameFiltersFromString(str) -> list-of-str """
        pass

    def path(self): # real signature unknown; restored from __doc__
        """ QDir.path() -> str """
        return ""

    def refresh(self): # real signature unknown; restored from __doc__
        """ QDir.refresh() """
        pass

    def relativeFilePath(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.relativeFilePath(str) -> str """
        return ""

    def remove(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.remove(str) -> bool """
        return False

    def rename(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QDir.rename(str, str) -> bool """
        return False

    def rmdir(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.rmdir(str) -> bool """
        return False

    def rmpath(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.rmpath(str) -> bool """
        return False

    def root(self): # real signature unknown; restored from __doc__
        """ QDir.root() -> QDir """
        return QDir

    def rootPath(self): # real signature unknown; restored from __doc__
        """ QDir.rootPath() -> str """
        return ""

    def searchPaths(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.searchPaths(str) -> list-of-str """
        pass

    def separator(self): # real signature unknown; restored from __doc__
        """ QDir.separator() -> str """
        return ""

    def setCurrent(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.setCurrent(str) -> bool """
        return False

    def setFilter(self, QDir_Filters): # real signature unknown; restored from __doc__
        """ QDir.setFilter(QDir.Filters) """
        pass

    def setNameFilters(self, list_of_str): # real signature unknown; restored from __doc__
        """ QDir.setNameFilters(list-of-str) """
        pass

    def setPath(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.setPath(str) """
        pass

    def setSearchPaths(self, p_str, list_of_str): # real signature unknown; restored from __doc__
        """ QDir.setSearchPaths(str, list-of-str) """
        pass

    def setSorting(self, QDir_SortFlags): # real signature unknown; restored from __doc__
        """ QDir.setSorting(QDir.SortFlags) """
        pass

    def sorting(self): # real signature unknown; restored from __doc__
        """ QDir.sorting() -> QDir.SortFlags """
        pass

    def temp(self): # real signature unknown; restored from __doc__
        """ QDir.temp() -> QDir """
        return QDir

    def tempPath(self): # real signature unknown; restored from __doc__
        """ QDir.tempPath() -> str """
        return ""

    def toNativeSeparators(self, p_str): # real signature unknown; restored from __doc__
        """ QDir.toNativeSeparators(str) -> str """
        return ""

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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


    AccessMask = 1008
    AllDirs = 1024
    AllEntries = 7
    CaseSensitive = 2048
    Dirs = 1
    DirsFirst = 4
    DirsLast = 32
    Drives = 4
    Executable = 64
    Files = 2
    Filter = None # (!) real value is ''
    Filters = None # (!) real value is ''
    Hidden = 256
    IgnoreCase = 16
    LocaleAware = 64
    Modified = 128
    Name = 0
    NoDot = 8192
    NoDotAndDotDot = 4096
    NoDotDot = 16384
    NoFilter = -1
    NoSort = -1
    NoSymLinks = 8
    PermissionMask = 112
    Readable = 16
    Reversed = 8
    Size = 2
    SortByMask = 3
    SortFlag = None # (!) real value is ''
    SortFlags = None # (!) real value is ''
    System = 512
    Time = 1
    Type = 128
    TypeMask = 15
    Unsorted = 3
    Writable = 32
    __hash__ = None


