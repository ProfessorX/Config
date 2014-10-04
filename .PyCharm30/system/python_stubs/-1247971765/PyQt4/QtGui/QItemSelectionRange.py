# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QItemSelectionRange(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QItemSelectionRange()
    QItemSelectionRange(QItemSelectionRange)
    QItemSelectionRange(QModelIndex, QModelIndex)
    QItemSelectionRange(QModelIndex)
    """
    def bottom(self): # real signature unknown; restored from __doc__
        """ QItemSelectionRange.bottom() -> int """
        return 0

    def bottomRight(self): # real signature unknown; restored from __doc__
        """ QItemSelectionRange.bottomRight() -> QModelIndex """
        pass

    def contains(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QItemSelectionRange.contains(QModelIndex) -> bool
        QItemSelectionRange.contains(int, int, QModelIndex) -> bool
        """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ QItemSelectionRange.height() -> int """
        return 0

    def indexes(self): # real signature unknown; restored from __doc__
        """ QItemSelectionRange.indexes() -> list-of-QModelIndex """
        pass

    def intersect(self, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ QItemSelectionRange.intersect(QItemSelectionRange) -> QItemSelectionRange """
        return QItemSelectionRange

    def intersected(self, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ QItemSelectionRange.intersected(QItemSelectionRange) -> QItemSelectionRange """
        return QItemSelectionRange

    def intersects(self, QItemSelectionRange): # real signature unknown; restored from __doc__
        """ QItemSelectionRange.intersects(QItemSelectionRange) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QItemSelectionRange.isEmpty() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QItemSelectionRange.isValid() -> bool """
        return False

    def left(self): # real signature unknown; restored from __doc__
        """ QItemSelectionRange.left() -> int """
        return 0

    def model(self): # real signature unknown; restored from __doc__
        """ QItemSelectionRange.model() -> QAbstractItemModel """
        pass

    def parent(self): # real signature unknown; restored from __doc__
        """ QItemSelectionRange.parent() -> QModelIndex """
        pass

    def right(self): # real signature unknown; restored from __doc__
        """ QItemSelectionRange.right() -> int """
        return 0

    def top(self): # real signature unknown; restored from __doc__
        """ QItemSelectionRange.top() -> int """
        return 0

    def topLeft(self): # real signature unknown; restored from __doc__
        """ QItemSelectionRange.topLeft() -> QModelIndex """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ QItemSelectionRange.width() -> int """
        return 0

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



