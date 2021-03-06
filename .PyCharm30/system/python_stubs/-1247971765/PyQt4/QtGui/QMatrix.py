# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QMatrix(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QMatrix()
    QMatrix(float, float, float, float, float, float)
    QMatrix(QMatrix)
    """
    def det(self): # real signature unknown; restored from __doc__
        """ QMatrix.det() -> float """
        return 0.0

    def determinant(self): # real signature unknown; restored from __doc__
        """ QMatrix.determinant() -> float """
        return 0.0

    def dx(self): # real signature unknown; restored from __doc__
        """ QMatrix.dx() -> float """
        return 0.0

    def dy(self): # real signature unknown; restored from __doc__
        """ QMatrix.dy() -> float """
        return 0.0

    def inverted(self): # real signature unknown; restored from __doc__
        """ QMatrix.inverted() -> (QMatrix, bool) """
        pass

    def isIdentity(self): # real signature unknown; restored from __doc__
        """ QMatrix.isIdentity() -> bool """
        return False

    def isInvertible(self): # real signature unknown; restored from __doc__
        """ QMatrix.isInvertible() -> bool """
        return False

    def m11(self): # real signature unknown; restored from __doc__
        """ QMatrix.m11() -> float """
        return 0.0

    def m12(self): # real signature unknown; restored from __doc__
        """ QMatrix.m12() -> float """
        return 0.0

    def m21(self): # real signature unknown; restored from __doc__
        """ QMatrix.m21() -> float """
        return 0.0

    def m22(self): # real signature unknown; restored from __doc__
        """ QMatrix.m22() -> float """
        return 0.0

    def map(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMatrix.map(int, int) -> (int, int)
        QMatrix.map(float, float) -> (float, float)
        QMatrix.map(QPoint) -> QPoint
        QMatrix.map(QPointF) -> QPointF
        QMatrix.map(QLine) -> QLine
        QMatrix.map(QLineF) -> QLineF
        QMatrix.map(QPolygonF) -> QPolygonF
        QMatrix.map(QPolygon) -> QPolygon
        QMatrix.map(QRegion) -> QRegion
        QMatrix.map(QPainterPath) -> QPainterPath
        """
        return QPolygonF or QPolygon or QRegion or QPainterPath

    def mapRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMatrix.mapRect(QRect) -> QRect
        QMatrix.mapRect(QRectF) -> QRectF
        """
        pass

    def mapToPolygon(self, QRect): # real signature unknown; restored from __doc__
        """ QMatrix.mapToPolygon(QRect) -> QPolygon """
        return QPolygon

    def reset(self): # real signature unknown; restored from __doc__
        """ QMatrix.reset() """
        pass

    def rotate(self, p_float): # real signature unknown; restored from __doc__
        """ QMatrix.rotate(float) -> QMatrix """
        return QMatrix

    def scale(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QMatrix.scale(float, float) -> QMatrix """
        return QMatrix

    def setMatrix(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5): # real signature unknown; restored from __doc__
        """ QMatrix.setMatrix(float, float, float, float, float, float) """
        pass

    def shear(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QMatrix.shear(float, float) -> QMatrix """
        return QMatrix

    def translate(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QMatrix.translate(float, float) -> QMatrix """
        return QMatrix

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Return self*=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


