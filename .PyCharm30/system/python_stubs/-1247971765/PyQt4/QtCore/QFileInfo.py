# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


class QFileInfo(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QFileInfo()
    QFileInfo(str)
    QFileInfo(QFile)
    QFileInfo(QDir, str)
    QFileInfo(QFileInfo)
    """
    def absoluteDir(self): # real signature unknown; restored from __doc__
        """ QFileInfo.absoluteDir() -> QDir """
        return QDir

    def absoluteFilePath(self): # real signature unknown; restored from __doc__
        """ QFileInfo.absoluteFilePath() -> str """
        return ""

    def absolutePath(self): # real signature unknown; restored from __doc__
        """ QFileInfo.absolutePath() -> str """
        return ""

    def baseName(self): # real signature unknown; restored from __doc__
        """ QFileInfo.baseName() -> str """
        return ""

    def bundleName(self): # real signature unknown; restored from __doc__
        """ QFileInfo.bundleName() -> str """
        return ""

    def caching(self): # real signature unknown; restored from __doc__
        """ QFileInfo.caching() -> bool """
        return False

    def canonicalFilePath(self): # real signature unknown; restored from __doc__
        """ QFileInfo.canonicalFilePath() -> str """
        return ""

    def canonicalPath(self): # real signature unknown; restored from __doc__
        """ QFileInfo.canonicalPath() -> str """
        return ""

    def completeBaseName(self): # real signature unknown; restored from __doc__
        """ QFileInfo.completeBaseName() -> str """
        return ""

    def completeSuffix(self): # real signature unknown; restored from __doc__
        """ QFileInfo.completeSuffix() -> str """
        return ""

    def created(self): # real signature unknown; restored from __doc__
        """ QFileInfo.created() -> QDateTime """
        return QDateTime

    def dir(self): # real signature unknown; restored from __doc__
        """ QFileInfo.dir() -> QDir """
        return QDir

    def exists(self): # real signature unknown; restored from __doc__
        """ QFileInfo.exists() -> bool """
        return False

    def fileName(self): # real signature unknown; restored from __doc__
        """ QFileInfo.fileName() -> str """
        return ""

    def filePath(self): # real signature unknown; restored from __doc__
        """ QFileInfo.filePath() -> str """
        return ""

    def group(self): # real signature unknown; restored from __doc__
        """ QFileInfo.group() -> str """
        return ""

    def groupId(self): # real signature unknown; restored from __doc__
        """ QFileInfo.groupId() -> int """
        return 0

    def isAbsolute(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isAbsolute() -> bool """
        return False

    def isBundle(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isBundle() -> bool """
        return False

    def isDir(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isDir() -> bool """
        return False

    def isExecutable(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isExecutable() -> bool """
        return False

    def isFile(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isFile() -> bool """
        return False

    def isHidden(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isHidden() -> bool """
        return False

    def isReadable(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isReadable() -> bool """
        return False

    def isRelative(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isRelative() -> bool """
        return False

    def isRoot(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isRoot() -> bool """
        return False

    def isSymLink(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isSymLink() -> bool """
        return False

    def isWritable(self): # real signature unknown; restored from __doc__
        """ QFileInfo.isWritable() -> bool """
        return False

    def lastModified(self): # real signature unknown; restored from __doc__
        """ QFileInfo.lastModified() -> QDateTime """
        return QDateTime

    def lastRead(self): # real signature unknown; restored from __doc__
        """ QFileInfo.lastRead() -> QDateTime """
        return QDateTime

    def makeAbsolute(self): # real signature unknown; restored from __doc__
        """ QFileInfo.makeAbsolute() -> bool """
        return False

    def owner(self): # real signature unknown; restored from __doc__
        """ QFileInfo.owner() -> str """
        return ""

    def ownerId(self): # real signature unknown; restored from __doc__
        """ QFileInfo.ownerId() -> int """
        return 0

    def path(self): # real signature unknown; restored from __doc__
        """ QFileInfo.path() -> str """
        return ""

    def permission(self, QFile_Permissions): # real signature unknown; restored from __doc__
        """ QFileInfo.permission(QFile.Permissions) -> bool """
        return False

    def permissions(self): # real signature unknown; restored from __doc__
        """ QFileInfo.permissions() -> QFile.Permissions """
        pass

    def readLink(self): # real signature unknown; restored from __doc__
        """ QFileInfo.readLink() -> str """
        return ""

    def refresh(self): # real signature unknown; restored from __doc__
        """ QFileInfo.refresh() """
        pass

    def setCaching(self, bool): # real signature unknown; restored from __doc__
        """ QFileInfo.setCaching(bool) """
        pass

    def setFile(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFileInfo.setFile(str)
        QFileInfo.setFile(QFile)
        QFileInfo.setFile(QDir, str)
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QFileInfo.size() -> int """
        return 0

    def suffix(self): # real signature unknown; restored from __doc__
        """ QFileInfo.suffix() -> str """
        return ""

    def symLinkTarget(self): # real signature unknown; restored from __doc__
        """ QFileInfo.symLinkTarget() -> str """
        return ""

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


    __hash__ = None


