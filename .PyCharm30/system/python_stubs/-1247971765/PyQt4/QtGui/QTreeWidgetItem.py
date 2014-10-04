# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QTreeWidgetItem(): # skipped bases: <class 'sip.wrapper'>
    """
    QTreeWidgetItem(int type=QTreeWidgetItem.Type)
    QTreeWidgetItem(list-of-str, int type=QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidget, int type=QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidget, list-of-str, int type=QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidget, QTreeWidgetItem, int type=QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidgetItem, int type=QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidgetItem, list-of-str, int type=QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidgetItem, QTreeWidgetItem, int type=QTreeWidgetItem.Type)
    QTreeWidgetItem(QTreeWidgetItem)
    """
    def addChild(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.addChild(QTreeWidgetItem) """
        pass

    def addChildren(self, list_of_QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.addChildren(list-of-QTreeWidgetItem) """
        pass

    def background(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.background(int) -> QBrush """
        return QBrush

    def backgroundColor(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.backgroundColor(int) -> QColor """
        return QColor

    def checkState(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.checkState(int) -> Qt.CheckState """
        pass

    def child(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.child(int) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def childCount(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.childCount() -> int """
        return 0

    def childIndicatorPolicy(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.childIndicatorPolicy() -> QTreeWidgetItem.ChildIndicatorPolicy """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.clone() -> QTreeWidgetItem """
        return QTreeWidgetItem

    def columnCount(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.columnCount() -> int """
        return 0

    def data(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.data(int, int) -> object """
        return object()

    def emitDataChanged(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.emitDataChanged() """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.flags() -> Qt.ItemFlags """
        pass

    def font(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.font(int) -> QFont """
        return QFont

    def foreground(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.foreground(int) -> QBrush """
        return QBrush

    def icon(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.icon(int) -> QIcon """
        return QIcon

    def indexOfChild(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.indexOfChild(QTreeWidgetItem) -> int """
        return 0

    def insertChild(self, p_int, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.insertChild(int, QTreeWidgetItem) """
        pass

    def insertChildren(self, p_int, list_of_QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.insertChildren(int, list-of-QTreeWidgetItem) """
        pass

    def isDisabled(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.isDisabled() -> bool """
        return False

    def isExpanded(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.isExpanded() -> bool """
        return False

    def isFirstColumnSpanned(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.isFirstColumnSpanned() -> bool """
        return False

    def isHidden(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.isHidden() -> bool """
        return False

    def isSelected(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.isSelected() -> bool """
        return False

    def parent(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.parent() -> QTreeWidgetItem """
        return QTreeWidgetItem

    def read(self, QDataStream): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.read(QDataStream) """
        pass

    def removeChild(self, QTreeWidgetItem): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.removeChild(QTreeWidgetItem) """
        pass

    def setBackground(self, p_int, QBrush): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setBackground(int, QBrush) """
        pass

    def setBackgroundColor(self, p_int, QColor): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setBackgroundColor(int, QColor) """
        pass

    def setCheckState(self, p_int, Qt_CheckState): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setCheckState(int, Qt.CheckState) """
        pass

    def setChildIndicatorPolicy(self, QTreeWidgetItem_ChildIndicatorPolicy): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setChildIndicatorPolicy(QTreeWidgetItem.ChildIndicatorPolicy) """
        pass

    def setData(self, p_int, p_int_1, p_object): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setData(int, int, object) """
        pass

    def setDisabled(self, bool): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setDisabled(bool) """
        pass

    def setExpanded(self, bool): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setExpanded(bool) """
        pass

    def setFirstColumnSpanned(self, bool): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setFirstColumnSpanned(bool) """
        pass

    def setFlags(self, Qt_ItemFlags): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setFlags(Qt.ItemFlags) """
        pass

    def setFont(self, p_int, QFont): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setFont(int, QFont) """
        pass

    def setForeground(self, p_int, QBrush): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setForeground(int, QBrush) """
        pass

    def setHidden(self, bool): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setHidden(bool) """
        pass

    def setIcon(self, p_int, QIcon): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setIcon(int, QIcon) """
        pass

    def setSelected(self, bool): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setSelected(bool) """
        pass

    def setSizeHint(self, p_int, QSize): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setSizeHint(int, QSize) """
        pass

    def setStatusTip(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setStatusTip(int, str) """
        pass

    def setText(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setText(int, str) """
        pass

    def setTextAlignment(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setTextAlignment(int, int) """
        pass

    def setTextColor(self, p_int, QColor): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setTextColor(int, QColor) """
        pass

    def setToolTip(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setToolTip(int, str) """
        pass

    def setWhatsThis(self, p_int, p_str): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.setWhatsThis(int, str) """
        pass

    def sizeHint(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.sizeHint(int) -> QSize """
        pass

    def sortChildren(self, p_int, Qt_SortOrder): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.sortChildren(int, Qt.SortOrder) """
        pass

    def statusTip(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.statusTip(int) -> str """
        return ""

    def takeChild(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.takeChild(int) -> QTreeWidgetItem """
        return QTreeWidgetItem

    def takeChildren(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.takeChildren() -> list-of-QTreeWidgetItem """
        pass

    def text(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.text(int) -> str """
        return ""

    def textAlignment(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.textAlignment(int) -> int """
        return 0

    def textColor(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.textColor(int) -> QColor """
        return QColor

    def toolTip(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.toolTip(int) -> str """
        return ""

    def treeWidget(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.treeWidget() -> QTreeWidget """
        return QTreeWidget

    def type(self): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.type() -> int """
        return 0

    def whatsThis(self, p_int): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.whatsThis(int) -> str """
        return ""

    def write(self, QDataStream): # real signature unknown; restored from __doc__
        """ QTreeWidgetItem.write(QDataStream) """
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


    ChildIndicatorPolicy = None # (!) real value is ''
    DontShowIndicator = 1
    DontShowIndicatorWhenChildless = 2
    ItemType = None # (!) real value is ''
    ShowIndicator = 0
    Type = 0
    UserType = 1000
    __hash__ = None


