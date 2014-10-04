# encoding: utf-8
# module PyKDE4.kdecore
# from /usr/lib/python2.7/dist-packages/PyKDE4/kdecore.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtNetwork as __PyQt4_QtNetwork


class KTcpSocket(__PyQt4_QtCore.QIODevice):
    # no doc
    def abort(self, *args, **kwargs): # real signature unknown
        pass

    def addCaCertificate(self, *args, **kwargs): # real signature unknown
        pass

    def addCaCertificates(self, *args, **kwargs): # real signature unknown
        pass

    def advertisedSslVersion(self, *args, **kwargs): # real signature unknown
        pass

    def atEnd(self, *args, **kwargs): # real signature unknown
        pass

    def bytesAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def bytesToWrite(self, *args, **kwargs): # real signature unknown
        pass

    def caCertificates(self, *args, **kwargs): # real signature unknown
        pass

    def canReadLine(self, *args, **kwargs): # real signature unknown
        pass

    def ciphers(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def connected(self, *args, **kwargs): # real signature unknown
        pass

    def connectToHost(self, *args, **kwargs): # real signature unknown
        pass

    def connectToHostEncrypted(self, *args, **kwargs): # real signature unknown
        pass

    def disconnected(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectFromHost(self, *args, **kwargs): # real signature unknown
        pass

    def encrypted(self, *args, **kwargs): # real signature unknown
        pass

    def encryptedBytesWritten(self, *args, **kwargs): # real signature unknown
        pass

    def encryptionMode(self, *args, **kwargs): # real signature unknown
        pass

    def encryptionModeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def hostFound(self, *args, **kwargs): # real signature unknown
        pass

    def ignoreSslErrors(self, *args, **kwargs): # real signature unknown
        pass

    def isSequential(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def localAddress(self, *args, **kwargs): # real signature unknown
        pass

    def localCertificate(self, *args, **kwargs): # real signature unknown
        pass

    def negotiatedSslVersion(self, *args, **kwargs): # real signature unknown
        pass

    def negotiatedSslVersionName(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, *args, **kwargs): # real signature unknown
        pass

    def peerAddress(self, *args, **kwargs): # real signature unknown
        pass

    def peerCertificateChain(self, *args, **kwargs): # real signature unknown
        pass

    def peerName(self, *args, **kwargs): # real signature unknown
        pass

    def peerPort(self, *args, **kwargs): # real signature unknown
        pass

    def privateKey(self, *args, **kwargs): # real signature unknown
        pass

    def proxy(self, *args, **kwargs): # real signature unknown
        pass

    def proxyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        pass

    def readBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def sessionCipher(self, *args, **kwargs): # real signature unknown
        pass

    def setAdvertisedSslVersion(self, *args, **kwargs): # real signature unknown
        pass

    def setCaCertificates(self, *args, **kwargs): # real signature unknown
        pass

    def setCiphers(self, *args, **kwargs): # real signature unknown
        pass

    def setLocalCertificate(self, *args, **kwargs): # real signature unknown
        pass

    def setPrivateKey(self, *args, **kwargs): # real signature unknown
        pass

    def setProxy(self, *args, **kwargs): # real signature unknown
        pass

    def setReadBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketOption(self, *args, **kwargs): # real signature unknown
        pass

    def setVerificationPeerName(self, *args, **kwargs): # real signature unknown
        pass

    def socketOption(self, *args, **kwargs): # real signature unknown
        pass

    def sslErrors(self, *args, **kwargs): # real signature unknown
        pass

    def startClientEncryption(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def waitForBytesWritten(self, *args, **kwargs): # real signature unknown
        pass

    def waitForConnected(self, *args, **kwargs): # real signature unknown
        pass

    def waitForDisconnected(self, *args, **kwargs): # real signature unknown
        pass

    def waitForEncrypted(self, *args, **kwargs): # real signature unknown
        pass

    def waitForReadyRead(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AnySslVersion = 14
    AutoProxy = 0
    BoundState = 4
    ClosingState = 6
    ConnectedState = 3
    ConnectingState = 2
    ConnectionRefusedError = 1
    EncryptionMode = None # (!) real value is ''
    Error = None # (!) real value is ''
    HostLookupState = 1
    HostNotFoundError = 3
    ListeningState = 5
    ManualProxy = 1
    NetworkError = 7
    ProxyPolicy = None # (!) real value is ''
    RemoteHostClosedError = 2
    SecureProtocols = 32
    SocketAccessError = 4
    SocketResourceError = 5
    SocketTimeoutError = 6
    SslClientMode = 1
    SslServerMode = 2
    SslV2 = 2
    SslV3 = 4
    SslV3_1 = 8
    SslVersion = None # (!) real value is ''
    SslVersions = None # (!) real value is ''
    State = None # (!) real value is ''
    TlsV1 = 8
    TlsV1SslV3 = 16
    UnconnectedState = 0
    UnencryptedMode = 0
    UnknownError = 0
    UnknownSslVersion = 1
    UnsupportedSocketOperationError = 8


