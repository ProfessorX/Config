# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QListWidgetItem(): # skipped bases: <class 'sip.wrapper'>
    """
    QListWidgetItem(QListWidget parent=None, int type=QListWidgetItem.Type)
    QListWidgetItem(str, QListWidget parent=None, int type=QListWidgetItem.Type)
    QListWidgetItem(QIcon, str, QListWidget parent=None, int type=QListWidgetItem.Type)
    QListWidgetItem(QListWidgetItem)
    """
    def background(self): # real signature unknown; restored from __doc__
        """ QListWidgetItem.background() -> QBrush """
        return QBrush

    def backgroundColor(self): # real signature unknown; restored from __doc__
        """ QListWidgetItem.backgroundColor() -> QColor """
        return QColor

    def checkState(self): # real signature unknown; restored from __doc__
        """ QListWidgetItem.checkState() -> Qt.CheckState """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ QListWidgetItem.clone() -> QListWidgetItem """
        return QListWidgetItem

    def data(self, p_int): # real signature unknown; restored from __doc__
        """ QListWidgetItem.data(int) -> object """
        return object()

    def flags(self): # real signature unknown; restored from __doc__
        """ QListWidgetItem.flags() -> Qt.ItemFlags """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ QListWidgetItem.font() -> QFont """
        return QFont

    def foreground(self): # real signature unknown; restored from __doc__
        """ QListWidgetItem.foreground() -> QBrush """
        return QBrush

    def icon(self): # real signature unknown; restored from __doc__
        """ QListWidgetItem.icon() -> QIcon """
        return QIcon

    def isHidden(self): # real signature unknown; restored from __doc__
        """ QListWidgetItem.isHidden() -> bool """
        return False

    def isSelected(self): # real signature unknown; restored from __doc__
        """ QListWidgetItem.isSelected() -> bool """
        return False

    def listWidget(self): # real signature unknown; restored from __doc__
        """ QListWidgetItem.listWidget() -> QListWidget """
        return QListWidget

    def read(self, QDataStream): # real signature unknown; restored from __doc__
        """ QListWidgetItem.read(QDataStream) """
        pass

    def setBackground(self, QBrush): # real signature unknown; restored from __doc__
        """ QListWidgetItem.setBackground(QBrush) """
        pass

    def setBackgroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QListWidgetItem.setBackgroundColor(QColor) """
        pass

    def setCheckState(self, Qt_CheckState): # real signature unknown; restored from __doc__
        """ QListWidgetItem.setCheckState(Qt.CheckState) """
        pass

    def setData(self, p_int, p_object): # real signature unknown; restored from __doc__
        """ QListWidgetItem.setData(int, object) """
        pass

    def setFlags(self, Qt_ItemFlags): # real signature unknown; restored from __doc__
        """ QListWidgetItem.setFlags(Qt.ItemFlags) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ QListWidgetItem.setFont(QFont) """
        pass

    def setForeground(self, QBrush): # real signature unknown; restored from __doc__
        """ QListWidgetItem.setForeground(QBrush) """
        pass

    def setHidden(self, bool): # real signature unknown; restored from __doc__
        """ QListWidgetItem.setHidden(bool) """
        pass

    def setIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ QListWidgetItem.setIcon(QIcon) """
        pass

    def setSelected(self, bool): # real signature unknown; restored from __doc__
        """ QListWidgetItem.setSelected(bool) """
        pass

    def setSizeHint(self, QSize): # real signature unknown; restored from __doc__
        """ QListWidgetItem.setSizeHint(QSize) """
        pass

    def setStatusTip(self, p_str): # real signature unknown; restored from __doc__
        """ QListWidgetItem.setStatusTip(str) """
        pass

    def setText(self, p_str): # real signature unknown; restored from __doc__
        """ QListWidgetItem.setText(str) """
        pass

    def setTextAlignment(self, p_int): # real signature unknown; restored from __doc__
        """ QListWidgetItem.setTextAlignment(int) """
        pass

    def setTextColor(self, QColor): # real signature unknown; restored from __doc__
        """ QListWidgetItem.setTextColor(QColor) """
        pass

    def setToolTip(self, p_str): # real signature unknown; restored from __doc__
        """ QListWidgetItem.setToolTip(str) """
        pass

    def setWhatsThis(self, p_str): # real signature unknown; restored from __doc__
        """ QListWidgetItem.setWhatsThis(str) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QListWidgetItem.sizeHint() -> QSize """
        pass

    def statusTip(self): # real signature unknown; restored from __doc__
        """ QListWidgetItem.statusTip() -> str """
        return ""

    def text(self): # real signature unknown; restored from __doc__
        """ QListWidgetItem.text() -> str """
        return ""

    def textAlignment(self): # real signature unknown; restored from __doc__
        """ QListWidgetItem.textAlignment() -> int """
        return 0

    def textColor(self): # real signature unknown; restored from __doc__
        """ QListWidgetItem.textColor() -> QColor """
        return QColor

    def toolTip(self): # real signature unknown; restored from __doc__
        """ QListWidgetItem.toolTip() -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ QListWidgetItem.type() -> int """
        return 0

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ QListWidgetItem.whatsThis() -> str """
        return ""

    def write(self, QDataStream): # real signature unknown; restored from __doc__
        """ QListWidgetItem.write(QDataStream) """
        pass

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


    ItemType = None # (!) real value is ''
    Type = 0
    UserType = 1000
    __hash__ = None


