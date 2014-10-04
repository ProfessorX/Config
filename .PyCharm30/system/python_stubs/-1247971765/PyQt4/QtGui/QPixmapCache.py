# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QPixmapCache(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QPixmapCache()
    QPixmapCache(QPixmapCache)
    """
    def cacheLimit(self): # real signature unknown; restored from __doc__
        """ QPixmapCache.cacheLimit() -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ QPixmapCache.clear() """
        pass

    def find(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPixmapCache.find(str) -> QPixmap
        QPixmapCache.find(str, QPixmap) -> bool
        QPixmapCache.find(QPixmapCache.Key, QPixmap) -> bool
        """
        return QPixmap or False

    def insert(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPixmapCache.insert(str, QPixmap) -> bool
        QPixmapCache.insert(QPixmap) -> QPixmapCache.Key
        """
        return False

    def remove(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPixmapCache.remove(str)
        QPixmapCache.remove(QPixmapCache.Key)
        """
        pass

    def replace(self, QPixmapCache_Key, QPixmap): # real signature unknown; restored from __doc__
        """ QPixmapCache.replace(QPixmapCache.Key, QPixmap) -> bool """
        return False

    def setCacheLimit(self, p_int): # real signature unknown; restored from __doc__
        """ QPixmapCache.setCacheLimit(int) """
        pass

    def __init__(self, QPixmapCache=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Key = None # (!) real value is ''


