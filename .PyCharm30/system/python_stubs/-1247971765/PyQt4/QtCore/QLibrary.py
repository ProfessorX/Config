# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


from .QObject import QObject

class QLibrary(QObject):
    """
    QLibrary(QObject parent=None)
    QLibrary(str, QObject parent=None)
    QLibrary(str, int, QObject parent=None)
    QLibrary(str, str, QObject parent=None)
    """
    def errorString(self): # real signature unknown; restored from __doc__
        """ QLibrary.errorString() -> str """
        return ""

    def fileName(self): # real signature unknown; restored from __doc__
        """ QLibrary.fileName() -> str """
        return ""

    def isLibrary(self, p_str): # real signature unknown; restored from __doc__
        """ QLibrary.isLibrary(str) -> bool """
        return False

    def isLoaded(self): # real signature unknown; restored from __doc__
        """ QLibrary.isLoaded() -> bool """
        return False

    def load(self): # real signature unknown; restored from __doc__
        """ QLibrary.load() -> bool """
        return False

    def loadHints(self): # real signature unknown; restored from __doc__
        """ QLibrary.loadHints() -> QLibrary.LoadHints """
        pass

    def resolve(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QLibrary.resolve(str) -> sip.voidptr
        QLibrary.resolve(str, str) -> sip.voidptr
        QLibrary.resolve(str, int, str) -> sip.voidptr
        QLibrary.resolve(str, str, str) -> sip.voidptr
        """
        pass

    def setFileName(self, p_str): # real signature unknown; restored from __doc__
        """ QLibrary.setFileName(str) """
        pass

    def setFileNameAndVersion(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QLibrary.setFileNameAndVersion(str, int)
        QLibrary.setFileNameAndVersion(str, str)
        """
        pass

    def setLoadHints(self, QLibrary_LoadHints): # real signature unknown; restored from __doc__
        """ QLibrary.setLoadHints(QLibrary.LoadHints) """
        pass

    def unload(self): # real signature unknown; restored from __doc__
        """ QLibrary.unload() -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    ExportExternalSymbolsHint = 2
    LoadArchiveMemberHint = 4
    LoadHint = None # (!) real value is ''
    LoadHints = None # (!) real value is ''
    ResolveAllSymbolsHint = 1


