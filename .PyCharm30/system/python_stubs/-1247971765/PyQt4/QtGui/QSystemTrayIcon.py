# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QSystemTrayIcon(__PyQt4_QtCore.QObject):
    """
    QSystemTrayIcon(QObject parent=None)
    QSystemTrayIcon(QIcon, QObject parent=None)
    """
    def activated(self, *args, **kwargs): # real signature unknown
        """ QSystemTrayIcon.activated[QSystemTrayIcon.ActivationReason] [signal] """
        pass

    def contextMenu(self): # real signature unknown; restored from __doc__
        """ QSystemTrayIcon.contextMenu() -> QMenu """
        return QMenu

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QSystemTrayIcon.event(QEvent) -> bool """
        return False

    def geometry(self): # real signature unknown; restored from __doc__
        """ QSystemTrayIcon.geometry() -> QRect """
        pass

    def hide(self): # real signature unknown; restored from __doc__
        """ QSystemTrayIcon.hide() """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ QSystemTrayIcon.icon() -> QIcon """
        return QIcon

    def isSystemTrayAvailable(self): # real signature unknown; restored from __doc__
        """ QSystemTrayIcon.isSystemTrayAvailable() -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ QSystemTrayIcon.isVisible() -> bool """
        return False

    def messageClicked(self, *args, **kwargs): # real signature unknown
        """ QSystemTrayIcon.messageClicked [signal] """
        pass

    def setContextMenu(self, QMenu): # real signature unknown; restored from __doc__
        """ QSystemTrayIcon.setContextMenu(QMenu) """
        pass

    def setIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ QSystemTrayIcon.setIcon(QIcon) """
        pass

    def setToolTip(self, p_str): # real signature unknown; restored from __doc__
        """ QSystemTrayIcon.setToolTip(str) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ QSystemTrayIcon.setVisible(bool) """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ QSystemTrayIcon.show() """
        pass

    def showMessage(self, p_str, p_str_1, QSystemTrayIcon_MessageIcon_icon=None, int_msecs=10000): # real signature unknown; restored from __doc__
        """ QSystemTrayIcon.showMessage(str, str, QSystemTrayIcon.MessageIcon icon=QSystemTrayIcon.Information, int msecs=10000) """
        pass

    def supportsMessages(self): # real signature unknown; restored from __doc__
        """ QSystemTrayIcon.supportsMessages() -> bool """
        return False

    def toolTip(self): # real signature unknown; restored from __doc__
        """ QSystemTrayIcon.toolTip() -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    ActivationReason = None # (!) real value is ''
    Context = 1
    Critical = 3
    DoubleClick = 2
    Information = 1
    MessageIcon = None # (!) real value is ''
    MiddleClick = 4
    NoIcon = 0
    Trigger = 3
    Unknown = 0
    Warning = 2


