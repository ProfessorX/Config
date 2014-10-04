# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt4/QtNetwork.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QNetworkProxy(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QNetworkProxy()
    QNetworkProxy(QNetworkProxy.ProxyType, str hostName='', int port=0, str user='', str password='')
    QNetworkProxy(QNetworkProxy)
    """
    def applicationProxy(self): # real signature unknown; restored from __doc__
        """ QNetworkProxy.applicationProxy() -> QNetworkProxy """
        return QNetworkProxy

    def capabilities(self): # real signature unknown; restored from __doc__
        """ QNetworkProxy.capabilities() -> QNetworkProxy.Capabilities """
        pass

    def hostName(self): # real signature unknown; restored from __doc__
        """ QNetworkProxy.hostName() -> str """
        return ""

    def isCachingProxy(self): # real signature unknown; restored from __doc__
        """ QNetworkProxy.isCachingProxy() -> bool """
        return False

    def isTransparentProxy(self): # real signature unknown; restored from __doc__
        """ QNetworkProxy.isTransparentProxy() -> bool """
        return False

    def password(self): # real signature unknown; restored from __doc__
        """ QNetworkProxy.password() -> str """
        return ""

    def port(self): # real signature unknown; restored from __doc__
        """ QNetworkProxy.port() -> int """
        return 0

    def setApplicationProxy(self, QNetworkProxy): # real signature unknown; restored from __doc__
        """ QNetworkProxy.setApplicationProxy(QNetworkProxy) """
        pass

    def setCapabilities(self, QNetworkProxy_Capabilities): # real signature unknown; restored from __doc__
        """ QNetworkProxy.setCapabilities(QNetworkProxy.Capabilities) """
        pass

    def setHostName(self, p_str): # real signature unknown; restored from __doc__
        """ QNetworkProxy.setHostName(str) """
        pass

    def setPassword(self, p_str): # real signature unknown; restored from __doc__
        """ QNetworkProxy.setPassword(str) """
        pass

    def setPort(self, p_int): # real signature unknown; restored from __doc__
        """ QNetworkProxy.setPort(int) """
        pass

    def setType(self, QNetworkProxy_ProxyType): # real signature unknown; restored from __doc__
        """ QNetworkProxy.setType(QNetworkProxy.ProxyType) """
        pass

    def setUser(self, p_str): # real signature unknown; restored from __doc__
        """ QNetworkProxy.setUser(str) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ QNetworkProxy.type() -> QNetworkProxy.ProxyType """
        pass

    def user(self): # real signature unknown; restored from __doc__
        """ QNetworkProxy.user() -> str """
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


    CachingCapability = 8
    Capabilities = None # (!) real value is ''
    Capability = None # (!) real value is ''
    DefaultProxy = 0
    FtpCachingProxy = 5
    HostNameLookupCapability = 16
    HttpCachingProxy = 4
    HttpProxy = 3
    ListeningCapability = 2
    NoProxy = 2
    ProxyType = None # (!) real value is ''
    Socks5Proxy = 1
    TunnelingCapability = 1
    UdpTunnelingCapability = 4
    __hash__ = None


