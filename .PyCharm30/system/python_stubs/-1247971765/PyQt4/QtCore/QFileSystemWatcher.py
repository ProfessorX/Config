# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


from .QObject import QObject

class QFileSystemWatcher(QObject):
    """
    QFileSystemWatcher(QObject parent=None)
    QFileSystemWatcher(list-of-str, QObject parent=None)
    """
    def addPath(self, p_str): # real signature unknown; restored from __doc__
        """ QFileSystemWatcher.addPath(str) """
        pass

    def addPaths(self, list_of_str): # real signature unknown; restored from __doc__
        """ QFileSystemWatcher.addPaths(list-of-str) """
        pass

    def directories(self): # real signature unknown; restored from __doc__
        """ QFileSystemWatcher.directories() -> list-of-str """
        pass

    def directoryChanged(self, *args, **kwargs): # real signature unknown
        """ QFileSystemWatcher.directoryChanged[str] [signal] """
        pass

    def fileChanged(self, *args, **kwargs): # real signature unknown
        """ QFileSystemWatcher.fileChanged[str] [signal] """
        pass

    def files(self): # real signature unknown; restored from __doc__
        """ QFileSystemWatcher.files() -> list-of-str """
        pass

    def removePath(self, p_str): # real signature unknown; restored from __doc__
        """ QFileSystemWatcher.removePath(str) """
        pass

    def removePaths(self, list_of_str): # real signature unknown; restored from __doc__
        """ QFileSystemWatcher.removePaths(list-of-str) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


