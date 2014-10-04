# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QDesktopServices(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDesktopServices()
    QDesktopServices(QDesktopServices)
    """
    def displayName(self, QDesktopServices_StandardLocation): # real signature unknown; restored from __doc__
        """ QDesktopServices.displayName(QDesktopServices.StandardLocation) -> str """
        return ""

    def openUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ QDesktopServices.openUrl(QUrl) -> bool """
        return False

    def setUrlHandler(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDesktopServices.setUrlHandler(str, QObject, str)
        QDesktopServices.setUrlHandler(str, callable)
        """
        pass

    def storageLocation(self, QDesktopServices_StandardLocation): # real signature unknown; restored from __doc__
        """ QDesktopServices.storageLocation(QDesktopServices.StandardLocation) -> str """
        return ""

    def unsetUrlHandler(self, p_str): # real signature unknown; restored from __doc__
        """ QDesktopServices.unsetUrlHandler(str) """
        pass

    def __init__(self, QDesktopServices=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ApplicationsLocation = 3
    CacheLocation = 10
    DataLocation = 9
    DesktopLocation = 0
    DocumentsLocation = 1
    FontsLocation = 2
    HomeLocation = 8
    MoviesLocation = 5
    MusicLocation = 4
    PicturesLocation = 6
    StandardLocation = None # (!) real value is ''
    TempLocation = 7


