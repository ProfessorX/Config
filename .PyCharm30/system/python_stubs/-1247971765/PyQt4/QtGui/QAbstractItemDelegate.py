# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QAbstractItemDelegate(__PyQt4_QtCore.QObject):
    """ QAbstractItemDelegate(QObject parent=None) """
    def closeEditor(self, *args, **kwargs): # real signature unknown
        """
        QAbstractItemDelegate.closeEditor[QWidget, QAbstractItemDelegate.EndEditHint] [signal]
        QAbstractItemDelegate.closeEditor[QWidget] [signal]
        """
        pass

    def commitData(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemDelegate.commitData[QWidget] [signal] """
        pass

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemDelegate.createEditor(QWidget, QStyleOptionViewItem, QModelIndex) -> QWidget """
        return QWidget

    def editorEvent(self, QEvent, QAbstractItemModel, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemDelegate.editorEvent(QEvent, QAbstractItemModel, QStyleOptionViewItem, QModelIndex) -> bool """
        return False

    def elidedText(self, QFontMetrics, p_int, Qt_TextElideMode, p_str): # real signature unknown; restored from __doc__
        """ QAbstractItemDelegate.elidedText(QFontMetrics, int, Qt.TextElideMode, str) -> str """
        return ""

    def helpEvent(self, QHelpEvent, QAbstractItemView, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemDelegate.helpEvent(QHelpEvent, QAbstractItemView, QStyleOptionViewItem, QModelIndex) -> bool """
        return False

    def paint(self, QPainter, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemDelegate.paint(QPainter, QStyleOptionViewItem, QModelIndex) """
        pass

    def setEditorData(self, QWidget, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemDelegate.setEditorData(QWidget, QModelIndex) """
        pass

    def setModelData(self, QWidget, QAbstractItemModel, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemDelegate.setModelData(QWidget, QAbstractItemModel, QModelIndex) """
        pass

    def sizeHint(self, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemDelegate.sizeHint(QStyleOptionViewItem, QModelIndex) -> QSize """
        pass

    def sizeHintChanged(self, *args, **kwargs): # real signature unknown
        """ QAbstractItemDelegate.sizeHintChanged[QModelIndex] [signal] """
        pass

    def updateEditorGeometry(self, QWidget, QStyleOptionViewItem, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractItemDelegate.updateEditorGeometry(QWidget, QStyleOptionViewItem, QModelIndex) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    EditNextItem = 1
    EditPreviousItem = 2
    EndEditHint = None # (!) real value is ''
    NoHint = 0
    RevertModelCache = 4
    SubmitModelCache = 3


