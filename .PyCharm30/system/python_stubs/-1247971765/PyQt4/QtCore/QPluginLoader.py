# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


from .QObject import QObject

class QPluginLoader(QObject):
    """
    QPluginLoader(QObject parent=None)
    QPluginLoader(str, QObject parent=None)
    """
    def errorString(self): # real signature unknown; restored from __doc__
        """ QPluginLoader.errorString() -> str """
        return ""

    def fileName(self): # real signature unknown; restored from __doc__
        """ QPluginLoader.fileName() -> str """
        return ""

    def instance(self): # real signature unknown; restored from __doc__
        """ QPluginLoader.instance() -> QObject """
        return QObject

    def isLoaded(self): # real signature unknown; restored from __doc__
        """ QPluginLoader.isLoaded() -> bool """
        return False

    def load(self): # real signature unknown; restored from __doc__
        """ QPluginLoader.load() -> bool """
        return False

    def loadHints(self): # real signature unknown; restored from __doc__
        """ QPluginLoader.loadHints() -> QLibrary.LoadHints """
        pass

    def setFileName(self, p_str): # real signature unknown; restored from __doc__
        """ QPluginLoader.setFileName(str) """
        pass

    def setLoadHints(self, QLibrary_LoadHints): # real signature unknown; restored from __doc__
        """ QPluginLoader.setLoadHints(QLibrary.LoadHints) """
        pass

    def staticInstances(self): # real signature unknown; restored from __doc__
        """ QPluginLoader.staticInstances() -> list-of-QObject """
        pass

    def unload(self): # real signature unknown; restored from __doc__
        """ QPluginLoader.unload() -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


