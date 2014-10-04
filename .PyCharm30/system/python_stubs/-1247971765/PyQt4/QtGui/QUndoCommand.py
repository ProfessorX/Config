# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QUndoCommand(): # skipped bases: <class 'sip.wrapper'>
    """
    QUndoCommand(QUndoCommand parent=None)
    QUndoCommand(str, QUndoCommand parent=None)
    """
    def actionText(self): # real signature unknown; restored from __doc__
        """ QUndoCommand.actionText() -> str """
        return ""

    def child(self, p_int): # real signature unknown; restored from __doc__
        """ QUndoCommand.child(int) -> QUndoCommand """
        return QUndoCommand

    def childCount(self): # real signature unknown; restored from __doc__
        """ QUndoCommand.childCount() -> int """
        return 0

    def id(self): # real signature unknown; restored from __doc__
        """ QUndoCommand.id() -> int """
        return 0

    def mergeWith(self, QUndoCommand): # real signature unknown; restored from __doc__
        """ QUndoCommand.mergeWith(QUndoCommand) -> bool """
        return False

    def redo(self): # real signature unknown; restored from __doc__
        """ QUndoCommand.redo() """
        pass

    def setText(self, p_str): # real signature unknown; restored from __doc__
        """ QUndoCommand.setText(str) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ QUndoCommand.text() -> str """
        return ""

    def undo(self): # real signature unknown; restored from __doc__
        """ QUndoCommand.undo() """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



