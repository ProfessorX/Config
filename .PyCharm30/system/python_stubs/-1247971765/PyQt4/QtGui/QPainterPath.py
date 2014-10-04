# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QPainterPath(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QPainterPath()
    QPainterPath(QPointF)
    QPainterPath(QPainterPath)
    """
    def addEllipse(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.addEllipse(QRectF)
        QPainterPath.addEllipse(float, float, float, float)
        QPainterPath.addEllipse(QPointF, float, float)
        """
        pass

    def addPath(self, QPainterPath): # real signature unknown; restored from __doc__
        """ QPainterPath.addPath(QPainterPath) """
        pass

    def addPolygon(self, QPolygonF): # real signature unknown; restored from __doc__
        """ QPainterPath.addPolygon(QPolygonF) """
        pass

    def addRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.addRect(QRectF)
        QPainterPath.addRect(float, float, float, float)
        """
        pass

    def addRegion(self, QRegion): # real signature unknown; restored from __doc__
        """ QPainterPath.addRegion(QRegion) """
        pass

    def addRoundedRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.addRoundedRect(QRectF, float, float, Qt.SizeMode mode=Qt.AbsoluteSize)
        QPainterPath.addRoundedRect(float, float, float, float, float, float, Qt.SizeMode mode=Qt.AbsoluteSize)
        """
        pass

    def addRoundRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.addRoundRect(QRectF, int, int)
        QPainterPath.addRoundRect(float, float, float, float, int, int)
        QPainterPath.addRoundRect(QRectF, int)
        QPainterPath.addRoundRect(float, float, float, float, int)
        """
        pass

    def addText(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.addText(QPointF, QFont, str)
        QPainterPath.addText(float, float, QFont, str)
        """
        pass

    def angleAtPercent(self, p_float): # real signature unknown; restored from __doc__
        """ QPainterPath.angleAtPercent(float) -> float """
        return 0.0

    def arcMoveTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.arcMoveTo(QRectF, float)
        QPainterPath.arcMoveTo(float, float, float, float, float)
        """
        pass

    def arcTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.arcTo(QRectF, float, float)
        QPainterPath.arcTo(float, float, float, float, float, float)
        """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QPainterPath.boundingRect() -> QRectF """
        pass

    def closeSubpath(self): # real signature unknown; restored from __doc__
        """ QPainterPath.closeSubpath() """
        pass

    def connectPath(self, QPainterPath): # real signature unknown; restored from __doc__
        """ QPainterPath.connectPath(QPainterPath) """
        pass

    def contains(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.contains(QPointF) -> bool
        QPainterPath.contains(QRectF) -> bool
        QPainterPath.contains(QPainterPath) -> bool
        """
        return False

    def controlPointRect(self): # real signature unknown; restored from __doc__
        """ QPainterPath.controlPointRect() -> QRectF """
        pass

    def cubicTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.cubicTo(QPointF, QPointF, QPointF)
        QPainterPath.cubicTo(float, float, float, float, float, float)
        """
        pass

    def currentPosition(self): # real signature unknown; restored from __doc__
        """ QPainterPath.currentPosition() -> QPointF """
        pass

    def elementAt(self, p_int): # real signature unknown; restored from __doc__
        """ QPainterPath.elementAt(int) -> QPainterPath.Element """
        pass

    def elementCount(self): # real signature unknown; restored from __doc__
        """ QPainterPath.elementCount() -> int """
        return 0

    def fillRule(self): # real signature unknown; restored from __doc__
        """ QPainterPath.fillRule() -> Qt.FillRule """
        pass

    def intersected(self, QPainterPath): # real signature unknown; restored from __doc__
        """ QPainterPath.intersected(QPainterPath) -> QPainterPath """
        return QPainterPath

    def intersects(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.intersects(QRectF) -> bool
        QPainterPath.intersects(QPainterPath) -> bool
        """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QPainterPath.isEmpty() -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ QPainterPath.length() -> float """
        return 0.0

    def lineTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.lineTo(QPointF)
        QPainterPath.lineTo(float, float)
        """
        pass

    def moveTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.moveTo(QPointF)
        QPainterPath.moveTo(float, float)
        """
        pass

    def percentAtLength(self, p_float): # real signature unknown; restored from __doc__
        """ QPainterPath.percentAtLength(float) -> float """
        return 0.0

    def pointAtPercent(self, p_float): # real signature unknown; restored from __doc__
        """ QPainterPath.pointAtPercent(float) -> QPointF """
        pass

    def quadTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.quadTo(QPointF, QPointF)
        QPainterPath.quadTo(float, float, float, float)
        """
        pass

    def setElementPositionAt(self, p_int, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QPainterPath.setElementPositionAt(int, float, float) """
        pass

    def setFillRule(self, Qt_FillRule): # real signature unknown; restored from __doc__
        """ QPainterPath.setFillRule(Qt.FillRule) """
        pass

    def simplified(self): # real signature unknown; restored from __doc__
        """ QPainterPath.simplified() -> QPainterPath """
        return QPainterPath

    def slopeAtPercent(self, p_float): # real signature unknown; restored from __doc__
        """ QPainterPath.slopeAtPercent(float) -> float """
        return 0.0

    def subtracted(self, QPainterPath): # real signature unknown; restored from __doc__
        """ QPainterPath.subtracted(QPainterPath) -> QPainterPath """
        return QPainterPath

    def subtractedInverted(self, QPainterPath): # real signature unknown; restored from __doc__
        """ QPainterPath.subtractedInverted(QPainterPath) -> QPainterPath """
        return QPainterPath

    def swap(self, QPainterPath): # real signature unknown; restored from __doc__
        """ QPainterPath.swap(QPainterPath) """
        pass

    def toFillPolygon(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.toFillPolygon(QMatrix matrix=QMatrix()) -> QPolygonF
        QPainterPath.toFillPolygon(QTransform) -> QPolygonF
        """
        return QPolygonF

    def toFillPolygons(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.toFillPolygons(QMatrix matrix=QMatrix()) -> list-of-QPolygonF
        QPainterPath.toFillPolygons(QTransform) -> list-of-QPolygonF
        """
        pass

    def toReversed(self): # real signature unknown; restored from __doc__
        """ QPainterPath.toReversed() -> QPainterPath """
        return QPainterPath

    def toSubpathPolygons(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.toSubpathPolygons(QMatrix matrix=QMatrix()) -> list-of-QPolygonF
        QPainterPath.toSubpathPolygons(QTransform) -> list-of-QPolygonF
        """
        pass

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.translate(float, float)
        QPainterPath.translate(QPointF)
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPainterPath.translated(float, float) -> QPainterPath
        QPainterPath.translated(QPointF) -> QPainterPath
        """
        return QPainterPath

    def united(self, QPainterPath): # real signature unknown; restored from __doc__
        """ QPainterPath.united(QPainterPath) -> QPainterPath """
        return QPainterPath

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
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

    def __iadd__(self, *args, **kwargs): # real signature unknown
        """ Return self+=value. """
        pass

    def __iand__(self, *args, **kwargs): # real signature unknown
        """ Return self&=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __ior__(self, *args, **kwargs): # real signature unknown
        """ Return self|=value. """
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CurveToDataElement = 3
    CurveToElement = 2
    Element = None # (!) real value is ''
    ElementType = None # (!) real value is ''
    LineToElement = 1
    MoveToElement = 0
    __hash__ = None


