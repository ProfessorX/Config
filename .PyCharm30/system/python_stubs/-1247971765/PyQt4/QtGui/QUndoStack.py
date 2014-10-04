# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QUndoStack(__PyQt4_QtCore.QObject):
    """ QUndoStack(QObject parent=None) """
    def beginMacro(self, p_str): # real signature unknown; restored from __doc__
        """ QUndoStack.beginMacro(str) """
        pass

    def canRedo(self): # real signature unknown; restored from __doc__
        """ QUndoStack.canRedo() -> bool """
        return False

    def canRedoChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoStack.canRedoChanged[bool] [signal] """
        pass

    def canUndo(self): # real signature unknown; restored from __doc__
        """ QUndoStack.canUndo() -> bool """
        return False

    def canUndoChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoStack.canUndoChanged[bool] [signal] """
        pass

    def cleanChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoStack.cleanChanged[bool] [signal] """
        pass

    def cleanIndex(self): # real signature unknown; restored from __doc__
        """ QUndoStack.cleanIndex() -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ QUndoStack.clear() """
        pass

    def command(self, p_int): # real signature unknown; restored from __doc__
        """ QUndoStack.command(int) -> QUndoCommand """
        return QUndoCommand

    def count(self): # real signature unknown; restored from __doc__
        """ QUndoStack.count() -> int """
        return 0

    def createRedoAction(self, QObject, str_prefix=''): # real signature unknown; restored from __doc__
        """ QUndoStack.createRedoAction(QObject, str prefix='') -> QAction """
        return QAction

    def createUndoAction(self, QObject, str_prefix=''): # real signature unknown; restored from __doc__
        """ QUndoStack.createUndoAction(QObject, str prefix='') -> QAction """
        return QAction

    def endMacro(self): # real signature unknown; restored from __doc__
        """ QUndoStack.endMacro() """
        pass

    def index(self): # real signature unknown; restored from __doc__
        """ QUndoStack.index() -> int """
        return 0

    def indexChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoStack.indexChanged[int] [signal] """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ QUndoStack.isActive() -> bool """
        return False

    def isClean(self): # real signature unknown; restored from __doc__
        """ QUndoStack.isClean() -> bool """
        return False

    def push(self, QUndoCommand): # real signature unknown; restored from __doc__
        """ QUndoStack.push(QUndoCommand) """
        pass

    def redo(self): # real signature unknown; restored from __doc__
        """ QUndoStack.redo() """
        pass

    def redoText(self): # real signature unknown; restored from __doc__
        """ QUndoStack.redoText() -> str """
        return ""

    def redoTextChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoStack.redoTextChanged[str] [signal] """
        pass

    def setActive(self, bool_active=True): # real signature unknown; restored from __doc__
        """ QUndoStack.setActive(bool active=True) """
        pass

    def setClean(self): # real signature unknown; restored from __doc__
        """ QUndoStack.setClean() """
        pass

    def setIndex(self, p_int): # real signature unknown; restored from __doc__
        """ QUndoStack.setIndex(int) """
        pass

    def setUndoLimit(self, p_int): # real signature unknown; restored from __doc__
        """ QUndoStack.setUndoLimit(int) """
        pass

    def text(self, p_int): # real signature unknown; restored from __doc__
        """ QUndoStack.text(int) -> str """
        return ""

    def undo(self): # real signature unknown; restored from __doc__
        """ QUndoStack.undo() """
        pass

    def undoLimit(self): # real signature unknown; restored from __doc__
        """ QUndoStack.undoLimit() -> int """
        return 0

    def undoText(self): # real signature unknown; restored from __doc__
        """ QUndoStack.undoText() -> str """
        return ""

    def undoTextChanged(self, *args, **kwargs): # real signature unknown
        """ QUndoStack.undoTextChanged[str] [signal] """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass


