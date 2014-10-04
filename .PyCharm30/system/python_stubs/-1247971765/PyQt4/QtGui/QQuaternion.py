# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QQuaternion(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QQuaternion()
    QQuaternion(float, float, float, float)
    QQuaternion(float, QVector3D)
    QQuaternion(QVector4D)
    QQuaternion(QQuaternion)
    """
    def conjugate(self): # real signature unknown; restored from __doc__
        """ QQuaternion.conjugate() -> QQuaternion """
        return QQuaternion

    def fromAxisAndAngle(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QQuaternion.fromAxisAndAngle(QVector3D, float) -> QQuaternion
        QQuaternion.fromAxisAndAngle(float, float, float, float) -> QQuaternion
        """
        return QQuaternion

    def isIdentity(self): # real signature unknown; restored from __doc__
        """ QQuaternion.isIdentity() -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QQuaternion.isNull() -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ QQuaternion.length() -> float """
        return 0.0

    def lengthSquared(self): # real signature unknown; restored from __doc__
        """ QQuaternion.lengthSquared() -> float """
        return 0.0

    def nlerp(self, QQuaternion, QQuaternion_1, p_float): # real signature unknown; restored from __doc__
        """ QQuaternion.nlerp(QQuaternion, QQuaternion, float) -> QQuaternion """
        return QQuaternion

    def normalize(self): # real signature unknown; restored from __doc__
        """ QQuaternion.normalize() """
        pass

    def normalized(self): # real signature unknown; restored from __doc__
        """ QQuaternion.normalized() -> QQuaternion """
        return QQuaternion

    def rotatedVector(self, QVector3D): # real signature unknown; restored from __doc__
        """ QQuaternion.rotatedVector(QVector3D) -> QVector3D """
        return QVector3D

    def scalar(self): # real signature unknown; restored from __doc__
        """ QQuaternion.scalar() -> float """
        return 0.0

    def setScalar(self, p_float): # real signature unknown; restored from __doc__
        """ QQuaternion.setScalar(float) """
        pass

    def setVector(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QQuaternion.setVector(QVector3D)
        QQuaternion.setVector(float, float, float)
        """
        pass

    def setX(self, p_float): # real signature unknown; restored from __doc__
        """ QQuaternion.setX(float) """
        pass

    def setY(self, p_float): # real signature unknown; restored from __doc__
        """ QQuaternion.setY(float) """
        pass

    def setZ(self, p_float): # real signature unknown; restored from __doc__
        """ QQuaternion.setZ(float) """
        pass

    def slerp(self, QQuaternion, QQuaternion_1, p_float): # real signature unknown; restored from __doc__
        """ QQuaternion.slerp(QQuaternion, QQuaternion, float) -> QQuaternion """
        return QQuaternion

    def toVector4D(self): # real signature unknown; restored from __doc__
        """ QQuaternion.toVector4D() -> QVector4D """
        return QVector4D

    def vector(self): # real signature unknown; restored from __doc__
        """ QQuaternion.vector() -> QVector3D """
        return QVector3D

    def x(self): # real signature unknown; restored from __doc__
        """ QQuaternion.x() -> float """
        return 0.0

    def y(self): # real signature unknown; restored from __doc__
        """ QQuaternion.y() -> float """
        return 0.0

    def z(self): # real signature unknown; restored from __doc__
        """ QQuaternion.z() -> float """
        return 0.0

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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


