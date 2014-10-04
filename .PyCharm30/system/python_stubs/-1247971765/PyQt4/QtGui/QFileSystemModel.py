# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QFileSystemModel(__PyQt4_QtCore.QAbstractItemModel):
    """ QFileSystemModel(QObject parent=None) """
    def canFetchMore(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QFileSystemModel.canFetchMore(QModelIndex) -> bool """
        return False

    def columnCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFileSystemModel.columnCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def data(self, QModelIndex, int_role=None): # real signature unknown; restored from __doc__
        """ QFileSystemModel.data(QModelIndex, int role=Qt.DisplayRole) -> object """
        return object()

    def directoryLoaded(self, *args, **kwargs): # real signature unknown
        """ QFileSystemModel.directoryLoaded[str] [signal] """
        pass

    def dropMimeData(self, QMimeData, Qt_DropAction, p_int, p_int_1, QModelIndex): # real signature unknown; restored from __doc__
        """ QFileSystemModel.dropMimeData(QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool """
        return False

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QFileSystemModel.event(QEvent) -> bool """
        return False

    def fetchMore(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QFileSystemModel.fetchMore(QModelIndex) """
        pass

    def fileIcon(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QFileSystemModel.fileIcon(QModelIndex) -> QIcon """
        return QIcon

    def fileInfo(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QFileSystemModel.fileInfo(QModelIndex) -> QFileInfo """
        pass

    def fileName(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QFileSystemModel.fileName(QModelIndex) -> str """
        return ""

    def filePath(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QFileSystemModel.filePath(QModelIndex) -> str """
        return ""

    def fileRenamed(self, *args, **kwargs): # real signature unknown
        """ QFileSystemModel.fileRenamed[str, str, str] [signal] """
        pass

    def filter(self): # real signature unknown; restored from __doc__
        """ QFileSystemModel.filter() -> QDir.Filters """
        pass

    def flags(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QFileSystemModel.flags(QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFileSystemModel.hasChildren(QModelIndex parent=QModelIndex()) -> bool """
        pass

    def headerData(self, p_int, Qt_Orientation, int_role=None): # real signature unknown; restored from __doc__
        """ QFileSystemModel.headerData(int, Qt.Orientation, int role=Qt.DisplayRole) -> object """
        return object()

    def iconProvider(self): # real signature unknown; restored from __doc__
        """ QFileSystemModel.iconProvider() -> QFileIconProvider """
        return QFileIconProvider

    def index(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFileSystemModel.index(int, int, QModelIndex parent=QModelIndex()) -> QModelIndex
        QFileSystemModel.index(str, int column=0) -> QModelIndex
        """
        pass

    def isDir(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QFileSystemModel.isDir(QModelIndex) -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ QFileSystemModel.isReadOnly() -> bool """
        return False

    def lastModified(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QFileSystemModel.lastModified(QModelIndex) -> QDateTime """
        pass

    def mimeData(self, list_of_QModelIndex): # real signature unknown; restored from __doc__
        """ QFileSystemModel.mimeData(list-of-QModelIndex) -> QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ QFileSystemModel.mimeTypes() -> list-of-str """
        pass

    def mkdir(self, QModelIndex, p_str): # real signature unknown; restored from __doc__
        """ QFileSystemModel.mkdir(QModelIndex, str) -> QModelIndex """
        pass

    def myComputer(self, int_role=None): # real signature unknown; restored from __doc__
        """ QFileSystemModel.myComputer(int role=Qt.DisplayRole) -> object """
        return object()

    def nameFilterDisables(self): # real signature unknown; restored from __doc__
        """ QFileSystemModel.nameFilterDisables() -> bool """
        return False

    def nameFilters(self): # real signature unknown; restored from __doc__
        """ QFileSystemModel.nameFilters() -> list-of-str """
        pass

    def parent(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QFileSystemModel.parent(QModelIndex) -> QModelIndex """
        pass

    def permissions(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QFileSystemModel.permissions(QModelIndex) -> QFile.Permissions """
        pass

    def remove(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QFileSystemModel.remove(QModelIndex) -> bool """
        return False

    def resolveSymlinks(self): # real signature unknown; restored from __doc__
        """ QFileSystemModel.resolveSymlinks() -> bool """
        return False

    def rmdir(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QFileSystemModel.rmdir(QModelIndex) -> bool """
        return False

    def rootDirectory(self): # real signature unknown; restored from __doc__
        """ QFileSystemModel.rootDirectory() -> QDir """
        pass

    def rootPath(self): # real signature unknown; restored from __doc__
        """ QFileSystemModel.rootPath() -> str """
        return ""

    def rootPathChanged(self, *args, **kwargs): # real signature unknown
        """ QFileSystemModel.rootPathChanged[str] [signal] """
        pass

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QFileSystemModel.rowCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def setData(self, QModelIndex, p_object, int_role=None): # real signature unknown; restored from __doc__
        """ QFileSystemModel.setData(QModelIndex, object, int role=Qt.EditRole) -> bool """
        return False

    def setFilter(self, QDir_Filters): # real signature unknown; restored from __doc__
        """ QFileSystemModel.setFilter(QDir.Filters) """
        pass

    def setIconProvider(self, QFileIconProvider): # real signature unknown; restored from __doc__
        """ QFileSystemModel.setIconProvider(QFileIconProvider) """
        pass

    def setNameFilterDisables(self, bool): # real signature unknown; restored from __doc__
        """ QFileSystemModel.setNameFilterDisables(bool) """
        pass

    def setNameFilters(self, list_of_str): # real signature unknown; restored from __doc__
        """ QFileSystemModel.setNameFilters(list-of-str) """
        pass

    def setReadOnly(self, bool): # real signature unknown; restored from __doc__
        """ QFileSystemModel.setReadOnly(bool) """
        pass

    def setResolveSymlinks(self, bool): # real signature unknown; restored from __doc__
        """ QFileSystemModel.setResolveSymlinks(bool) """
        pass

    def setRootPath(self, p_str): # real signature unknown; restored from __doc__
        """ QFileSystemModel.setRootPath(str) -> QModelIndex """
        pass

    def size(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QFileSystemModel.size(QModelIndex) -> int """
        return 0

    def sort(self, p_int, Qt_SortOrder_order=None): # real signature unknown; restored from __doc__
        """ QFileSystemModel.sort(int, Qt.SortOrder order=Qt.AscendingOrder) """
        pass

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ QFileSystemModel.supportedDropActions() -> Qt.DropActions """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ QFileSystemModel.timerEvent(QTimerEvent) """
        pass

    def type(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QFileSystemModel.type(QModelIndex) -> str """
        return ""

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    FileIconRole = 1
    FileNameRole = 34
    FilePathRole = 33
    FilePermissions = 35
    Roles = None # (!) real value is ''


