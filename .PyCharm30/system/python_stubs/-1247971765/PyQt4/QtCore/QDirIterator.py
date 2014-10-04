# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


class QDirIterator(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDirIterator(QDir, QDirIterator.IteratorFlags flags=QDirIterator.NoIteratorFlags)
    QDirIterator(str, QDirIterator.IteratorFlags flags=QDirIterator.NoIteratorFlags)
    QDirIterator(str, QDir.Filters, QDirIterator.IteratorFlags flags=QDirIterator.NoIteratorFlags)
    QDirIterator(str, list-of-str, QDir.Filters filters=QDir.NoFilter, QDirIterator.IteratorFlags flags=QDirIterator.NoIteratorFlags)
    """
    def fileInfo(self): # real signature unknown; restored from __doc__
        """ QDirIterator.fileInfo() -> QFileInfo """
        return QFileInfo

    def fileName(self): # real signature unknown; restored from __doc__
        """ QDirIterator.fileName() -> str """
        return ""

    def filePath(self): # real signature unknown; restored from __doc__
        """ QDirIterator.filePath() -> str """
        return ""

    def hasNext(self): # real signature unknown; restored from __doc__
        """ QDirIterator.hasNext() -> bool """
        return False

    def next(self): # real signature unknown; restored from __doc__
        """ QDirIterator.next() -> str """
        return ""

    def path(self): # real signature unknown; restored from __doc__
        """ QDirIterator.path() -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    FollowSymlinks = 1
    IteratorFlag = None # (!) real value is ''
    IteratorFlags = None # (!) real value is ''
    NoIteratorFlags = 0
    Subdirectories = 2


