# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt4/QtNetwork.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QHttp(__PyQt4_QtCore.QObject):
    """
    QHttp(QObject parent=None)
    QHttp(str, int port=80, QObject parent=None)
    QHttp(str, QHttp.ConnectionMode, int port=0, QObject parent=None)
    """
    def abort(self): # real signature unknown; restored from __doc__
        """ QHttp.abort() """
        pass

    def authenticationRequired(self, *args, **kwargs): # real signature unknown
        """ QHttp.authenticationRequired[str, int, QAuthenticator] [signal] """
        pass

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ QHttp.bytesAvailable() -> int """
        return 0

    def clearPendingRequests(self): # real signature unknown; restored from __doc__
        """ QHttp.clearPendingRequests() """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ QHttp.close() -> int """
        return 0

    def currentDestinationDevice(self): # real signature unknown; restored from __doc__
        """ QHttp.currentDestinationDevice() -> QIODevice """
        pass

    def currentId(self): # real signature unknown; restored from __doc__
        """ QHttp.currentId() -> int """
        return 0

    def currentRequest(self): # real signature unknown; restored from __doc__
        """ QHttp.currentRequest() -> QHttpRequestHeader """
        return QHttpRequestHeader

    def currentSourceDevice(self): # real signature unknown; restored from __doc__
        """ QHttp.currentSourceDevice() -> QIODevice """
        pass

    def dataReadProgress(self, *args, **kwargs): # real signature unknown
        """ QHttp.dataReadProgress[int, int] [signal] """
        pass

    def dataSendProgress(self, *args, **kwargs): # real signature unknown
        """ QHttp.dataSendProgress[int, int] [signal] """
        pass

    def done(self, *args, **kwargs): # real signature unknown
        """ QHttp.done[bool] [signal] """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ QHttp.error() -> QHttp.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QHttp.errorString() -> str """
        return ""

    def get(self, p_str, QIODevice_to=None): # real signature unknown; restored from __doc__
        """ QHttp.get(str, QIODevice to=None) -> int """
        return 0

    def hasPendingRequests(self): # real signature unknown; restored from __doc__
        """ QHttp.hasPendingRequests() -> bool """
        return False

    def head(self, p_str): # real signature unknown; restored from __doc__
        """ QHttp.head(str) -> int """
        return 0

    def ignoreSslErrors(self): # real signature unknown; restored from __doc__
        """ QHttp.ignoreSslErrors() """
        pass

    def lastResponse(self): # real signature unknown; restored from __doc__
        """ QHttp.lastResponse() -> QHttpResponseHeader """
        return QHttpResponseHeader

    def post(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHttp.post(str, QIODevice, QIODevice to=None) -> int
        QHttp.post(str, QByteArray, QIODevice to=None) -> int
        """
        return 0

    def proxyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        """ QHttp.proxyAuthenticationRequired[QNetworkProxy, QAuthenticator] [signal] """
        pass

    def read(self, p_int): # real signature unknown; restored from __doc__
        """ QHttp.read(int) -> bytes """
        return b""

    def readAll(self): # real signature unknown; restored from __doc__
        """ QHttp.readAll() -> QByteArray """
        pass

    def readyRead(self, *args, **kwargs): # real signature unknown
        """ QHttp.readyRead[QHttpResponseHeader] [signal] """
        pass

    def request(self, QHttpRequestHeader, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHttp.request(QHttpRequestHeader, QIODevice data=None, QIODevice to=None) -> int
        QHttp.request(QHttpRequestHeader, QByteArray, QIODevice to=None) -> int
        """
        return 0

    def requestFinished(self, *args, **kwargs): # real signature unknown
        """ QHttp.requestFinished[int, bool] [signal] """
        pass

    def requestStarted(self, *args, **kwargs): # real signature unknown
        """ QHttp.requestStarted[int] [signal] """
        pass

    def responseHeaderReceived(self, *args, **kwargs): # real signature unknown
        """ QHttp.responseHeaderReceived[QHttpResponseHeader] [signal] """
        pass

    def setHost(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHttp.setHost(str, int port=80) -> int
        QHttp.setHost(str, QHttp.ConnectionMode, int port=0) -> int
        """
        return 0

    def setProxy(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHttp.setProxy(str, int, str user='', str password='') -> int
        QHttp.setProxy(QNetworkProxy) -> int
        """
        return 0

    def setSocket(self, QTcpSocket): # real signature unknown; restored from __doc__
        """ QHttp.setSocket(QTcpSocket) -> int """
        return 0

    def setUser(self, p_str, str_password=''): # real signature unknown; restored from __doc__
        """ QHttp.setUser(str, str password='') -> int """
        return 0

    def sslErrors(self, *args, **kwargs): # real signature unknown
        """ QHttp.sslErrors[list-of-QSslError] [signal] """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ QHttp.state() -> QHttp.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ QHttp.stateChanged[int] [signal] """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Aborted = 7
    AuthenticationRequiredError = 8
    Closing = 6
    Connected = 5
    Connecting = 2
    ConnectionMode = None # (!) real value is ''
    ConnectionModeHttp = 0
    ConnectionModeHttps = 1
    ConnectionRefused = 3
    Error = None # (!) real value is ''
    HostLookup = 1
    HostNotFound = 2
    InvalidResponseHeader = 5
    NoError = 0
    ProxyAuthenticationRequiredError = 9
    Reading = 4
    Sending = 3
    State = None # (!) real value is ''
    Unconnected = 0
    UnexpectedClose = 4
    UnknownError = 1
    WrongContentLength = 6


