# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from .QInputEvent import QInputEvent

class QKeyEvent(QInputEvent):
    """
    QKeyEvent(QEvent.Type, int, Qt.KeyboardModifiers, str text='', bool autorep=False, int count=1)
    QKeyEvent(QKeyEvent)
    """
    def count(self): # real signature unknown; restored from __doc__
        """ QKeyEvent.count() -> int """
        return 0

    def isAutoRepeat(self): # real signature unknown; restored from __doc__
        """ QKeyEvent.isAutoRepeat() -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ QKeyEvent.key() -> int """
        return 0

    def matches(self, QKeySequence_StandardKey): # real signature unknown; restored from __doc__
        """ QKeyEvent.matches(QKeySequence.StandardKey) -> bool """
        return False

    def modifiers(self): # real signature unknown; restored from __doc__
        """ QKeyEvent.modifiers() -> Qt.KeyboardModifiers """
        pass

    def nativeModifiers(self): # real signature unknown; restored from __doc__
        """ QKeyEvent.nativeModifiers() -> int """
        return 0

    def nativeScanCode(self): # real signature unknown; restored from __doc__
        """ QKeyEvent.nativeScanCode() -> int """
        return 0

    def nativeVirtualKey(self): # real signature unknown; restored from __doc__
        """ QKeyEvent.nativeVirtualKey() -> int """
        return 0

    def text(self): # real signature unknown; restored from __doc__
        """ QKeyEvent.text() -> str """
        return ""

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    __hash__ = None


