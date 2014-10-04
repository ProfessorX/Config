# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt4/QtNetwork.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QNetworkProxyQuery(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QNetworkProxyQuery()
    QNetworkProxyQuery(QUrl, QNetworkProxyQuery.QueryType type=QNetworkProxyQuery.UrlRequest)
    QNetworkProxyQuery(str, int, str protocolTag='', QNetworkProxyQuery.QueryType type=QNetworkProxyQuery.TcpSocket)
    QNetworkProxyQuery(int, str protocolTag='', QNetworkProxyQuery.QueryType type=QNetworkProxyQuery.TcpServer)
    QNetworkProxyQuery(QNetworkConfiguration, QUrl, QNetworkProxyQuery.QueryType queryType=QNetworkProxyQuery.UrlRequest)
    QNetworkProxyQuery(QNetworkConfiguration, str, int, str protocolTag='', QNetworkProxyQuery.QueryType type=QNetworkProxyQuery.TcpSocket)
    QNetworkProxyQuery(QNetworkConfiguration, int, str protocolTag='', QNetworkProxyQuery.QueryType type=QNetworkProxyQuery.TcpServer)
    QNetworkProxyQuery(QNetworkProxyQuery)
    """
    def localPort(self): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.localPort() -> int """
        return 0

    def networkConfiguration(self): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.networkConfiguration() -> QNetworkConfiguration """
        return QNetworkConfiguration

    def peerHostName(self): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.peerHostName() -> str """
        return ""

    def peerPort(self): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.peerPort() -> int """
        return 0

    def protocolTag(self): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.protocolTag() -> str """
        return ""

    def queryType(self): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.queryType() -> QNetworkProxyQuery.QueryType """
        pass

    def setLocalPort(self, p_int): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.setLocalPort(int) """
        pass

    def setNetworkConfiguration(self, QNetworkConfiguration): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.setNetworkConfiguration(QNetworkConfiguration) """
        pass

    def setPeerHostName(self, p_str): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.setPeerHostName(str) """
        pass

    def setPeerPort(self, p_int): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.setPeerPort(int) """
        pass

    def setProtocolTag(self, p_str): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.setProtocolTag(str) """
        pass

    def setQueryType(self, QNetworkProxyQuery_QueryType): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.setQueryType(QNetworkProxyQuery.QueryType) """
        pass

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.setUrl(QUrl) """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ QNetworkProxyQuery.url() -> QUrl """
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


    QueryType = None # (!) real value is ''
    TcpServer = 100
    TcpSocket = 0
    UdpSocket = 1
    UrlRequest = 101
    __hash__ = None


