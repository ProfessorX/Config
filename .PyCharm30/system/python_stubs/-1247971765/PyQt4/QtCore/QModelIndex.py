# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


class QModelIndex(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QModelIndex()
    QModelIndex(QModelIndex)
    QModelIndex(QPersistentModelIndex)
    """
    def child(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QModelIndex.child(int, int) -> QModelIndex """
        return QModelIndex

    def column(self): # real signature unknown; restored from __doc__
        """ QModelIndex.column() -> int """
        return 0

    def data(self, int_role=None): # real signature unknown; restored from __doc__
        """ QModelIndex.data(int role=Qt.DisplayRole) -> object """
        return object()

    def flags(self): # real signature unknown; restored from __doc__
        """ QModelIndex.flags() -> Qt.ItemFlags """
        pass

    def internalId(self): # real signature unknown; restored from __doc__
        """ QModelIndex.internalId() -> int """
        return 0

    def internalPointer(self): # real signature unknown; restored from __doc__
        """ QModelIndex.internalPointer() -> object """
        return object()

    def isValid(self): # real signature unknown; restored from __doc__
        """ QModelIndex.isValid() -> bool """
        return False

    def model(self): # real signature unknown; restored from __doc__
        """ QModelIndex.model() -> QAbstractItemModel """
        return QAbstractItemModel

    def parent(self): # real signature unknown; restored from __doc__
        """ QModelIndex.parent() -> QModelIndex """
        return QModelIndex

    def row(self): # real signature unknown; restored from __doc__
        """ QModelIndex.row() -> int """
        return 0

    def sibling(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QModelIndex.sibling(int, int) -> QModelIndex """
        return QModelIndex

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



