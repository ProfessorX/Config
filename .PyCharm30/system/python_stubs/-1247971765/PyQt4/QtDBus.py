# encoding: utf-8
# module PyQt4.QtDBus
# from /usr/lib/python3/dist-packages/PyQt4/QtDBus.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


# no functions
# classes

class QDBus(): # skipped bases: <class 'sip.wrapper'>
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AutoDetect = 3
    Block = 1
    BlockWithGui = 2
    CallMode = None # (!) real value is ''
    NoBlock = 0


class QDBusAbstractAdaptor(__PyQt4_QtCore.QObject):
    """ QDBusAbstractAdaptor(QObject) """
    def autoRelaySignals(self): # real signature unknown; restored from __doc__
        """ QDBusAbstractAdaptor.autoRelaySignals() -> bool """
        return False

    def setAutoRelaySignals(self, bool): # real signature unknown; restored from __doc__
        """ QDBusAbstractAdaptor.setAutoRelaySignals(bool) """
        pass

    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass


class QDBusAbstractInterface(__PyQt4_QtCore.QObject):
    """ QDBusAbstractInterface(str, str, str, QDBusConnection, QObject) """
    def asyncCall(self, p_str, object_arg1=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QDBusAbstractInterface.asyncCall(str, object arg1=QVariant(), object arg2=QVariant(), object arg3=QVariant(), object arg4=QVariant(), object arg5=QVariant(), object arg6=QVariant(), object arg7=QVariant(), object arg8=QVariant()) -> QDBusPendingCall """
        pass

    def asyncCallWithArgumentList(self, p_str, list_of_QVariant): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.asyncCallWithArgumentList(str, list-of-QVariant) -> QDBusPendingCall """
        return QDBusPendingCall

    def call(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDBusAbstractInterface.call(str, object arg1=QVariant(), object arg2=QVariant(), object arg3=QVariant(), object arg4=QVariant(), object arg5=QVariant(), object arg6=QVariant(), object arg7=QVariant(), object arg8=QVariant()) -> QDBusMessage
        QDBusAbstractInterface.call(QDBus.CallMode, str, object arg1=QVariant(), object arg2=QVariant(), object arg3=QVariant(), object arg4=QVariant(), object arg5=QVariant(), object arg6=QVariant(), object arg7=QVariant(), object arg8=QVariant()) -> QDBusMessage
        """
        pass

    def callWithArgumentList(self, QDBus_CallMode, p_str, list_of_QVariant): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.callWithArgumentList(QDBus.CallMode, str, list-of-QVariant) -> QDBusMessage """
        return QDBusMessage

    def callWithCallback(self, p_str, list_of_QVariant, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDBusAbstractInterface.callWithCallback(str, list-of-QVariant, QObject, SLOT(), SLOT()) -> bool
        QDBusAbstractInterface.callWithCallback(str, list-of-QVariant, callable, callable) -> object
        QDBusAbstractInterface.callWithCallback(str, list-of-QVariant, QObject, SLOT()) -> bool
        QDBusAbstractInterface.callWithCallback(str, list-of-QVariant, callable) -> object
        """
        return object()

    def connection(self): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.connection() -> QDBusConnection """
        return QDBusConnection

    def connectNotify(self, SIGNAL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QDBusAbstractInterface.connectNotify(SIGNAL()) """
        pass

    def disconnectNotify(self, SIGNAL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QDBusAbstractInterface.disconnectNotify(SIGNAL()) """
        pass

    def interface(self): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.interface() -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.isValid() -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.lastError() -> QDBusError """
        return QDBusError

    def path(self): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.path() -> str """
        return ""

    def service(self): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.service() -> str """
        return ""

    def setTimeout(self, p_int): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.setTimeout(int) """
        pass

    def timeout(self): # real signature unknown; restored from __doc__
        """ QDBusAbstractInterface.timeout() -> int """
        return 0

    def __init__(self, p_str, p_str_1, p_str_2, QDBusConnection, QObject): # real signature unknown; restored from __doc__
        pass


class QDBusArgument(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDBusArgument()
    QDBusArgument(QDBusArgument)
    QDBusArgument(object, int id=QMetaType.Int)
    """
    def add(self, p_object, int_id=None): # real signature unknown; restored from __doc__
        """ QDBusArgument.add(object, int id=QMetaType.Int) """
        pass

    def beginArray(self, p_int): # real signature unknown; restored from __doc__
        """ QDBusArgument.beginArray(int) """
        pass

    def beginMap(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QDBusArgument.beginMap(int, int) """
        pass

    def beginMapEntry(self): # real signature unknown; restored from __doc__
        """ QDBusArgument.beginMapEntry() """
        pass

    def beginStructure(self): # real signature unknown; restored from __doc__
        """ QDBusArgument.beginStructure() """
        pass

    def endArray(self): # real signature unknown; restored from __doc__
        """ QDBusArgument.endArray() """
        pass

    def endMap(self): # real signature unknown; restored from __doc__
        """ QDBusArgument.endMap() """
        pass

    def endMapEntry(self): # real signature unknown; restored from __doc__
        """ QDBusArgument.endMapEntry() """
        pass

    def endStructure(self): # real signature unknown; restored from __doc__
        """ QDBusArgument.endStructure() """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDBusConnection(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDBusConnection(str)
    QDBusConnection(QDBusConnection)
    """
    def asyncCall(self, QDBusMessage, int_timeout=-1): # real signature unknown; restored from __doc__
        """ QDBusConnection.asyncCall(QDBusMessage, int timeout=-1) -> QDBusPendingCall """
        return QDBusPendingCall

    def baseService(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.baseService() -> str """
        return ""

    def call(self, QDBusMessage, QDBus_CallMode_mode=None, int_timeout=-1): # real signature unknown; restored from __doc__
        """ QDBusConnection.call(QDBusMessage, QDBus.CallMode mode=QDBus.Block, int timeout=-1) -> QDBusMessage """
        return QDBusMessage

    def callWithCallback(self, QDBusMessage, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDBusConnection.callWithCallback(QDBusMessage, QObject, SLOT(), SLOT(), int timeout=-1) -> bool
        QDBusConnection.callWithCallback(QDBusMessage, callable, callable, int timeout=-1) -> object
        QDBusConnection.callWithCallback(QDBusMessage, QObject, SLOT(), int timeout=-1) -> bool
        QDBusConnection.callWithCallback(QDBusMessage, callable, int timeout=-1) -> object
        """
        return object()

    def connect(self, p_str, p_str_1, p_str_2, p_str_3, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDBusConnection.connect(str, str, str, str, QObject, SLOT()) -> bool
        QDBusConnection.connect(str, str, str, str, callable) -> object
        QDBusConnection.connect(str, str, str, str, str, QObject, SLOT()) -> bool
        QDBusConnection.connect(str, str, str, str, str, callable) -> object
        QDBusConnection.connect(str, str, str, str, list-of-str, str, QObject, SLOT()) -> bool
        QDBusConnection.connect(str, str, str, str, list-of-str, str, callable) -> object
        """
        return object()

    def connectionCapabilities(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.connectionCapabilities() -> QDBusConnection.ConnectionCapabilities """
        pass

    def connectToBus(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDBusConnection.connectToBus(QDBusConnection.BusType, str) -> QDBusConnection
        QDBusConnection.connectToBus(str, str) -> QDBusConnection
        """
        return QDBusConnection

    def connectToPeer(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QDBusConnection.connectToPeer(str, str) -> QDBusConnection """
        return QDBusConnection

    def disconnect(self, p_str, p_str_1, p_str_2, p_str_3, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDBusConnection.disconnect(str, str, str, str, QObject, SLOT()) -> bool
        QDBusConnection.disconnect(str, str, str, str, callable) -> object
        QDBusConnection.disconnect(str, str, str, str, str, QObject, SLOT()) -> bool
        QDBusConnection.disconnect(str, str, str, str, str, callable) -> object
        QDBusConnection.disconnect(str, str, str, str, list-of-str, str, QObject, SLOT()) -> bool
        QDBusConnection.disconnect(str, str, str, str, list-of-str, str, callable) -> object
        """
        return object()

    def disconnectFromBus(self, p_str): # real signature unknown; restored from __doc__
        """ QDBusConnection.disconnectFromBus(str) """
        pass

    def disconnectFromPeer(self, p_str): # real signature unknown; restored from __doc__
        """ QDBusConnection.disconnectFromPeer(str) """
        pass

    def interface(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.interface() -> QDBusConnectionInterface """
        return QDBusConnectionInterface

    def isConnected(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.isConnected() -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.lastError() -> QDBusError """
        return QDBusError

    def localMachineId(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.localMachineId() -> QByteArray """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.name() -> str """
        return ""

    def objectRegisteredAt(self, p_str): # real signature unknown; restored from __doc__
        """ QDBusConnection.objectRegisteredAt(str) -> QObject """
        pass

    def registerObject(self, p_str, QObject, QDBusConnection_RegisterOptions_options=None): # real signature unknown; restored from __doc__
        """ QDBusConnection.registerObject(str, QObject, QDBusConnection.RegisterOptions options=QDBusConnection.ExportAdaptors) -> bool """
        return False

    def registerService(self, p_str): # real signature unknown; restored from __doc__
        """ QDBusConnection.registerService(str) -> bool """
        return False

    def send(self, QDBusMessage): # real signature unknown; restored from __doc__
        """ QDBusConnection.send(QDBusMessage) -> bool """
        return False

    def sender(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.sender() -> QDBusConnection """
        return QDBusConnection

    def sessionBus(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.sessionBus() -> QDBusConnection """
        return QDBusConnection

    def systemBus(self): # real signature unknown; restored from __doc__
        """ QDBusConnection.systemBus() -> QDBusConnection """
        return QDBusConnection

    def unregisterObject(self, p_str, QDBusConnection_UnregisterMode_mode=None): # real signature unknown; restored from __doc__
        """ QDBusConnection.unregisterObject(str, QDBusConnection.UnregisterMode mode=QDBusConnection.UnregisterNode) """
        pass

    def unregisterService(self, p_str): # real signature unknown; restored from __doc__
        """ QDBusConnection.unregisterService(str) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ActivationBus = 2
    BusType = None # (!) real value is ''
    ConnectionCapabilities = None # (!) real value is ''
    ConnectionCapability = None # (!) real value is ''
    ExportAdaptors = 1
    ExportAllContents = 4080
    ExportAllInvokables = 2176
    ExportAllProperties = 1088
    ExportAllSignal = 544
    ExportAllSignals = 544
    ExportAllSlots = 272
    ExportChildObjects = 4096
    ExportNonScriptableContents = 3840
    ExportNonScriptableInvokables = 2048
    ExportNonScriptableProperties = 1024
    ExportNonScriptableSignals = 512
    ExportNonScriptableSlots = 256
    ExportScriptableContents = 240
    ExportScriptableInvokables = 128
    ExportScriptableProperties = 64
    ExportScriptableSignals = 32
    ExportScriptableSlots = 16
    RegisterOption = None # (!) real value is ''
    RegisterOptions = None # (!) real value is ''
    SessionBus = 0
    SystemBus = 1
    UnixFileDescriptorPassing = 1
    UnregisterMode = None # (!) real value is ''
    UnregisterNode = 0
    UnregisterTree = 1


from .QDBusAbstractInterface import QDBusAbstractInterface

class QDBusConnectionInterface(QDBusAbstractInterface):
    # no doc
    def callWithCallbackFailed(self, *args, **kwargs): # real signature unknown
        """ QDBusConnectionInterface.callWithCallbackFailed[QDBusError, QDBusMessage] [signal] """
        pass

    def connectNotify(self, SIGNAL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QDBusConnectionInterface.connectNotify(SIGNAL()) """
        pass

    def disconnectNotify(self, SIGNAL, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QDBusConnectionInterface.disconnectNotify(SIGNAL()) """
        pass

    def isServiceRegistered(self, p_str): # real signature unknown; restored from __doc__
        """ QDBusConnectionInterface.isServiceRegistered(str) -> QDBusReply """
        return QDBusReply

    def registeredServiceNames(self): # real signature unknown; restored from __doc__
        """ QDBusConnectionInterface.registeredServiceNames() -> QDBusReply """
        return QDBusReply

    def registerService(self, p_str, QDBusConnectionInterface_ServiceQueueOptions_qoption=None, QDBusConnectionInterface_ServiceReplacementOptions_roption=None): # real signature unknown; restored from __doc__
        """ QDBusConnectionInterface.registerService(str, QDBusConnectionInterface.ServiceQueueOptions qoption=QDBusConnectionInterface.DontQueueService, QDBusConnectionInterface.ServiceReplacementOptions roption=QDBusConnectionInterface.DontAllowReplacement) -> QDBusReply """
        return QDBusReply

    def serviceOwner(self, p_str): # real signature unknown; restored from __doc__
        """ QDBusConnectionInterface.serviceOwner(str) -> QDBusReply """
        return QDBusReply

    def serviceOwnerChanged(self, *args, **kwargs): # real signature unknown
        """ QDBusConnectionInterface.serviceOwnerChanged[str, str, str] [signal] """
        pass

    def servicePid(self, p_str): # real signature unknown; restored from __doc__
        """ QDBusConnectionInterface.servicePid(str) -> QDBusReply """
        return QDBusReply

    def serviceRegistered(self, *args, **kwargs): # real signature unknown
        """ QDBusConnectionInterface.serviceRegistered[str] [signal] """
        pass

    def serviceUid(self, p_str): # real signature unknown; restored from __doc__
        """ QDBusConnectionInterface.serviceUid(str) -> QDBusReply """
        return QDBusReply

    def serviceUnregistered(self, *args, **kwargs): # real signature unknown
        """ QDBusConnectionInterface.serviceUnregistered[str] [signal] """
        pass

    def startService(self, p_str): # real signature unknown; restored from __doc__
        """ QDBusConnectionInterface.startService(str) -> QDBusReply """
        return QDBusReply

    def unregisterService(self, p_str): # real signature unknown; restored from __doc__
        """ QDBusConnectionInterface.unregisterService(str) -> QDBusReply """
        return QDBusReply

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AllowReplacement = 1
    DontAllowReplacement = 0
    DontQueueService = 0
    QueueService = 1
    RegisterServiceReply = None # (!) real value is ''
    ReplaceExistingService = 2
    ServiceNotRegistered = 0
    ServiceQueued = 2
    ServiceQueueOptions = None # (!) real value is ''
    ServiceRegistered = 1
    ServiceReplacementOptions = None # (!) real value is ''


class QDBusError(): # skipped bases: <class 'sip.simplewrapper'>
    """ QDBusError(QDBusError) """
    def errorString(self, QDBusError_ErrorType): # real signature unknown; restored from __doc__
        """ QDBusError.errorString(QDBusError.ErrorType) -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ QDBusError.isValid() -> bool """
        return False

    def message(self): # real signature unknown; restored from __doc__
        """ QDBusError.message() -> str """
        return ""

    def name(self): # real signature unknown; restored from __doc__
        """ QDBusError.name() -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ QDBusError.type() -> QDBusError.ErrorType """
        pass

    def __init__(self, QDBusError): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AccessDenied = 9
    AddressInUse = 13
    BadAddress = 6
    Disconnected = 14
    ErrorType = None # (!) real value is ''
    Failed = 2
    InternalError = 20
    InvalidArgs = 15
    InvalidInterface = 24
    InvalidMember = 25
    InvalidObjectPath = 23
    InvalidService = 22
    InvalidSignature = 18
    LimitsExceeded = 8
    NoError = 0
    NoMemory = 3
    NoNetwork = 12
    NoReply = 5
    NoServer = 10
    NotSupported = 7
    Other = 1
    ServiceUnknown = 4
    TimedOut = 17
    Timeout = 11
    UnknownInterface = 19
    UnknownMethod = 16
    UnknownObject = 21


from .QDBusAbstractInterface import QDBusAbstractInterface

class QDBusInterface(QDBusAbstractInterface):
    """ QDBusInterface(str, str, str interface=QString(), QDBusConnection connection=QDBusConnection.sessionBus(), QObject parent=None) """
    def __init__(self, p_str, p_str_1, str_interface=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QDBusMessage(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDBusMessage()
    QDBusMessage(QDBusMessage)
    """
    def arguments(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.arguments() -> list-of-QVariant """
        pass

    def autoStartService(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.autoStartService() -> bool """
        return False

    def createError(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDBusMessage.createError(str, str) -> QDBusMessage
        QDBusMessage.createError(QDBusError) -> QDBusMessage
        QDBusMessage.createError(QDBusError.ErrorType, str) -> QDBusMessage
        """
        return QDBusMessage

    def createErrorReply(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDBusMessage.createErrorReply(str, str) -> QDBusMessage
        QDBusMessage.createErrorReply(QDBusError) -> QDBusMessage
        QDBusMessage.createErrorReply(QDBusError.ErrorType, str) -> QDBusMessage
        """
        return QDBusMessage

    def createMethodCall(self, p_str, p_str_1, p_str_2, p_str_3): # real signature unknown; restored from __doc__
        """ QDBusMessage.createMethodCall(str, str, str, str) -> QDBusMessage """
        return QDBusMessage

    def createReply(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDBusMessage.createReply(list-of-QVariant arguments=QList&lt;QVariant&gt;()) -> QDBusMessage
        QDBusMessage.createReply(object) -> QDBusMessage
        """
        return QDBusMessage

    def createSignal(self, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
        """ QDBusMessage.createSignal(str, str, str) -> QDBusMessage """
        return QDBusMessage

    def errorMessage(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.errorMessage() -> str """
        return ""

    def errorName(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.errorName() -> str """
        return ""

    def interface(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.interface() -> str """
        return ""

    def isDelayedReply(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.isDelayedReply() -> bool """
        return False

    def isReplyRequired(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.isReplyRequired() -> bool """
        return False

    def member(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.member() -> str """
        return ""

    def path(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.path() -> str """
        return ""

    def service(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.service() -> str """
        return ""

    def setArguments(self, list_of_QVariant): # real signature unknown; restored from __doc__
        """ QDBusMessage.setArguments(list-of-QVariant) """
        pass

    def setAutoStartService(self, bool): # real signature unknown; restored from __doc__
        """ QDBusMessage.setAutoStartService(bool) """
        pass

    def setDelayedReply(self, bool): # real signature unknown; restored from __doc__
        """ QDBusMessage.setDelayedReply(bool) """
        pass

    def signature(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.signature() -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ QDBusMessage.type() -> QDBusMessage.MessageType """
        pass

    def __init__(self, QDBusMessage=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ErrorMessage = 3
    InvalidMessage = 0
    MessageType = None # (!) real value is ''
    MethodCallMessage = 1
    ReplyMessage = 2
    SignalMessage = 4


class QDBusObjectPath(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDBusObjectPath()
    QDBusObjectPath(str)
    QDBusObjectPath(QDBusObjectPath)
    """
    def path(self): # real signature unknown; restored from __doc__
        """ QDBusObjectPath.path() -> str """
        return ""

    def setPath(self, p_str): # real signature unknown; restored from __doc__
        """ QDBusObjectPath.setPath(str) """
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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
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



class QDBusPendingCall(): # skipped bases: <class 'sip.simplewrapper'>
    """ QDBusPendingCall(QDBusPendingCall) """
    def fromCompletedCall(self, QDBusMessage): # real signature unknown; restored from __doc__
        """ QDBusPendingCall.fromCompletedCall(QDBusMessage) -> QDBusPendingCall """
        return QDBusPendingCall

    def fromError(self, QDBusError): # real signature unknown; restored from __doc__
        """ QDBusPendingCall.fromError(QDBusError) -> QDBusPendingCall """
        return QDBusPendingCall

    def __init__(self, QDBusPendingCall): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



from .QDBusPendingCall import QDBusPendingCall

class QDBusPendingCallWatcher(__PyQt4_QtCore.QObject, QDBusPendingCall):
    """ QDBusPendingCallWatcher(QDBusPendingCall, QObject parent=None) """
    def finished(self, *args, **kwargs): # real signature unknown
        """ QDBusPendingCallWatcher.finished[QDBusPendingCallWatcher] [signal] """
        pass

    def isFinished(self): # real signature unknown; restored from __doc__
        """ QDBusPendingCallWatcher.isFinished() -> bool """
        return False

    def waitForFinished(self): # real signature unknown; restored from __doc__
        """ QDBusPendingCallWatcher.waitForFinished() """
        pass

    def __init__(self, QDBusPendingCall, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


from .QDBusPendingCall import QDBusPendingCall

class QDBusPendingReply(QDBusPendingCall):
    """
    QDBusPendingReply()
    QDBusPendingReply(QDBusPendingReply)
    QDBusPendingReply(QDBusPendingCall)
    QDBusPendingReply(QDBusMessage)
    """
    def argumentAt(self, p_int): # real signature unknown; restored from __doc__
        """ QDBusPendingReply.argumentAt(int) -> object """
        return object()

    def error(self): # real signature unknown; restored from __doc__
        """ QDBusPendingReply.error() -> QDBusError """
        return QDBusError

    def isError(self): # real signature unknown; restored from __doc__
        """ QDBusPendingReply.isError() -> bool """
        return False

    def isFinished(self): # real signature unknown; restored from __doc__
        """ QDBusPendingReply.isFinished() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QDBusPendingReply.isValid() -> bool """
        return False

    def reply(self): # real signature unknown; restored from __doc__
        """ QDBusPendingReply.reply() -> QDBusMessage """
        return QDBusMessage

    def value(self, object_type=None): # real signature unknown; restored from __doc__
        """ QDBusPendingReply.value(object type=None) -> object """
        return object()

    def waitForFinished(self): # real signature unknown; restored from __doc__
        """ QDBusPendingReply.waitForFinished() """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QDBusReply(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDBusReply(QDBusMessage)
    QDBusReply(QDBusPendingCall)
    QDBusReply(QDBusError)
    QDBusReply(QDBusReply)
    """
    def error(self): # real signature unknown; restored from __doc__
        """ QDBusReply.error() -> QDBusError """
        return QDBusError

    def isValid(self): # real signature unknown; restored from __doc__
        """ QDBusReply.isValid() -> bool """
        return False

    def value(self, object_type=None): # real signature unknown; restored from __doc__
        """ QDBusReply.value(object type=None) -> object """
        return object()

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDBusServiceWatcher(__PyQt4_QtCore.QObject):
    """
    QDBusServiceWatcher(QObject parent=None)
    QDBusServiceWatcher(str, QDBusConnection, QDBusServiceWatcher.WatchMode watchMode=QDBusServiceWatcher.WatchForOwnerChange, QObject parent=None)
    """
    def addWatchedService(self, p_str): # real signature unknown; restored from __doc__
        """ QDBusServiceWatcher.addWatchedService(str) """
        pass

    def connection(self): # real signature unknown; restored from __doc__
        """ QDBusServiceWatcher.connection() -> QDBusConnection """
        return QDBusConnection

    def removeWatchedService(self, p_str): # real signature unknown; restored from __doc__
        """ QDBusServiceWatcher.removeWatchedService(str) -> bool """
        return False

    def serviceOwnerChanged(self, *args, **kwargs): # real signature unknown
        """ QDBusServiceWatcher.serviceOwnerChanged[str, str, str] [signal] """
        pass

    def serviceRegistered(self, *args, **kwargs): # real signature unknown
        """ QDBusServiceWatcher.serviceRegistered[str] [signal] """
        pass

    def serviceUnregistered(self, *args, **kwargs): # real signature unknown
        """ QDBusServiceWatcher.serviceUnregistered[str] [signal] """
        pass

    def setConnection(self, QDBusConnection): # real signature unknown; restored from __doc__
        """ QDBusServiceWatcher.setConnection(QDBusConnection) """
        pass

    def setWatchedServices(self, list_of_str): # real signature unknown; restored from __doc__
        """ QDBusServiceWatcher.setWatchedServices(list-of-str) """
        pass

    def setWatchMode(self, QDBusServiceWatcher_WatchMode): # real signature unknown; restored from __doc__
        """ QDBusServiceWatcher.setWatchMode(QDBusServiceWatcher.WatchMode) """
        pass

    def watchedServices(self): # real signature unknown; restored from __doc__
        """ QDBusServiceWatcher.watchedServices() -> list-of-str """
        pass

    def watchMode(self): # real signature unknown; restored from __doc__
        """ QDBusServiceWatcher.watchMode() -> QDBusServiceWatcher.WatchMode """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    WatchForOwnerChange = 3
    WatchForRegistration = 1
    WatchForUnregistration = 2
    WatchMode = None # (!) real value is ''
    WatchModeFlag = None # (!) real value is ''


class QDBusSignature(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDBusSignature()
    QDBusSignature(str)
    QDBusSignature(QDBusSignature)
    """
    def setSignature(self, p_str): # real signature unknown; restored from __doc__
        """ QDBusSignature.setSignature(str) """
        pass

    def signature(self): # real signature unknown; restored from __doc__
        """ QDBusSignature.signature() -> str """
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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
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



class QDBusUnixFileDescriptor(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDBusUnixFileDescriptor()
    QDBusUnixFileDescriptor(int)
    QDBusUnixFileDescriptor(QDBusUnixFileDescriptor)
    """
    def fileDescriptor(self): # real signature unknown; restored from __doc__
        """ QDBusUnixFileDescriptor.fileDescriptor() -> int """
        return 0

    def isSupported(self): # real signature unknown; restored from __doc__
        """ QDBusUnixFileDescriptor.isSupported() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QDBusUnixFileDescriptor.isValid() -> bool """
        return False

    def setFileDescriptor(self, p_int): # real signature unknown; restored from __doc__
        """ QDBusUnixFileDescriptor.setFileDescriptor(int) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDBusVariant(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDBusVariant()
    QDBusVariant(object)
    QDBusVariant(QDBusVariant)
    """
    def setVariant(self, p_object): # real signature unknown; restored from __doc__
        """ QDBusVariant.setVariant(object) """
        pass

    def variant(self): # real signature unknown; restored from __doc__
        """ QDBusVariant.variant() -> object """
        return object()

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


    __hash__ = None


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

