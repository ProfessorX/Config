# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from .QFrame import QFrame

class QToolBox(QFrame):
    """ QToolBox(QWidget parent=None, Qt.WindowFlags flags=0) """
    def addItem(self, QWidget, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QToolBox.addItem(QWidget, str) -> int
        QToolBox.addItem(QWidget, QIcon, str) -> int
        """
        return 0

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QToolBox.changeEvent(QEvent) """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ QToolBox.count() -> int """
        return 0

    def currentChanged(self, *args, **kwargs): # real signature unknown
        """ QToolBox.currentChanged[int] [signal] """
        pass

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ QToolBox.currentIndex() -> int """
        return 0

    def currentWidget(self): # real signature unknown; restored from __doc__
        """ QToolBox.currentWidget() -> QWidget """
        return QWidget

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QToolBox.event(QEvent) -> bool """
        return False

    def indexOf(self, QWidget): # real signature unknown; restored from __doc__
        """ QToolBox.indexOf(QWidget) -> int """
        return 0

    def insertItem(self, p_int, QWidget, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QToolBox.insertItem(int, QWidget, str) -> int
        QToolBox.insertItem(int, QWidget, QIcon, str) -> int
        """
        return 0

    def isItemEnabled(self, p_int): # real signature unknown; restored from __doc__
        """ QToolBox.isItemEnabled(int) -> bool """
        return False

    def itemIcon(self, p_int): # real signature unknown; restored from __doc__
        """ QToolBox.itemIcon(int) -> QIcon """
        return QIcon

    def itemInserted(self, p_int): # real signature unknown; restored from __doc__
        """ QToolBox.itemInserted(int) """
        pass

    def itemRemoved(self, p_int): # real signature unknown; restored from __doc__
        """ QToolBox.itemRemoved(int) """
        pass

    def itemText(self, p_int): # real signature unknown; restored from __doc__
        """ QToolBox.itemText(int) -> str """
        return ""

    def itemToolTip(self, p_int): # real signature unknown; restored from __doc__
        """ QToolBox.itemToolTip(int) -> str """
        return ""

    def removeItem(self, p_int): # real signature unknown; restored from __doc__
        """ QToolBox.removeItem(int) """
        pass

    def setCurrentIndex(self, p_int): # real signature unknown; restored from __doc__
        """ QToolBox.setCurrentIndex(int) """
        pass

    def setCurrentWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QToolBox.setCurrentWidget(QWidget) """
        pass

    def setItemEnabled(self, p_int, bool): # real signature unknown; restored from __doc__
        """ QToolBox.setItemEnabled(int, bool) """
        pass

    def setItemIcon(self, p_int, QIcon): # real signature unknown; restored from __doc__
        """ QToolBox.setItemIcon(int, QIcon) """
        pass

    def setItemText(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ QToolBox.setItemText(int, str) """
        pass

    def setItemToolTip(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ QToolBox.setItemToolTip(int, str) """
        pass

    def showEvent(self, QShowEvent): # real signature unknown; restored from __doc__
        """ QToolBox.showEvent(QShowEvent) """
        pass

    def widget(self, p_int): # real signature unknown; restored from __doc__
        """ QToolBox.widget(int) -> QWidget """
        return QWidget

    def __init__(self, QWidget_parent=None, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass


