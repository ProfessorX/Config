# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QInputMethodEvent(__PyQt4_QtCore.QEvent):
    """
    QInputMethodEvent()
    QInputMethodEvent(str, list-of-QInputMethodEvent.Attribute)
    QInputMethodEvent(QInputMethodEvent)
    """
    def attributes(self): # real signature unknown; restored from __doc__
        """ QInputMethodEvent.attributes() -> list-of-QInputMethodEvent.Attribute """
        pass

    def commitString(self): # real signature unknown; restored from __doc__
        """ QInputMethodEvent.commitString() -> str """
        return ""

    def preeditString(self): # real signature unknown; restored from __doc__
        """ QInputMethodEvent.preeditString() -> str """
        return ""

    def replacementLength(self): # real signature unknown; restored from __doc__
        """ QInputMethodEvent.replacementLength() -> int """
        return 0

    def replacementStart(self): # real signature unknown; restored from __doc__
        """ QInputMethodEvent.replacementStart() -> int """
        return 0

    def setCommitString(self, p_str, int_from=0, int_length=0): # real signature unknown; restored from __doc__
        """ QInputMethodEvent.setCommitString(str, int from=0, int length=0) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Attribute = None # (!) real value is ''
    AttributeType = None # (!) real value is ''
    Cursor = 1
    Language = 2
    Ruby = 3
    Selection = 4
    TextFormat = 0


