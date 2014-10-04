# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


class QRect(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QRect()
    QRect(int, int, int, int)
    QRect(QPoint, QPoint)
    QRect(QPoint, QSize)
    QRect(QRect)
    """
    def adjust(self, p_int, p_int_1, p_int_2, p_int_3): # real signature unknown; restored from __doc__
        """ QRect.adjust(int, int, int, int) """
        pass

    def adjusted(self, p_int, p_int_1, p_int_2, p_int_3): # real signature unknown; restored from __doc__
        """ QRect.adjusted(int, int, int, int) -> QRect """
        return QRect

    def bottom(self): # real signature unknown; restored from __doc__
        """ QRect.bottom() -> int """
        return 0

    def bottomLeft(self): # real signature unknown; restored from __doc__
        """ QRect.bottomLeft() -> QPoint """
        return QPoint

    def bottomRight(self): # real signature unknown; restored from __doc__
        """ QRect.bottomRight() -> QPoint """
        return QPoint

    def center(self): # real signature unknown; restored from __doc__
        """ QRect.center() -> QPoint """
        return QPoint

    def contains(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRect.contains(QPoint, bool proper=False) -> bool
        QRect.contains(QRect, bool proper=False) -> bool
        QRect.contains(int, int, bool) -> bool
        QRect.contains(int, int) -> bool
        """
        return False

    def getCoords(self): # real signature unknown; restored from __doc__
        """ QRect.getCoords() -> (int, int, int, int) """
        pass

    def getRect(self): # real signature unknown; restored from __doc__
        """ QRect.getRect() -> (int, int, int, int) """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ QRect.height() -> int """
        return 0

    def intersect(self, QRect): # real signature unknown; restored from __doc__
        """ QRect.intersect(QRect) -> QRect """
        return QRect

    def intersected(self, QRect): # real signature unknown; restored from __doc__
        """ QRect.intersected(QRect) -> QRect """
        return QRect

    def intersects(self, QRect): # real signature unknown; restored from __doc__
        """ QRect.intersects(QRect) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QRect.isEmpty() -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QRect.isNull() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QRect.isValid() -> bool """
        return False

    def left(self): # real signature unknown; restored from __doc__
        """ QRect.left() -> int """
        return 0

    def moveBottom(self, p_int): # real signature unknown; restored from __doc__
        """ QRect.moveBottom(int) """
        pass

    def moveBottomLeft(self, QPoint): # real signature unknown; restored from __doc__
        """ QRect.moveBottomLeft(QPoint) """
        pass

    def moveBottomRight(self, QPoint): # real signature unknown; restored from __doc__
        """ QRect.moveBottomRight(QPoint) """
        pass

    def moveCenter(self, QPoint): # real signature unknown; restored from __doc__
        """ QRect.moveCenter(QPoint) """
        pass

    def moveLeft(self, p_int): # real signature unknown; restored from __doc__
        """ QRect.moveLeft(int) """
        pass

    def moveRight(self, p_int): # real signature unknown; restored from __doc__
        """ QRect.moveRight(int) """
        pass

    def moveTo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRect.moveTo(int, int)
        QRect.moveTo(QPoint)
        """
        pass

    def moveTop(self, p_int): # real signature unknown; restored from __doc__
        """ QRect.moveTop(int) """
        pass

    def moveTopLeft(self, QPoint): # real signature unknown; restored from __doc__
        """ QRect.moveTopLeft(QPoint) """
        pass

    def moveTopRight(self, QPoint): # real signature unknown; restored from __doc__
        """ QRect.moveTopRight(QPoint) """
        pass

    def normalized(self): # real signature unknown; restored from __doc__
        """ QRect.normalized() -> QRect """
        return QRect

    def right(self): # real signature unknown; restored from __doc__
        """ QRect.right() -> int """
        return 0

    def setBottom(self, p_int): # real signature unknown; restored from __doc__
        """ QRect.setBottom(int) """
        pass

    def setBottomLeft(self, QPoint): # real signature unknown; restored from __doc__
        """ QRect.setBottomLeft(QPoint) """
        pass

    def setBottomRight(self, QPoint): # real signature unknown; restored from __doc__
        """ QRect.setBottomRight(QPoint) """
        pass

    def setCoords(self, p_int, p_int_1, p_int_2, p_int_3): # real signature unknown; restored from __doc__
        """ QRect.setCoords(int, int, int, int) """
        pass

    def setHeight(self, p_int): # real signature unknown; restored from __doc__
        """ QRect.setHeight(int) """
        pass

    def setLeft(self, p_int): # real signature unknown; restored from __doc__
        """ QRect.setLeft(int) """
        pass

    def setRect(self, p_int, p_int_1, p_int_2, p_int_3): # real signature unknown; restored from __doc__
        """ QRect.setRect(int, int, int, int) """
        pass

    def setRight(self, p_int): # real signature unknown; restored from __doc__
        """ QRect.setRight(int) """
        pass

    def setSize(self, QSize): # real signature unknown; restored from __doc__
        """ QRect.setSize(QSize) """
        pass

    def setTop(self, p_int): # real signature unknown; restored from __doc__
        """ QRect.setTop(int) """
        pass

    def setTopLeft(self, QPoint): # real signature unknown; restored from __doc__
        """ QRect.setTopLeft(QPoint) """
        pass

    def setTopRight(self, QPoint): # real signature unknown; restored from __doc__
        """ QRect.setTopRight(QPoint) """
        pass

    def setWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QRect.setWidth(int) """
        pass

    def setX(self, p_int): # real signature unknown; restored from __doc__
        """ QRect.setX(int) """
        pass

    def setY(self, p_int): # real signature unknown; restored from __doc__
        """ QRect.setY(int) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QRect.size() -> QSize """
        return QSize

    def top(self): # real signature unknown; restored from __doc__
        """ QRect.top() -> int """
        return 0

    def topLeft(self): # real signature unknown; restored from __doc__
        """ QRect.topLeft() -> QPoint """
        return QPoint

    def topRight(self): # real signature unknown; restored from __doc__
        """ QRect.topRight() -> QPoint """
        return QPoint

    def translate(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRect.translate(int, int)
        QRect.translate(QPoint)
        """
        pass

    def translated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRect.translated(int, int) -> QRect
        QRect.translated(QPoint) -> QRect
        """
        return QRect

    def unite(self, QRect): # real signature unknown; restored from __doc__
        """ QRect.unite(QRect) -> QRect """
        return QRect

    def united(self, QRect): # real signature unknown; restored from __doc__
        """ QRect.united(QRect) -> QRect """
        return QRect

    def width(self): # real signature unknown; restored from __doc__
        """ QRect.width() -> int """
        return 0

    def x(self): # real signature unknown; restored from __doc__
        """ QRect.x() -> int """
        return 0

    def y(self): # real signature unknown; restored from __doc__
        """ QRect.y() -> int """
        return 0

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

    def __iand__(self, *args, **kwargs): # real signature unknown
        """ Return self&=value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __ior__(self, *args, **kwargs): # real signature unknown
        """ Return self|=value. """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


