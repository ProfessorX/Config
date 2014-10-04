# encoding: utf-8
# module PyKDE4.kdecore
# from /usr/lib/python3/dist-packages/PyKDE4/kdecore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtNetwork as __PyQt4_QtNetwork


class KSslError(): # skipped bases: <class 'sip.wrapper'>
    # no doc
    def certificate(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CertificateSignatureFailed = 4
    Error = None # (!) real value is ''
    ExpiredCertificate = 6
    HostNameMismatch = 12
    InvalidCertificate = 3
    InvalidCertificateAuthorityCertificate = 2
    InvalidCertificatePurpose = 8
    NoError = 0
    NoPeerCertificate = 11
    PathLengthExceeded = 13
    RejectedCertificate = 9
    RevokedCertificate = 7
    SelfSignedCertificate = 5
    UnknownError = 1
    UntrustedCertificate = 10


