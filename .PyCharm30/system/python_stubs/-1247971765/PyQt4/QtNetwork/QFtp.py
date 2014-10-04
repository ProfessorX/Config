# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt4/QtNetwork.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QFtp(__PyQt4_QtCore.QObject):
    """ QFtp(QObject parent=None) """
    def abort(self): # real signature unknown; restored from __doc__
        """ QFtp.abort() """
        pass

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ QFtp.bytesAvailable() -> int """
        return 0

    def cd(self, p_str): # real signature unknown; restored from __doc__
        """ QFtp.cd(str) -> int """
        return 0

    def clearPendingCommands(self): # real signature unknown; restored from __doc__
        """ QFtp.clearPendingCommands() """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ QFtp.close() -> int """
        return 0

    def commandFinished(self, *args, **kwargs): # real signature unknown
        """ QFtp.commandFinished[int, bool] [signal] """
        pass

    def commandStarted(self, *args, **kwargs): # real signature unknown
        """ QFtp.commandStarted[int] [signal] """
        pass

    def connectToHost(self, p_str, int_port=21): # real signature unknown; restored from __doc__
        """ QFtp.connectToHost(str, int port=21) -> int """
        return 0

    def currentCommand(self): # real signature unknown; restored from __doc__
        """ QFtp.currentCommand() -> QFtp.Command """
        pass

    def currentDevice(self): # real signature unknown; restored from __doc__
        """ QFtp.currentDevice() -> QIODevice """
        pass

    def currentId(self): # real signature unknown; restored from __doc__
        """ QFtp.currentId() -> int """
        return 0

    def dataTransferProgress(self, *args, **kwargs): # real signature unknown
        """ QFtp.dataTransferProgress[int, int] [signal] """
        pass

    def done(self, *args, **kwargs): # real signature unknown
        """ QFtp.done[bool] [signal] """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ QFtp.error() -> QFtp.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QFtp.errorString() -> str """
        return ""

    def get(self, p_str, QIODevice_device=None, QFtp_TransferType_type=None): # real signature unknown; restored from __doc__
        """ QFtp.get(str, QIODevice device=None, QFtp.TransferType type=QFtp.Binary) -> int """
        return 0

    def hasPendingCommands(self): # real signature unknown; restored from __doc__
        """ QFtp.hasPendingCommands() -> bool """
        return False

    def list(self, str_directory=''): # real signature unknown; restored from __doc__
        """ QFtp.list(str directory='') -> int """
        return 0

    def listInfo(self, *args, **kwargs): # real signature unknown
        """ QFtp.listInfo[QUrlInfo] [signal] """
        pass

    def login(self, str_user='', str_password=''): # real signature unknown; restored from __doc__
        """ QFtp.login(str user='', str password='') -> int """
        return 0

    def mkdir(self, p_str): # real signature unknown; restored from __doc__
        """ QFtp.mkdir(str) -> int """
        return 0

    def put(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFtp.put(QByteArray, str, QFtp.TransferType type=QFtp.Binary) -> int
        QFtp.put(QIODevice, str, QFtp.TransferType type=QFtp.Binary) -> int
        """
        return 0

    def rawCommand(self, p_str): # real signature unknown; restored from __doc__
        """ QFtp.rawCommand(str) -> int """
        return 0

    def rawCommandReply(self, *args, **kwargs): # real signature unknown
        """ QFtp.rawCommandReply[int, str] [signal] """
        pass

    def read(self, p_int): # real signature unknown; restored from __doc__
        """ QFtp.read(int) -> bytes """
        return b""

    def readAll(self): # real signature unknown; restored from __doc__
        """ QFtp.readAll() -> QByteArray """
        pass

    def readyRead(self, *args, **kwargs): # real signature unknown
        """ QFtp.readyRead [signal] """
        pass

    def remove(self, p_str): # real signature unknown; restored from __doc__
        """ QFtp.remove(str) -> int """
        return 0

    def rename(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QFtp.rename(str, str) -> int """
        return 0

    def rmdir(self, p_str): # real signature unknown; restored from __doc__
        """ QFtp.rmdir(str) -> int """
        return 0

    def setProxy(self, p_str, p_int): # real signature unknown; restored from __doc__
        """ QFtp.setProxy(str, int) -> int """
        return 0

    def setTransferMode(self, QFtp_TransferMode): # real signature unknown; restored from __doc__
        """ QFtp.setTransferMode(QFtp.TransferMode) -> int """
        return 0

    def state(self): # real signature unknown; restored from __doc__
        """ QFtp.state() -> QFtp.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ QFtp.stateChanged[int] [signal] """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Active = 0
    Ascii = 1
    Binary = 0
    Cd = 7
    Close = 5
    Closing = 5
    Command = None # (!) real value is ''
    Connected = 3
    Connecting = 2
    ConnectionRefused = 3
    ConnectToHost = 3
    Error = None # (!) real value is ''
    Get = 8
    HostLookup = 1
    HostNotFound = 2
    List = 6
    LoggedIn = 4
    Login = 4
    Mkdir = 11
    NoError = 0
    None_ = 0
    NotConnected = 4
    Passive = 1
    Put = 9
    RawCommand = 14
    Remove = 10
    Rename = 13
    Rmdir = 12
    SetProxy = 2
    SetTransferMode = 1
    State = None # (!) real value is ''
    TransferMode = None # (!) real value is ''
    TransferType = None # (!) real value is ''
    Unconnected = 0
    UnknownError = 1


