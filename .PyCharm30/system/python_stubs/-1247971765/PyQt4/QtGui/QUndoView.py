# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from .QListView import QListView

class QUndoView(QListView):
    """
    QUndoView(QWidget parent=None)
    QUndoView(QUndoStack, QWidget parent=None)
    QUndoView(QUndoGroup, QWidget parent=None)
    """
    def cleanIcon(self): # real signature unknown; restored from __doc__
        """ QUndoView.cleanIcon() -> QIcon """
        return QIcon

    def emptyLabel(self): # real signature unknown; restored from __doc__
        """ QUndoView.emptyLabel() -> str """
        return ""

    def group(self): # real signature unknown; restored from __doc__
        """ QUndoView.group() -> QUndoGroup """
        return QUndoGroup

    def setCleanIcon(self, QIcon): # real signature unknown; restored from __doc__
        """ QUndoView.setCleanIcon(QIcon) """
        pass

    def setEmptyLabel(self, p_str): # real signature unknown; restored from __doc__
        """ QUndoView.setEmptyLabel(str) """
        pass

    def setGroup(self, QUndoGroup): # real signature unknown; restored from __doc__
        """ QUndoView.setGroup(QUndoGroup) """
        pass

    def setStack(self, QUndoStack): # real signature unknown; restored from __doc__
        """ QUndoView.setStack(QUndoStack) """
        pass

    def stack(self): # real signature unknown; restored from __doc__
        """ QUndoView.stack() -> QUndoStack """
        return QUndoStack

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


