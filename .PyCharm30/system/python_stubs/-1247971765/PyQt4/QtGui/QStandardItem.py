# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QStandardItem(): # skipped bases: <class 'sip.wrapper'>
    """
    QStandardItem()
    QStandardItem(str)
    QStandardItem(QIcon, str)
    QStandardItem(int, int columns=1)
    QStandardItem(QStandardItem)
    """
    def accessibleDescription(self): # real signature unknown; restored from __doc__
        """ QStandardItem.accessibleDescription() -> str """
        return ""

    def accessibleText(self): # real signature unknown; restored from __doc__
        """ QStandardItem.accessibleText() -> str """
        return ""

    def appendColumn(self, list_of_QStandardItem): # real signature unknown; restored from __doc__
        """ QStandardItem.appendColumn(list-of-QStandardItem) """
        pass

    def appendRow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QStandardItem.appendRow(list-of-QStandardItem)
        QStandardItem.appendRow(QStandardItem)
        """
        pass

    def appendRows(self, list_of_QStandardItem): # real signature unknown; restored from __doc__
        """ QStandardItem.appendRows(list-of-QStandardItem) """
        pass

    def background(self): # real signature unknown; restored from __doc__
        """ QStandardItem.background() -> QBrush """
        return QBrush

    def checkState(self): # real signature unknown; restored from __doc__
        """ QStandardItem.checkState() -> Qt.CheckState """
        pass

    def child(self, p_int, int_column=0): # real signature unknown; restored from __doc__
        """ QStandardItem.child(int, int column=0) -> QStandardItem """
        return QStandardItem

    def clone(self): # real signature unknown; restored from __doc__
        """ QStandardItem.clone() -> QStandardItem """
        return QStandardItem

    def column(self): # real signature unknown; restored from __doc__
        """ QStandardItem.column() -> int """
        return 0

    def columnCount(self): # real signature unknown; restored from __doc__
        """ QStandardItem.columnCount() -> int """
        return 0

    def data(self, int_role=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QStandardItem.data(int role=Qt.UserRole+1) -> object """
        pass

    def emitDataChanged(self): # real signature unknown; restored from __doc__
        """ QStandardItem.emitDataChanged() """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ QStandardItem.flags() -> Qt.ItemFlags """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ QStandardItem.font() -> QFont """
        return QFont

    def foreground(self): # real signature unknown; restored from __doc__
        """ QStandardItem.foreground() -> QBrush """
        return QBrush

    def hasChildren(self): # real signature unknown; restored from __doc__
        """ QStandardItem.hasChildren() -> bool """
        return False

    def icon(self): # real signature unknown; restored from __doc__
        """ QStandardItem.icon() -> QIcon """
        return QIcon

    def index(self): # real signature unknown; restored from __doc__
        """ QStandardItem.index() -> QModelIndex """
        pass

    def insertColumn(self, p_int, list_of_QStandardItem): # real signature unknown; restored from __doc__
        """ QStandardItem.insertColumn(int, list-of-QStandardItem) """
        pass

    def insertColumns(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QStandardItem.insertColumns(int, int) """
        pass

    def insertRow(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QStandardItem.insertRow(int, list-of-QStandardItem)
        QStandardItem.insertRow(int, QStandardItem)
        """
        pass

    def insertRows(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QStandardItem.insertRows(int, int)
        QStandardItem.insertRows(int, list-of-QStandardItem)
        """
        pass

    def isCheckable(self): # real signature unknown; restored from __doc__
        """ QStandardItem.isCheckable() -> bool """
        return False

    def isDragEnabled(self): # real signature unknown; restored from __doc__
        """ QStandardItem.isDragEnabled() -> bool """
        return False

    def isDropEnabled(self): # real signature unknown; restored from __doc__
        """ QStandardItem.isDropEnabled() -> bool """
        return False

    def isEditable(self): # real signature unknown; restored from __doc__
        """ QStandardItem.isEditable() -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ QStandardItem.isEnabled() -> bool """
        return False

    def isSelectable(self): # real signature unknown; restored from __doc__
        """ QStandardItem.isSelectable() -> bool """
        return False

    def isTristate(self): # real signature unknown; restored from __doc__
        """ QStandardItem.isTristate() -> bool """
        return False

    def model(self): # real signature unknown; restored from __doc__
        """ QStandardItem.model() -> QStandardItemModel """
        return QStandardItemModel

    def parent(self): # real signature unknown; restored from __doc__
        """ QStandardItem.parent() -> QStandardItem """
        return QStandardItem

    def read(self, QDataStream): # real signature unknown; restored from __doc__
        """ QStandardItem.read(QDataStream) """
        pass

    def removeColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QStandardItem.removeColumn(int) """
        pass

    def removeColumns(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QStandardItem.removeColumns(int, int) """
        pass

    def removeRow(self, p_int): # real signature unknown; restored from __doc__
        """ QStandardItem.removeRow(int) """
        pass

    def removeRows(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QStandardItem.removeRows(int, int) """
        pass

    def row(self): # real signature unknown; restored from __doc__
        """ QStandardItem.row() -> int """
        return 0

    def rowCount(self): # real signature unknown; restored from __doc__
        """ QStandardItem.rowCount() -> int """
        return 0

    def setAccessibleDescription(self, p_str): # real signature unknown; restored from __doc__
        """ QStandardItem.setAccessibleDescription(str) """
        pass

    def setAccessibleText(self, p_str): # real signature unknown; restored from __doc__
        """ QStandardItem.setAccessibleText(str) """
        pass

    def setBackground(self, QBrush): # real signature unknown; restored from __doc__
        """ QStandardItem.setBackground(QBrush) """
        pass

    def setCheckable(self, bool): # real signature unknown; restored from __doc__
        """ QStandardItem.setCheckable(bool) """
        pass

    def setCheckState(self, Qt_CheckState): # real signature unknown; restored from __doc__
        """ QStandardItem.setCheckState(Qt.CheckState) """
        pass

    def setChild(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QStandardItem.setChild(int, int, QStandardItem)
        QStandardItem.setChild(int, QStandardItem)
        """
        pass

    def setColumnCount(self, p_int): # real signature unknown; restored from __doc__
        """ QStandardItem.setColumnCount(int) """
        pass

    def setData(self, p_object, int_role=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QStandardItem.setData(object, int role=Qt.UserRole+1) """
        pass

    def setDragEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QStandardItem.setDragEnabled(bool) """
        pass

    def setDropEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QStandardItem.setDropEnabled(bool) """
        pass

    def setEditable(self, bool): # real signature unknown; restored from __doc__
        """ QStandardItem.setEditable(bool) """
        pass

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QStandardItem.setEnabled(bool) """
        pass

    def setFlags(self, Qt_ItemFlags): # real signature unknown; restored from __doc__
        """ QStandardItem.setFlags(Qt.ItemFlags) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ QStandardItem.setFont(QFont) """
        pass

    def setForeground(self, QBrush): # real signature unknown; restored from __doc__
        """ QStandardItem.setForeground(QBrush) """
        pass

    def setIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ QStandardItem.setIcon(QIcon) """
        pass

    def setRowCount(self, p_int): # real signature unknown; restored from __doc__
        """ QStandardItem.setRowCount(int) """
        pass

    def setSelectable(self, bool): # real signature unknown; restored from __doc__
        """ QStandardItem.setSelectable(bool) """
        pass

    def setSizeHint(self, QSize): # real signature unknown; restored from __doc__
        """ QStandardItem.setSizeHint(QSize) """
        pass

    def setStatusTip(self, p_str): # real signature unknown; restored from __doc__
        """ QStandardItem.setStatusTip(str) """
        pass

    def setText(self, p_str): # real signature unknown; restored from __doc__
        """ QStandardItem.setText(str) """
        pass

    def setTextAlignment(self, Qt_Alignment): # real signature unknown; restored from __doc__
        """ QStandardItem.setTextAlignment(Qt.Alignment) """
        pass

    def setToolTip(self, p_str): # real signature unknown; restored from __doc__
        """ QStandardItem.setToolTip(str) """
        pass

    def setTristate(self, bool): # real signature unknown; restored from __doc__
        """ QStandardItem.setTristate(bool) """
        pass

    def setWhatsThis(self, p_str): # real signature unknown; restored from __doc__
        """ QStandardItem.setWhatsThis(str) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QStandardItem.sizeHint() -> QSize """
        pass

    def sortChildren(self, p_int, Qt_SortOrder_order=None): # real signature unknown; restored from __doc__
        """ QStandardItem.sortChildren(int, Qt.SortOrder order=Qt.AscendingOrder) """
        pass

    def statusTip(self): # real signature unknown; restored from __doc__
        """ QStandardItem.statusTip() -> str """
        return ""

    def takeChild(self, p_int, int_column=0): # real signature unknown; restored from __doc__
        """ QStandardItem.takeChild(int, int column=0) -> QStandardItem """
        return QStandardItem

    def takeColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QStandardItem.takeColumn(int) -> list-of-QStandardItem """
        pass

    def takeRow(self, p_int): # real signature unknown; restored from __doc__
        """ QStandardItem.takeRow(int) -> list-of-QStandardItem """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ QStandardItem.text() -> str """
        return ""

    def textAlignment(self): # real signature unknown; restored from __doc__
        """ QStandardItem.textAlignment() -> Qt.Alignment """
        pass

    def toolTip(self): # real signature unknown; restored from __doc__
        """ QStandardItem.toolTip() -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ QStandardItem.type() -> int """
        return 0

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ QStandardItem.whatsThis() -> str """
        return ""

    def write(self, QDataStream): # real signature unknown; restored from __doc__
        """ QStandardItem.write(QDataStream) """
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


