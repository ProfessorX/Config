# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QMatrix4x4(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QMatrix4x4()
    QMatrix4x4(sequence-of-float)
    QMatrix4x4(float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float)
    QMatrix4x4(QTransform)
    QMatrix4x4(QMatrix)
    QMatrix4x4(QMatrix4x4)
    """
    def column(self, p_int): # real signature unknown; restored from __doc__
        """ QMatrix4x4.column(int) -> QVector4D """
        return QVector4D

    def copyDataTo(self): # real signature unknown; restored from __doc__
        """ QMatrix4x4.copyDataTo() -> list-of-float """
        pass

    def data(self): # real signature unknown; restored from __doc__
        """ QMatrix4x4.data() -> list-of-float """
        pass

    def determinant(self): # real signature unknown; restored from __doc__
        """ QMatrix4x4.determinant() -> float """
        return 0.0

    def fill(self, p_float): # real signature unknown; restored from __doc__
        """ QMatrix4x4.fill(float) """
        pass

    def flipCoordinates(self): # real signature unknown; restored from __doc__
        """ QMatrix4x4.flipCoordinates() """
        pass

    def frustum(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5): # real signature unknown; restored from __doc__
        """ QMatrix4x4.frustum(float, float, float, float, float, float) """
        pass

    def inverted(self): # real signature unknown; restored from __doc__
        """ QMatrix4x4.inverted() -> (QMatrix4x4, bool) """
        pass

    def isIdentity(self): # real signature unknown; restored from __doc__
        """ QMatrix4x4.isIdentity() -> bool """
        return False

    def lookAt(self, QVector3D, QVector3D_1, QVector3D_2): # real signature unknown; restored from __doc__
        """ QMatrix4x4.lookAt(QVector3D, QVector3D, QVector3D) """
        pass

    def map(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMatrix4x4.map(QPoint) -> QPoint
        QMatrix4x4.map(QPointF) -> QPointF
        QMatrix4x4.map(QVector3D) -> QVector3D
        QMatrix4x4.map(QVector4D) -> QVector4D
        """
        return QVector3D or QVector4D

    def mapRect(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMatrix4x4.mapRect(QRect) -> QRect
        QMatrix4x4.mapRect(QRectF) -> QRectF
        """
        pass

    def mapVector(self, QVector3D): # real signature unknown; restored from __doc__
        """ QMatrix4x4.mapVector(QVector3D) -> QVector3D """
        return QVector3D

    def normalMatrix(self): # real signature unknown; restored from __doc__
        """ QMatrix4x4.normalMatrix() -> QMatrix3x3 """
        return QMatrix3x3

    def optimize(self): # real signature unknown; restored from __doc__
        """ QMatrix4x4.optimize() """
        pass

    def ortho(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMatrix4x4.ortho(QRect)
        QMatrix4x4.ortho(QRectF)
        QMatrix4x4.ortho(float, float, float, float, float, float)
        """
        pass

    def perspective(self, p_float, p_float_1, p_float_2, p_float_3): # real signature unknown; restored from __doc__
        """ QMatrix4x4.perspective(float, float, float, float) """
        pass

    def rotate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMatrix4x4.rotate(float, QVector3D)
        QMatrix4x4.rotate(float, float, float, float z=0)
        QMatrix4x4.rotate(QQuaternion)
        """
        pass

    def row(self, p_int): # real signature unknown; restored from __doc__
        """ QMatrix4x4.row(int) -> QVector4D """
        return QVector4D

    def scale(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMatrix4x4.scale(QVector3D)
        QMatrix4x4.scale(float, float)
        QMatrix4x4.scale(float, float, float)
        QMatrix4x4.scale(float)
        """
        pass

    def setColumn(self, p_int, QVector4D): # real signature unknown; restored from __doc__
        """ QMatrix4x4.setColumn(int, QVector4D) """
        pass

    def setRow(self, p_int, QVector4D): # real signature unknown; restored from __doc__
        """ QMatrix4x4.setRow(int, QVector4D) """
        pass

    def setToIdentity(self): # real signature unknown; restored from __doc__
        """ QMatrix4x4.setToIdentity() """
        pass

    def toAffine(self): # real signature unknown; restored from __doc__
        """ QMatrix4x4.toAffine() -> QMatrix """
        return QMatrix

    def toTransform(self, p_float=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMatrix4x4.toTransform() -> QTransform
        QMatrix4x4.toTransform(float) -> QTransform
        """
        return QTransform

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QMatrix4x4.translate(QVector3D)
        QMatrix4x4.translate(float, float)
        QMatrix4x4.translate(float, float, float)
        """
        pass

    def transposed(self): # real signature unknown; restored from __doc__
        """ QMatrix4x4.transposed() -> QMatrix4x4 """
        return QMatrix4x4

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
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

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
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

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


