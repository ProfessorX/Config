# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt4/QtNetwork.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QSslError(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QSslError()
    QSslError(QSslError.SslError)
    QSslError(QSslError.SslError, QSslCertificate)
    QSslError(QSslError)
    """
    def certificate(self): # real signature unknown; restored from __doc__
        """ QSslError.certificate() -> QSslCertificate """
        return QSslCertificate

    def error(self): # real signature unknown; restored from __doc__
        """ QSslError.error() -> QSslError.SslError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QSslError.errorString() -> str """
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


    AuthorityIssuerSerialNumberMismatch = 20
    CertificateBlacklisted = 24
    CertificateExpired = 6
    CertificateNotYetValid = 5
    CertificateRejected = 18
    CertificateRevoked = 13
    CertificateSignatureFailed = 4
    CertificateUntrusted = 17
    HostNameMismatch = 22
    InvalidCaCertificate = 14
    InvalidNotAfterField = 8
    InvalidNotBeforeField = 7
    InvalidPurpose = 16
    NoError = 0
    NoPeerCertificate = 21
    NoSslSupport = 23
    PathLengthExceeded = 15
    SelfSignedCertificate = 9
    SelfSignedCertificateInChain = 10
    SslError = None # (!) real value is ''
    SubjectIssuerMismatch = 19
    UnableToDecodeIssuerPublicKey = 3
    UnableToDecryptCertificateSignature = 2
    UnableToGetIssuerCertificate = 1
    UnableToGetLocalIssuerCertificate = 11
    UnableToVerifyFirstCertificate = 12
    UnspecifiedError = -1
    __hash__ = None


