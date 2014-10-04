# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt4/QtNetwork.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QHostInfo(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QHostInfo(int id=-1)
    QHostInfo(QHostInfo)
    """
    def abortHostLookup(self, p_int): # real signature unknown; restored from __doc__
        """ QHostInfo.abortHostLookup(int) """
        pass

    def addresses(self): # real signature unknown; restored from __doc__
        """ QHostInfo.addresses() -> list-of-QHostAddress """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ QHostInfo.error() -> QHostInfo.HostInfoError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QHostInfo.errorString() -> str """
        return ""

    def fromName(self, p_str): # real signature unknown; restored from __doc__
        """ QHostInfo.fromName(str) -> QHostInfo """
        return QHostInfo

    def hostName(self): # real signature unknown; restored from __doc__
        """ QHostInfo.hostName() -> str """
        return ""

    def localDomainName(self): # real signature unknown; restored from __doc__
        """ QHostInfo.localDomainName() -> str """
        return ""

    def localHostName(self): # real signature unknown; restored from __doc__
        """ QHostInfo.localHostName() -> str """
        return ""

    def lookupHost(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHostInfo.lookupHost(str, QObject, SLOT()) -> int
        QHostInfo.lookupHost(str, callable) -> int
        """
        return 0

    def lookupId(self): # real signature unknown; restored from __doc__
        """ QHostInfo.lookupId() -> int """
        return 0

    def setAddresses(self, list_of_QHostAddress): # real signature unknown; restored from __doc__
        """ QHostInfo.setAddresses(list-of-QHostAddress) """
        pass

    def setError(self, QHostInfo_HostInfoError): # real signature unknown; restored from __doc__
        """ QHostInfo.setError(QHostInfo.HostInfoError) """
        pass

    def setErrorString(self, p_str): # real signature unknown; restored from __doc__
        """ QHostInfo.setErrorString(str) """
        pass

    def setHostName(self, p_str): # real signature unknown; restored from __doc__
        """ QHostInfo.setHostName(str) """
        pass

    def setLookupId(self, p_int): # real signature unknown; restored from __doc__
        """ QHostInfo.setLookupId(int) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    HostInfoError = None # (!) real value is ''
    HostNotFound = 1
    NoError = 0
    UnknownError = 2


