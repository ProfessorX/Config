# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QTableWidgetItem(): # skipped bases: <class 'sip.wrapper'>
    """
    QTableWidgetItem(int type=QTableWidgetItem.Type)
    QTableWidgetItem(str, int type=QTableWidgetItem.Type)
    QTableWidgetItem(QIcon, str, int type=QTableWidgetItem.Type)
    QTableWidgetItem(QTableWidgetItem)
    """
    def background(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.background() -> QBrush """
        return QBrush

    def backgroundColor(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.backgroundColor() -> QColor """
        return QColor

    def checkState(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.checkState() -> Qt.CheckState """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.clone() -> QTableWidgetItem """
        return QTableWidgetItem

    def column(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.column() -> int """
        return 0

    def data(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.data(int) -> object """
        return object()

    def flags(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.flags() -> Qt.ItemFlags """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.font() -> QFont """
        return QFont

    def foreground(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.foreground() -> QBrush """
        return QBrush

    def icon(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.icon() -> QIcon """
        return QIcon

    def isSelected(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.isSelected() -> bool """
        return False

    def read(self, QDataStream): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.read(QDataStream) """
        pass

    def row(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.row() -> int """
        return 0

    def setBackground(self, QBrush): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.setBackground(QBrush) """
        pass

    def setBackgroundColor(self, QColor): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.setBackgroundColor(QColor) """
        pass

    def setCheckState(self, Qt_CheckState): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.setCheckState(Qt.CheckState) """
        pass

    def setData(self, p_int, p_object): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.setData(int, object) """
        pass

    def setFlags(self, Qt_ItemFlags): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.setFlags(Qt.ItemFlags) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.setFont(QFont) """
        pass

    def setForeground(self, QBrush): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.setForeground(QBrush) """
        pass

    def setIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.setIcon(QIcon) """
        pass

    def setSelected(self, bool): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.setSelected(bool) """
        pass

    def setSizeHint(self, QSize): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.setSizeHint(QSize) """
        pass

    def setStatusTip(self, p_str): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.setStatusTip(str) """
        pass

    def setText(self, p_str): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.setText(str) """
        pass

    def setTextAlignment(self, p_int): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.setTextAlignment(int) """
        pass

    def setTextColor(self, QColor): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.setTextColor(QColor) """
        pass

    def setToolTip(self, p_str): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.setToolTip(str) """
        pass

    def setWhatsThis(self, p_str): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.setWhatsThis(str) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.sizeHint() -> QSize """
        pass

    def statusTip(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.statusTip() -> str """
        return ""

    def tableWidget(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.tableWidget() -> QTableWidget """
        return QTableWidget

    def text(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.text() -> str """
        return ""

    def textAlignment(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.textAlignment() -> int """
        return 0

    def textColor(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.textColor() -> QColor """
        return QColor

    def toolTip(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.toolTip() -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.type() -> int """
        return 0

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.whatsThis() -> str """
        return ""

    def write(self, QDataStream): # real signature unknown; restored from __doc__
        """ QTableWidgetItem.write(QDataStream) """
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


