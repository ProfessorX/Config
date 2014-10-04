# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt4/QtNetwork.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QSslCertificate(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QSslCertificate(QIODevice, QSsl.EncodingFormat format=QSsl.Pem)
    QSslCertificate(QByteArray data=QByteArray(), QSsl.EncodingFormat format=QSsl.Pem)
    QSslCertificate(QSslCertificate)
    """
    def alternateSubjectNames(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.alternateSubjectNames() -> dict-of-QSsl.AlternateNameEntryType-list-of-str """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.clear() """
        pass

    def digest(self, QCryptographicHash_Algorithm_algorithm=None): # real signature unknown; restored from __doc__
        """ QSslCertificate.digest(QCryptographicHash.Algorithm algorithm=QCryptographicHash.Md5) -> QByteArray """
        pass

    def effectiveDate(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.effectiveDate() -> QDateTime """
        pass

    def expiryDate(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.expiryDate() -> QDateTime """
        pass

    def fromData(self, QByteArray, QSsl_EncodingFormat_format=None): # real signature unknown; restored from __doc__
        """ QSslCertificate.fromData(QByteArray, QSsl.EncodingFormat format=QSsl.Pem) -> list-of-QSslCertificate """
        pass

    def fromDevice(self, QIODevice, QSsl_EncodingFormat_format=None): # real signature unknown; restored from __doc__
        """ QSslCertificate.fromDevice(QIODevice, QSsl.EncodingFormat format=QSsl.Pem) -> list-of-QSslCertificate """
        pass

    def fromPath(self, p_str, QSsl_EncodingFormat_format=None, QRegExp_PatternSyntax_syntax=None): # real signature unknown; restored from __doc__
        """ QSslCertificate.fromPath(str, QSsl.EncodingFormat format=QSsl.Pem, QRegExp.PatternSyntax syntax=QRegExp.FixedString) -> list-of-QSslCertificate """
        pass

    def handle(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.handle() -> int """
        return 0

    def isNull(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.isNull() -> bool """
        return False

    def issuerInfo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSslCertificate.issuerInfo(QSslCertificate.SubjectInfo) -> str
        QSslCertificate.issuerInfo(QByteArray) -> str
        """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.isValid() -> bool """
        return False

    def publicKey(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.publicKey() -> QSslKey """
        return QSslKey

    def serialNumber(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.serialNumber() -> QByteArray """
        pass

    def subjectInfo(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSslCertificate.subjectInfo(QSslCertificate.SubjectInfo) -> str
        QSslCertificate.subjectInfo(QByteArray) -> str
        """
        return ""

    def toDer(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.toDer() -> QByteArray """
        pass

    def toPem(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.toPem() -> QByteArray """
        pass

    def version(self): # real signature unknown; restored from __doc__
        """ QSslCertificate.version() -> QByteArray """
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


    CommonName = 1
    CountryName = 4
    LocalityName = 2
    Organization = 0
    OrganizationalUnitName = 3
    StateOrProvinceName = 5
    SubjectInfo = None # (!) real value is ''
    __hash__ = None


