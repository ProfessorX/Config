# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from .QAbstractGraphicsShapeItem import QAbstractGraphicsShapeItem

class QGraphicsSimpleTextItem(QAbstractGraphicsShapeItem):
    """
    QGraphicsSimpleTextItem(QGraphicsItem parent=None, QGraphicsScene scene=None)
    QGraphicsSimpleTextItem(str, QGraphicsItem parent=None, QGraphicsScene scene=None)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QGraphicsSimpleTextItem.boundingRect() -> QRectF """
        pass

    def contains(self, QPointF): # real signature unknown; restored from __doc__
        """ QGraphicsSimpleTextItem.contains(QPointF) -> bool """
        return False

    def font(self): # real signature unknown; restored from __doc__
        """ QGraphicsSimpleTextItem.font() -> QFont """
        return QFont

    def isObscuredBy(self, QGraphicsItem): # real signature unknown; restored from __doc__
        """ QGraphicsSimpleTextItem.isObscuredBy(QGraphicsItem) -> bool """
        return False

    def opaqueArea(self): # real signature unknown; restored from __doc__
        """ QGraphicsSimpleTextItem.opaqueArea() -> QPainterPath """
        return QPainterPath

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget): # real signature unknown; restored from __doc__
        """ QGraphicsSimpleTextItem.paint(QPainter, QStyleOptionGraphicsItem, QWidget) """
        pass

    def setFont(self, QFont): # real signature unknown; restored from __doc__
        """ QGraphicsSimpleTextItem.setFont(QFont) """
        pass

    def setText(self, p_str): # real signature unknown; restored from __doc__
        """ QGraphicsSimpleTextItem.setText(str) """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ QGraphicsSimpleTextItem.shape() -> QPainterPath """
        return QPainterPath

    def text(self): # real signature unknown; restored from __doc__
        """ QGraphicsSimpleTextItem.text() -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ QGraphicsSimpleTextItem.type() -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


