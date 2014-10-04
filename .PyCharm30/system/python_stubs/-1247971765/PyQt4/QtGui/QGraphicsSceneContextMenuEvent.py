# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from .QGraphicsSceneEvent import QGraphicsSceneEvent

class QGraphicsSceneContextMenuEvent(QGraphicsSceneEvent):
    # no doc
    def modifiers(self): # real signature unknown; restored from __doc__
        """ QGraphicsSceneContextMenuEvent.modifiers() -> Qt.KeyboardModifiers """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ QGraphicsSceneContextMenuEvent.pos() -> QPointF """
        pass

    def reason(self): # real signature unknown; restored from __doc__
        """ QGraphicsSceneContextMenuEvent.reason() -> QGraphicsSceneContextMenuEvent.Reason """
        pass

    def scenePos(self): # real signature unknown; restored from __doc__
        """ QGraphicsSceneContextMenuEvent.scenePos() -> QPointF """
        pass

    def screenPos(self): # real signature unknown; restored from __doc__
        """ QGraphicsSceneContextMenuEvent.screenPos() -> QPoint """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Keyboard = 1
    Mouse = 0
    Other = 2
    Reason = None # (!) real value is ''


