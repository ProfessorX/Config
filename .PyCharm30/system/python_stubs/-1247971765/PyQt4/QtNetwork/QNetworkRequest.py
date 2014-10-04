# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt4/QtNetwork.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QNetworkRequest(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QNetworkRequest(QUrl url=QUrl())
    QNetworkRequest(QNetworkRequest)
    """
    def attribute(self, QNetworkRequest_Attribute, object_defaultValue=None): # real signature unknown; restored from __doc__
        """ QNetworkRequest.attribute(QNetworkRequest.Attribute, object defaultValue=None) -> object """
        return object()

    def hasRawHeader(self, QByteArray): # real signature unknown; restored from __doc__
        """ QNetworkRequest.hasRawHeader(QByteArray) -> bool """
        return False

    def header(self, QNetworkRequest_KnownHeaders): # real signature unknown; restored from __doc__
        """ QNetworkRequest.header(QNetworkRequest.KnownHeaders) -> object """
        return object()

    def originatingObject(self): # real signature unknown; restored from __doc__
        """ QNetworkRequest.originatingObject() -> QObject """
        pass

    def priority(self): # real signature unknown; restored from __doc__
        """ QNetworkRequest.priority() -> QNetworkRequest.Priority """
        pass

    def rawHeader(self, QByteArray): # real signature unknown; restored from __doc__
        """ QNetworkRequest.rawHeader(QByteArray) -> QByteArray """
        pass

    def rawHeaderList(self): # real signature unknown; restored from __doc__
        """ QNetworkRequest.rawHeaderList() -> list-of-QByteArray """
        pass

    def setAttribute(self, QNetworkRequest_Attribute, p_object): # real signature unknown; restored from __doc__
        """ QNetworkRequest.setAttribute(QNetworkRequest.Attribute, object) """
        pass

    def setHeader(self, QNetworkRequest_KnownHeaders, p_object): # real signature unknown; restored from __doc__
        """ QNetworkRequest.setHeader(QNetworkRequest.KnownHeaders, object) """
        pass

    def setOriginatingObject(self, QObject): # real signature unknown; restored from __doc__
        """ QNetworkRequest.setOriginatingObject(QObject) """
        pass

    def setPriority(self, QNetworkRequest_Priority): # real signature unknown; restored from __doc__
        """ QNetworkRequest.setPriority(QNetworkRequest.Priority) """
        pass

    def setRawHeader(self, QByteArray, QByteArray_1): # real signature unknown; restored from __doc__
        """ QNetworkRequest.setRawHeader(QByteArray, QByteArray) """
        pass

    def setSslConfiguration(self, QSslConfiguration): # real signature unknown; restored from __doc__
        """ QNetworkRequest.setSslConfiguration(QSslConfiguration) """
        pass

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ QNetworkRequest.setUrl(QUrl) """
        pass

    def sslConfiguration(self): # real signature unknown; restored from __doc__
        """ QNetworkRequest.sslConfiguration() -> QSslConfiguration """
        return QSslConfiguration

    def url(self): # real signature unknown; restored from __doc__
        """ QNetworkRequest.url() -> QUrl """
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


    AlwaysCache = 3
    AlwaysNetwork = 0
    Attribute = None # (!) real value is ''
    AuthenticationReuseAttribute = 12
    Automatic = 0
    CacheLoadControl = None # (!) real value is ''
    CacheLoadControlAttribute = 4
    CacheSaveControlAttribute = 5
    ConnectionEncryptedAttribute = 3
    ContentDispositionHeader = 6
    ContentLengthHeader = 1
    ContentTypeHeader = 0
    CookieHeader = 4
    CookieLoadControlAttribute = 11
    CookieSaveControlAttribute = 13
    CustomVerbAttribute = 10
    DoNotBufferUploadDataAttribute = 7
    HighPriority = 1
    HttpPipeliningAllowedAttribute = 8
    HttpPipeliningWasUsedAttribute = 9
    HttpReasonPhraseAttribute = 1
    HttpStatusCodeAttribute = 0
    KnownHeaders = None # (!) real value is ''
    LastModifiedHeader = 3
    LoadControl = None # (!) real value is ''
    LocationHeader = 2
    LowPriority = 5
    Manual = 1
    NormalPriority = 3
    PreferCache = 2
    PreferNetwork = 1
    Priority = None # (!) real value is ''
    RedirectionTargetAttribute = 2
    SetCookieHeader = 5
    SourceIsFromCacheAttribute = 6
    User = 1000
    UserMax = 32767
    __hash__ = None


