# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QPolygon(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QPolygon()
    QPolygon(QPolygon)
    QPolygon(list-of-QPoint)
    QPolygon(QRect, bool closed=False)
    QPolygon(int)
    QPolygon(list-of-int)
    QPolygon(object)
    """
    def append(self, QPoint): # real signature unknown; restored from __doc__
        """ QPolygon.append(QPoint) """
        pass

    def at(self, p_int): # real signature unknown; restored from __doc__
        """ QPolygon.at(int) -> QPoint """
        pass

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QPolygon.boundingRect() -> QRect """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QPolygon.clear() """
        pass

    def contains(self, QPoint): # real signature unknown; restored from __doc__
        """ QPolygon.contains(QPoint) -> bool """
        return False

    def containsPoint(self, QPoint, Qt_FillRule): # real signature unknown; restored from __doc__
        """ QPolygon.containsPoint(QPoint, Qt.FillRule) -> bool """
        return False

    def count(self, QPoint=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPolygon.count(QPoint) -> int
        QPolygon.count() -> int
        """
        return 0

    def data(self): # real signature unknown; restored from __doc__
        """ QPolygon.data() -> sip.voidptr """
        pass

    def fill(self, QPoint, int_size=-1): # real signature unknown; restored from __doc__
        """ QPolygon.fill(QPoint, int size=-1) """
        pass

    def first(self): # real signature unknown; restored from __doc__
        """ QPolygon.first() -> QPoint """
        pass

    def indexOf(self, QPoint, int_from=0): # real signature unknown; restored from __doc__
        """ QPolygon.indexOf(QPoint, int from=0) -> int """
        return 0

    def insert(self, p_int, QPoint): # real signature unknown; restored from __doc__
        """ QPolygon.insert(int, QPoint) """
        pass

    def intersected(self, QPolygon): # real signature unknown; restored from __doc__
        """ QPolygon.intersected(QPolygon) -> QPolygon """
        return QPolygon

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QPolygon.isEmpty() -> bool """
        return False

    def last(self): # real signature unknown; restored from __doc__
        """ QPolygon.last() -> QPoint """
        pass

    def lastIndexOf(self, QPoint, int_from=-1): # real signature unknown; restored from __doc__
        """ QPolygon.lastIndexOf(QPoint, int from=-1) -> int """
        return 0

    def mid(self, p_int, int_length=-1): # real signature unknown; restored from __doc__
        """ QPolygon.mid(int, int length=-1) -> QPolygon """
        return QPolygon

    def point(self, p_int): # real signature unknown; restored from __doc__
        """ QPolygon.point(int) -> QPoint """
        pass

    def prepend(self, QPoint): # real signature unknown; restored from __doc__
        """ QPolygon.prepend(QPoint) """
        pass

    def putPoints(self, p_int, p_int_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPolygon.putPoints(int, int, int, ...)
        QPolygon.putPoints(int, int, QPolygon, int from=0)
        """
        pass

    def remove(self, p_int, p_int_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPolygon.remove(int)
        QPolygon.remove(int, int)
        """
        pass

    def replace(self, p_int, QPoint): # real signature unknown; restored from __doc__
        """ QPolygon.replace(int, QPoint) """
        pass

    def setPoint(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPolygon.setPoint(int, QPoint)
        QPolygon.setPoint(int, int, int)
        """
        pass

    def setPoints(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPolygon.setPoints(list-of-int)
        QPolygon.setPoints(int, int, ...)
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QPolygon.size() -> int """
        return 0

    def subtracted(self, QPolygon): # real signature unknown; restored from __doc__
        """ QPolygon.subtracted(QPolygon) -> QPolygon """
        return QPolygon

    def swap(self, QPolygon): # real signature unknown; restored from __doc__
        """ QPolygon.swap(QPolygon) """
        pass

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPolygon.translate(int, int)
        QPolygon.translate(QPoint)
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPolygon.translated(int, int) -> QPolygon
        QPolygon.translated(QPoint) -> QPolygon
        """
        return QPolygon

    def united(self, QPolygon): # real signature unknown; restored from __doc__
        """ QPolygon.united(QPolygon) -> QPolygon """
        return QPolygon

    def value(self, p_int, QPoint=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPolygon.value(int) -> QPoint
        QPolygon.value(int, QPoint) -> QPoint
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
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
        """ Implement self+=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
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

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


