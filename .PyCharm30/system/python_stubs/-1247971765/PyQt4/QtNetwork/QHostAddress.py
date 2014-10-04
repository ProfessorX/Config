# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt4/QtNetwork.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QHostAddress(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QHostAddress()
    QHostAddress(QHostAddress.SpecialAddress)
    QHostAddress(int)
    QHostAddress(str)
    QHostAddress(16-tuple-of-int)
    QHostAddress(QHostAddress)
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ QHostAddress.clear() """
        pass

    def isInSubnet(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHostAddress.isInSubnet(QHostAddress, int) -> bool
        QHostAddress.isInSubnet(tuple-of-QHostAddress-int) -> bool
        """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QHostAddress.isNull() -> bool """
        return False

    def parseSubnet(self, p_str): # real signature unknown; restored from __doc__
        """ QHostAddress.parseSubnet(str) -> tuple-of-QHostAddress-int """
        pass

    def protocol(self): # real signature unknown; restored from __doc__
        """ QHostAddress.protocol() -> QAbstractSocket.NetworkLayerProtocol """
        pass

    def scopeId(self): # real signature unknown; restored from __doc__
        """ QHostAddress.scopeId() -> str """
        return ""

    def setAddress(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHostAddress.setAddress(int)
        QHostAddress.setAddress(str) -> bool
        QHostAddress.setAddress(16-tuple-of-int)
        """
        return False

    def setScopeId(self, p_str): # real signature unknown; restored from __doc__
        """ QHostAddress.setScopeId(str) """
        pass

    def toIPv4Address(self): # real signature unknown; restored from __doc__
        """ QHostAddress.toIPv4Address() -> int """
        return 0

    def toIPv6Address(self): # real signature unknown; restored from __doc__
        """ QHostAddress.toIPv6Address() -> 16-tuple-of-int """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ QHostAddress.toString() -> str """
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


    Any = 4
    AnyIPv6 = 5
    Broadcast = 1
    LocalHost = 2
    LocalHostIPv6 = 3
    Null = 0
    SpecialAddress = None # (!) real value is ''


