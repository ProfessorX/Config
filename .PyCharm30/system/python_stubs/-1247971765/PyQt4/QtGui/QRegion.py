# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QRegion(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QRegion()
    QRegion(int, int, int, int, QRegion.RegionType type=QRegion.Rectangle)
    QRegion(QRect, QRegion.RegionType type=QRegion.Rectangle)
    QRegion(QPolygon, Qt.FillRule fillRule=Qt.OddEvenFill)
    QRegion(QBitmap)
    QRegion(QRegion)
    QRegion(object)
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QRegion.boundingRect() -> QRect """
        pass

    def contains(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRegion.contains(QPoint) -> bool
        QRegion.contains(QRect) -> bool
        """
        return False

    def eor(self, QRegion): # real signature unknown; restored from __doc__
        """ QRegion.eor(QRegion) -> QRegion """
        return QRegion

    def intersect(self, QRegion): # real signature unknown; restored from __doc__
        """ QRegion.intersect(QRegion) -> QRegion """
        return QRegion

    def intersected(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRegion.intersected(QRegion) -> QRegion
        QRegion.intersected(QRect) -> QRegion
        """
        return QRegion

    def intersects(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRegion.intersects(QRegion) -> bool
        QRegion.intersects(QRect) -> bool
        """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QRegion.isEmpty() -> bool """
        return False

    def numRects(self): # real signature unknown; restored from __doc__
        """ QRegion.numRects() -> int """
        return 0

    def rectCount(self): # real signature unknown; restored from __doc__
        """ QRegion.rectCount() -> int """
        return 0

    def rects(self): # real signature unknown; restored from __doc__
        """ QRegion.rects() -> list-of-QRect """
        pass

    def subtract(self, QRegion): # real signature unknown; restored from __doc__
        """ QRegion.subtract(QRegion) -> QRegion """
        return QRegion

    def subtracted(self, QRegion): # real signature unknown; restored from __doc__
        """ QRegion.subtracted(QRegion) -> QRegion """
        return QRegion

    def swap(self, QRegion): # real signature unknown; restored from __doc__
        """ QRegion.swap(QRegion) """
        pass

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRegion.translate(int, int)
        QRegion.translate(QPoint)
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRegion.translated(int, int) -> QRegion
        QRegion.translated(QPoint) -> QRegion
        """
        return QRegion

    def unite(self, QRegion): # real signature unknown; restored from __doc__
        """ QRegion.unite(QRegion) -> QRegion """
        return QRegion

    def united(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRegion.united(QRegion) -> QRegion
        QRegion.united(QRect) -> QRegion
        """
        return QRegion

    def xored(self, QRegion): # real signature unknown; restored from __doc__
        """ QRegion.xored(QRegion) -> QRegion """
        return QRegion

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
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

    def __ixor__(self, *args, **kwargs): # real signature unknown
        """ Return self^=value. """
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

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Ellipse = 1
    Rectangle = 0
    RegionType = None # (!) real value is ''
    __hash__ = None


