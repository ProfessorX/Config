# encoding: utf-8
# module PyKDE4.kio
# from /usr/lib/python3/dist-packages/PyKDE4/kio.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyKDE4.kdeui as __PyKDE4_kdeui
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


class KIO(): # skipped bases: <class 'sip.wrapper'>
    # no doc
    def buildErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def calculateRemaining(self, *args, **kwargs): # real signature unknown
        pass

    def calculateRemainingSeconds(self, *args, **kwargs): # real signature unknown
        pass

    def canPasteMimeSource(self, *args, **kwargs): # real signature unknown
        pass

    def chmod(self, *args, **kwargs): # real signature unknown
        pass

    def chown(self, *args, **kwargs): # real signature unknown
        pass

    def convertSeconds(self, *args, **kwargs): # real signature unknown
        pass

    def convertSize(self, *args, **kwargs): # real signature unknown
        pass

    def convertSizeFromKiB(self, *args, **kwargs): # real signature unknown
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def copyAs(self, *args, **kwargs): # real signature unknown
        pass

    def davPropFind(self, *args, **kwargs): # real signature unknown
        pass

    def davPropPatch(self, *args, **kwargs): # real signature unknown
        pass

    def davReport(self, *args, **kwargs): # real signature unknown
        pass

    def davSearch(self, *args, **kwargs): # real signature unknown
        pass

    def decodeFileName(self, *args, **kwargs): # real signature unknown
        pass

    def del_(self, *args, **kwargs): # real signature unknown
        pass

    def directorySize(self, *args, **kwargs): # real signature unknown
        pass

    def encodeFileName(self, *args, **kwargs): # real signature unknown
        pass

    def fileMetaInfo(self, *args, **kwargs): # real signature unknown
        pass

    def filePreview(self, *args, **kwargs): # real signature unknown
        pass

    def file_copy(self, *args, **kwargs): # real signature unknown
        pass

    def file_delete(self, *args, **kwargs): # real signature unknown
        pass

    def file_move(self, *args, **kwargs): # real signature unknown
        pass

    def get(self, *args, **kwargs): # real signature unknown
        pass

    def getCacheControlString(self, *args, **kwargs): # real signature unknown
        pass

    def getJobTracker(self, *args, **kwargs): # real signature unknown
        pass

    def http_delete(self, *args, **kwargs): # real signature unknown
        pass

    def http_post(self, *args, **kwargs): # real signature unknown
        pass

    def http_update_cache(self, *args, **kwargs): # real signature unknown
        pass

    def itemsSummaryString(self, *args, **kwargs): # real signature unknown
        pass

    def link(self, *args, **kwargs): # real signature unknown
        pass

    def linkAs(self, *args, **kwargs): # real signature unknown
        pass

    def listDir(self, *args, **kwargs): # real signature unknown
        pass

    def listRecursive(self, *args, **kwargs): # real signature unknown
        pass

    def mimetype(self, *args, **kwargs): # real signature unknown
        pass

    def mkdir(self, *args, **kwargs): # real signature unknown
        pass

    def mostLocalUrl(self, *args, **kwargs): # real signature unknown
        pass

    def mount(self, *args, **kwargs): # real signature unknown
        pass

    def move(self, *args, **kwargs): # real signature unknown
        pass

    def moveAs(self, *args, **kwargs): # real signature unknown
        pass

    def multi_get(self, *args, **kwargs): # real signature unknown
        pass

    def number(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, *args, **kwargs): # real signature unknown
        pass

    def parseCacheControl(self, *args, **kwargs): # real signature unknown
        pass

    def pasteActionText(self, *args, **kwargs): # real signature unknown
        pass

    def pasteClipboard(self, *args, **kwargs): # real signature unknown
        pass

    def pasteData(self, *args, **kwargs): # real signature unknown
        pass

    def pasteDataAsync(self, *args, **kwargs): # real signature unknown
        pass

    def pasteMimeData(self, *args, **kwargs): # real signature unknown
        pass

    def pasteMimeSource(self, *args, **kwargs): # real signature unknown
        pass

    def put(self, *args, **kwargs): # real signature unknown
        pass

    def rawErrorDetail(self, *args, **kwargs): # real signature unknown
        pass

    def rename(self, *args, **kwargs): # real signature unknown
        pass

    def rmdir(self, *args, **kwargs): # real signature unknown
        pass

    def setModificationTime(self, *args, **kwargs): # real signature unknown
        pass

    def special(self, *args, **kwargs): # real signature unknown
        pass

    def stat(self, *args, **kwargs): # real signature unknown
        pass

    def storedGet(self, *args, **kwargs): # real signature unknown
        pass

    def storedHttpPost(self, *args, **kwargs): # real signature unknown
        pass

    def storedPut(self, *args, **kwargs): # real signature unknown
        pass

    def symlink(self, *args, **kwargs): # real signature unknown
        pass

    def trash(self, *args, **kwargs): # real signature unknown
        pass

    def unmount(self, *args, **kwargs): # real signature unknown
        pass

    def unsupportedActionErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AccessManager = None # (!) real value is ''
    AuthInfo = None # (!) real value is ''
    CacheControl = None # (!) real value is ''
    CC_Cache = 1
    CC_CacheOnly = 0
    CC_Refresh = 3
    CC_Reload = 4
    CC_Verify = 2
    ChmodJob = None # (!) real value is ''
    CMD_CHMOD = 76
    CMD_CHOWN = 89
    CMD_CLOSE = 93
    CMD_CONFIG = 85
    CMD_CONNECT = 49
    CMD_COPY = 74
    CMD_DEL = 75
    CMD_DISCONNECT = 50
    CMD_GET = 67
    CMD_HOST = 48
    CMD_HOST_INFO = 94
    CMD_LISTDIR = 71
    CMD_MESSAGEBOXANSWER = 83
    CMD_META_DATA = 80
    CMD_MIMETYPE = 70
    CMD_MKDIR = 72
    CMD_MULTI_GET = 86
    CMD_NONE = 65
    CMD_OPEN = 88
    CMD_PUT = 68
    CMD_READ = 90
    CMD_RENAME = 73
    CMD_REPARSECONFIGURATION = 79
    CMD_RESUMEANSWER = 84
    CMD_SEEK = 92
    CMD_SETLINKDEST = 87
    CMD_SETMODIFICATIONTIME = 78
    CMD_SLAVE_CONNECT = 52
    CMD_SLAVE_HOLD = 53
    CMD_SLAVE_STATUS = 51
    CMD_SPECIAL = 77
    CMD_STAT = 69
    CMD_SUBURL = 82
    CMD_SYMLINK = 81
    CMD_TESTDIR = 66
    CMD_WRITE = 91
    Command = None # (!) real value is ''
    Connection = None # (!) real value is ''
    ConnectionServer = None # (!) real value is ''
    CopyInfo = None # (!) real value is ''
    CopyJob = None # (!) real value is ''
    DavJob = None # (!) real value is ''
    DefaultFlags = 0
    DeleteJob = None # (!) real value is ''
    DirectorySizeJob = None # (!) real value is ''
    Error = None # (!) real value is ''
    ERR_ABORTED = 147
    ERR_ACCESS_DENIED = 115
    ERR_CANNOT_CHMOD = 141
    ERR_CANNOT_CHOWN = 168
    ERR_CANNOT_DELETE = 142
    ERR_CANNOT_DELETE_ORIGINAL = 154
    ERR_CANNOT_DELETE_PARTIAL = 155
    ERR_CANNOT_ENTER_DIRECTORY = 117
    ERR_CANNOT_LAUNCH_PROCESS = 103
    ERR_CANNOT_OPEN_FOR_READING = 101
    ERR_CANNOT_OPEN_FOR_WRITING = 102
    ERR_CANNOT_RENAME = 140
    ERR_CANNOT_RENAME_ORIGINAL = 156
    ERR_CANNOT_RENAME_PARTIAL = 157
    ERR_CANNOT_RESUME = 139
    ERR_CANNOT_SETTIME = 167
    ERR_CANNOT_SYMLINK = 159
    ERR_CONNECTION_BROKEN = 124
    ERR_COULD_NOT_ACCEPT = 132
    ERR_COULD_NOT_AUTHENTICATE = 146
    ERR_COULD_NOT_BIND = 130
    ERR_COULD_NOT_CLOSEDIR = 135
    ERR_COULD_NOT_CONNECT = 123
    ERR_COULD_NOT_CREATE_SOCKET = 122
    ERR_COULD_NOT_LISTEN = 131
    ERR_COULD_NOT_LOGIN = 133
    ERR_COULD_NOT_MKDIR = 137
    ERR_COULD_NOT_MOUNT = 126
    ERR_COULD_NOT_READ = 128
    ERR_COULD_NOT_RMDIR = 138
    ERR_COULD_NOT_SEEK = 166
    ERR_COULD_NOT_STAT = 134
    ERR_COULD_NOT_UNMOUNT = 127
    ERR_COULD_NOT_WRITE = 129
    ERR_CYCLIC_COPY = 121
    ERR_CYCLIC_LINK = 119
    ERR_DIR_ALREADY_EXIST = 113
    ERR_DISK_FULL = 161
    ERR_DOES_NOT_EXIST = 111
    ERR_FILE_ALREADY_EXIST = 112
    ERR_IDENTICAL_FILES = 162
    ERR_INTERNAL = 104
    ERR_INTERNAL_SERVER = 148
    ERR_IS_DIRECTORY = 109
    ERR_IS_FILE = 110
    ERR_MALFORMED_URL = 105
    ERR_NEED_PASSWD = 158
    ERR_NOT_FILTER_PROTOCOL = 125
    ERR_NO_CONTENT = 160
    ERR_NO_SOURCE_PROTOCOL = 107
    ERR_OUT_OF_MEMORY = 144
    ERR_POST_DENIED = 165
    ERR_POST_NO_SIZE = 169
    ERR_PROTOCOL_IS_NOT_A_FILESYSTEM = 118
    ERR_SERVER_TIMEOUT = 149
    ERR_SERVICE_NOT_AVAILABLE = 150
    ERR_SLAVE_DEFINED = 163
    ERR_SLAVE_DIED = 143
    ERR_UNKNOWN = 151
    ERR_UNKNOWN_HOST = 114
    ERR_UNKNOWN_INTERRUPT = 153
    ERR_UNKNOWN_PROXY_HOST = 145
    ERR_UNSUPPORTED_ACTION = 108
    ERR_UNSUPPORTED_PROTOCOL = 106
    ERR_UPGRADE_REQUIRED = 164
    ERR_USER_CANCELED = 1
    ERR_WRITE_ACCESS_DENIED = 116
    FileCopyJob = None # (!) real value is ''
    FileJob = None # (!) real value is ''
    FileUndoManager = None # (!) real value is ''
    ForwardingSlaveBase = None # (!) real value is ''
    HideProgressInfo = 1
    Info = None # (!) real value is ''
    INF_ERROR_PAGE = 22
    INF_GETTING_FILE = 24
    INF_INFOMESSAGE = 26
    INF_MESSAGEBOX = 29
    INF_META_DATA = 27
    INF_MIME_TYPE = 21
    INF_NETWORK_STATUS = 28
    INF_POSITION = 30
    INF_PROCESSED_SIZE = 11
    INF_REDIRECTION = 20
    INF_SPEED = 12
    INF_TOTAL_SIZE = 10
    INF_UNUSED = 25
    INF_WARNING = 23
    Integration = None # (!) real value is ''
    Job = None # (!) real value is ''
    JobFlag = None # (!) real value is ''
    JobFlags = None # (!) real value is ''
    JobUiDelegate = None # (!) real value is ''
    ListJob = None # (!) real value is ''
    LoadType = None # (!) real value is ''
    Message = None # (!) real value is ''
    MetaInfoJob = None # (!) real value is ''
    MimetypeJob = None # (!) real value is ''
    MSG_AUTH_KEY = 115
    MSG_CANRESUME = 114
    MSG_CONNECTED = 103
    MSG_DATA = 100
    MSG_DATA_REQ = 101
    MSG_DEL_AUTH_KEY = 116
    MSG_ERROR = 102
    MSG_FINISHED = 104
    MSG_HOST_INFO_REQ = 119
    MSG_LIST_ENTRIES = 106
    MSG_NEED_SUBURL_DATA = 113
    MSG_NET_DROP = 112
    MSG_NET_REQUEST = 111
    MSG_OPENED = 117
    MSG_RENAMED = 107
    MSG_RESUME = 108
    MSG_SLAVE_ACK = 110
    MSG_SLAVE_STATUS = 109
    MSG_STAT_ENTRY = 105
    MSG_WRITTEN = 118
    MultiGetJob = None # (!) real value is ''
    M_ISDIR = 128
    M_MULTI = 16
    M_NORENAME = 64
    M_OVERWRITE = 1
    M_OVERWRITE_ITSELF = 2
    M_RESUME = 32
    M_SINGLE = 8
    M_SKIP = 4
    NetAccess = None # (!) real value is ''
    NetRC = None # (!) real value is ''
    NoReload = 1
    Overwrite = 4
    PasswordDialog = None # (!) real value is ''
    PreviewJob = None # (!) real value is ''
    Reload = 0
    RenameDialog = None # (!) real value is ''
    RenameDialogPlugin = None # (!) real value is ''
    RenameDialog_Mode = None # (!) real value is ''
    RenameDialog_Result = None # (!) real value is ''
    Resume = 2
    R_AUTO_RENAME = 8
    R_AUTO_SKIP = 3
    R_CANCEL = 0
    R_OVERWRITE = 4
    R_OVERWRITE_ALL = 5
    R_RENAME = 1
    R_RESUME = 6
    R_RESUME_ALL = 7
    R_SKIP = 2
    Scheduler = None # (!) real value is ''
    SessionData = None # (!) real value is ''
    SimpleJob = None # (!) real value is ''
    SkipDialog = None # (!) real value is ''
    SkipDialog_Result = None # (!) real value is ''
    Slave = None # (!) real value is ''
    SlaveBase = None # (!) real value is ''
    SlaveConfig = None # (!) real value is ''
    SlaveInterface = None # (!) real value is ''
    SpecialJob = None # (!) real value is ''
    SslUi = None # (!) real value is ''
    StatJob = None # (!) real value is ''
    StoredTransferJob = None # (!) real value is ''
    S_AUTO_SKIP = 2
    S_CANCEL = 0
    S_SKIP = 1
    TCPSlaveBase = None # (!) real value is ''
    TransferJob = None # (!) real value is ''
    UDSEntry = None # (!) real value is ''


