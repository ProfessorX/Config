# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt4/QtNetwork.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QSslConfiguration(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QSslConfiguration()
    QSslConfiguration(QSslConfiguration)
    """
    def caCertificates(self): # real signature unknown; restored from __doc__
        """ QSslConfiguration.caCertificates() -> list-of-QSslCertificate """
        pass

    def ciphers(self): # real signature unknown; restored from __doc__
        """ QSslConfiguration.ciphers() -> list-of-QSslCipher """
        pass

    def defaultConfiguration(self): # real signature unknown; restored from __doc__
        """ QSslConfiguration.defaultConfiguration() -> QSslConfiguration """
        return QSslConfiguration

    def isNull(self): # real signature unknown; restored from __doc__
        """ QSslConfiguration.isNull() -> bool """
        return False

    def localCertificate(self): # real signature unknown; restored from __doc__
        """ QSslConfiguration.localCertificate() -> QSslCertificate """
        return QSslCertificate

    def peerCertificate(self): # real signature unknown; restored from __doc__
        """ QSslConfiguration.peerCertificate() -> QSslCertificate """
        return QSslCertificate

    def peerCertificateChain(self): # real signature unknown; restored from __doc__
        """ QSslConfiguration.peerCertificateChain() -> list-of-QSslCertificate """
        pass

    def peerVerifyDepth(self): # real signature unknown; restored from __doc__
        """ QSslConfiguration.peerVerifyDepth() -> int """
        return 0

    def peerVerifyMode(self): # real signature unknown; restored from __doc__
        """ QSslConfiguration.peerVerifyMode() -> QSslSocket.PeerVerifyMode """
        pass

    def privateKey(self): # real signature unknown; restored from __doc__
        """ QSslConfiguration.privateKey() -> QSslKey """
        return QSslKey

    def protocol(self): # real signature unknown; restored from __doc__
        """ QSslConfiguration.protocol() -> QSsl.SslProtocol """
        pass

    def sessionCipher(self): # real signature unknown; restored from __doc__
        """ QSslConfiguration.sessionCipher() -> QSslCipher """
        return QSslCipher

    def setCaCertificates(self, list_of_QSslCertificate): # real signature unknown; restored from __doc__
        """ QSslConfiguration.setCaCertificates(list-of-QSslCertificate) """
        pass

    def setCiphers(self, list_of_QSslCipher): # real signature unknown; restored from __doc__
        """ QSslConfiguration.setCiphers(list-of-QSslCipher) """
        pass

    def setDefaultConfiguration(self, QSslConfiguration): # real signature unknown; restored from __doc__
        """ QSslConfiguration.setDefaultConfiguration(QSslConfiguration) """
        pass

    def setLocalCertificate(self, QSslCertificate): # real signature unknown; restored from __doc__
        """ QSslConfiguration.setLocalCertificate(QSslCertificate) """
        pass

    def setPeerVerifyDepth(self, p_int): # real signature unknown; restored from __doc__
        """ QSslConfiguration.setPeerVerifyDepth(int) """
        pass

    def setPeerVerifyMode(self, QSslSocket_PeerVerifyMode): # real signature unknown; restored from __doc__
        """ QSslConfiguration.setPeerVerifyMode(QSslSocket.PeerVerifyMode) """
        pass

    def setPrivateKey(self, QSslKey): # real signature unknown; restored from __doc__
        """ QSslConfiguration.setPrivateKey(QSslKey) """
        pass

    def setProtocol(self, QSsl_SslProtocol): # real signature unknown; restored from __doc__
        """ QSslConfiguration.setProtocol(QSsl.SslProtocol) """
        pass

    def setSslOption(self, QSsl_SslOption, bool): # real signature unknown; restored from __doc__
        """ QSslConfiguration.setSslOption(QSsl.SslOption, bool) """
        pass

    def testSslOption(self, QSsl_SslOption): # real signature unknown; restored from __doc__
        """ QSslConfiguration.testSslOption(QSsl.SslOption) -> bool """
        return False

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, QSslConfiguration=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    __hash__ = None


