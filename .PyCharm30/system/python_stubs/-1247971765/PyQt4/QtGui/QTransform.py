# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QTransform(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QTransform()
    QTransform(float, float, float, float, float, float, float, float, float m33=1)
    QTransform(float, float, float, float, float, float)
    QTransform(QMatrix)
    QTransform(QTransform)
    """
    def adjoint(self): # real signature unknown; restored from __doc__
        """ QTransform.adjoint() -> QTransform """
        return QTransform

    def det(self): # real signature unknown; restored from __doc__
        """ QTransform.det() -> float """
        return 0.0

    def determinant(self): # real signature unknown; restored from __doc__
        """ QTransform.determinant() -> float """
        return 0.0

    def dx(self): # real signature unknown; restored from __doc__
        """ QTransform.dx() -> float """
        return 0.0

    def dy(self): # real signature unknown; restored from __doc__
        """ QTransform.dy() -> float """
        return 0.0

    def fromScale(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QTransform.fromScale(float, float) -> QTransform """
        return QTransform

    def fromTranslate(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QTransform.fromTranslate(float, float) -> QTransform """
        return QTransform

    def inverted(self): # real signature unknown; restored from __doc__
        """ QTransform.inverted() -> (QTransform, bool) """
        pass

    def isAffine(self): # real signature unknown; restored from __doc__
        """ QTransform.isAffine() -> bool """
        return False

    def isIdentity(self): # real signature unknown; restored from __doc__
        """ QTransform.isIdentity() -> bool """
        return False

    def isInvertible(self): # real signature unknown; restored from __doc__
        """ QTransform.isInvertible() -> bool """
        return False

    def isRotating(self): # real signature unknown; restored from __doc__
        """ QTransform.isRotating() -> bool """
        return False

    def isScaling(self): # real signature unknown; restored from __doc__
        """ QTransform.isScaling() -> bool """
        return False

    def isTranslating(self): # real signature unknown; restored from __doc__
        """ QTransform.isTranslating() -> bool """
        return False

    def m11(self): # real signature unknown; restored from __doc__
        """ QTransform.m11() -> float """
        return 0.0

    def m12(self): # real signature unknown; restored from __doc__
        """ QTransform.m12() -> float """
        return 0.0

    def m13(self): # real signature unknown; restored from __doc__
        """ QTransform.m13() -> float """
        return 0.0

    def m21(self): # real signature unknown; restored from __doc__
        """ QTransform.m21() -> float """
        return 0.0

    def m22(self): # real signature unknown; restored from __doc__
        """ QTransform.m22() -> float """
        return 0.0

    def m23(self): # real signature unknown; restored from __doc__
        """ QTransform.m23() -> float """
        return 0.0

    def m31(self): # real signature unknown; restored from __doc__
        """ QTransform.m31() -> float """
        return 0.0

    def m32(self): # real signature unknown; restored from __doc__
        """ QTransform.m32() -> float """
        return 0.0

    def m33(self): # real signature unknown; restored from __doc__
        """ QTransform.m33() -> float """
        return 0.0

    def map(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTransform.map(int, int) -> (int, int)
        QTransform.map(float, float) -> (float, float)
        QTransform.map(QPoint) -> QPoint
        QTransform.map(QPointF) -> QPointF
        QTransform.map(QLine) -> QLine
        QTransform.map(QLineF) -> QLineF
        QTransform.map(QPolygonF) -> QPolygonF
        QTransform.map(QPolygon) -> QPolygon
        QTransform.map(QRegion) -> QRegion
        QTransform.map(QPainterPath) -> QPainterPath
        """
        return QPolygonF or QPolygon or QRegion or QPainterPath

    def mapRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTransform.mapRect(QRect) -> QRect
        QTransform.mapRect(QRectF) -> QRectF
        """
        pass

    def mapToPolygon(self, QRect): # real signature unknown; restored from __doc__
        """ QTransform.mapToPolygon(QRect) -> QPolygon """
        return QPolygon

    def quadToQuad(self, QPolygonF, QPolygonF_1, QTransform): # real signature unknown; restored from __doc__
        """ QTransform.quadToQuad(QPolygonF, QPolygonF, QTransform) -> bool """
        return False

    def quadToSquare(self, QPolygonF, QTransform): # real signature unknown; restored from __doc__
        """ QTransform.quadToSquare(QPolygonF, QTransform) -> bool """
        return False

    def reset(self): # real signature unknown; restored from __doc__
        """ QTransform.reset() """
        pass

    def rotate(self, p_float, Qt_Axis_axis=None): # real signature unknown; restored from __doc__
        """ QTransform.rotate(float, Qt.Axis axis=Qt.ZAxis) -> QTransform """
        return QTransform

    def rotateRadians(self, p_float, Qt_Axis_axis=None): # real signature unknown; restored from __doc__
        """ QTransform.rotateRadians(float, Qt.Axis axis=Qt.ZAxis) -> QTransform """
        return QTransform

    def scale(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QTransform.scale(float, float) -> QTransform """
        return QTransform

    def setMatrix(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5, p_float_6, p_float_7, p_float_8): # real signature unknown; restored from __doc__
        """ QTransform.setMatrix(float, float, float, float, float, float, float, float, float) """
        pass

    def shear(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QTransform.shear(float, float) -> QTransform """
        return QTransform

    def squareToQuad(self, QPolygonF, QTransform): # real signature unknown; restored from __doc__
        """ QTransform.squareToQuad(QPolygonF, QTransform) -> bool """
        return False

    def toAffine(self): # real signature unknown; restored from __doc__
        """ QTransform.toAffine() -> QMatrix """
        return QMatrix

    def translate(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QTransform.translate(float, float) -> QTransform """
        return QTransform

    def transposed(self): # real signature unknown; restored from __doc__
        """ QTransform.transposed() -> QTransform """
        return QTransform

    def type(self): # real signature unknown; restored from __doc__
        """ QTransform.type() -> QTransform.TransformationType """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
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

    def __imul__(self, *args, **kwargs): # real signature unknown
        """ Return self*=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __isub__(self, *args, **kwargs): # real signature unknown
        """ Return self-=value. """
        pass

    def __itruediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
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

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    TransformationType = None # (!) real value is ''
    TxNone = 0
    TxProject = 16
    TxRotate = 4
    TxScale = 2
    TxShear = 8
    TxTranslate = 1
    __hash__ = None


