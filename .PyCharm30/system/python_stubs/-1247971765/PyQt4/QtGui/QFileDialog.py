# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from .QDialog import QDialog

class QFileDialog(QDialog):
    """
    QFileDialog(QWidget, Qt.WindowFlags)
    QFileDialog(QWidget parent=None, str caption='', str directory='', str filter='')
    """
    def accept(self): # real signature unknown; restored from __doc__
        """ QFileDialog.accept() """
        pass

    def acceptMode(self): # real signature unknown; restored from __doc__
        """ QFileDialog.acceptMode() -> QFileDialog.AcceptMode """
        pass

    def changeEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QFileDialog.changeEvent(QEvent) """
        pass

    def confirmOverwrite(self): # real signature unknown; restored from __doc__
        """ QFileDialog.confirmOverwrite() -> bool """
        return False

    def currentChanged(self, *args, **kwargs): # real signature unknown
        """ QFileDialog.currentChanged[str] [signal] """
        pass

    def defaultSuffix(self): # real signature unknown; restored from __doc__
        """ QFileDialog.defaultSuffix() -> str """
        return ""

    def directory(self): # real signature unknown; restored from __doc__
        """ QFileDialog.directory() -> QDir """
        pass

    def directoryEntered(self, *args, **kwargs): # real signature unknown
        """ QFileDialog.directoryEntered[str] [signal] """
        pass

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ QFileDialog.done(int) """
        pass

    def fileMode(self): # real signature unknown; restored from __doc__
        """ QFileDialog.fileMode() -> QFileDialog.FileMode """
        pass

    def fileSelected(self, *args, **kwargs): # real signature unknown
        """ QFileDialog.fileSelected[str] [signal] """
        pass

    def filesSelected(self, *args, **kwargs): # real signature unknown
        """ QFileDialog.filesSelected[list-of-str] [signal] """
        pass

    def filter(self): # real signature unknown; restored from __doc__
        """ QFileDialog.filter() -> QDir.Filters """
        pass

    def filters(self): # real signature unknown; restored from __doc__
        """ QFileDialog.filters() -> list-of-str """
        pass

    def filterSelected(self, *args, **kwargs): # real signature unknown
        """ QFileDialog.filterSelected[str] [signal] """
        pass

    def getExistingDirectory(self, QWidget_parent=None, str_caption='', str_directory='', QFileDialog_Options_options=None): # real signature unknown; restored from __doc__
        """ QFileDialog.getExistingDirectory(QWidget parent=None, str caption='', str directory='', QFileDialog.Options options=QFileDialog.ShowDirsOnly) -> str """
        return ""

    def getOpenFileName(self, QWidget_parent=None, str_caption='', str_directory='', str_filter='', QFileDialog_Options_options=0): # real signature unknown; restored from __doc__
        """ QFileDialog.getOpenFileName(QWidget parent=None, str caption='', str directory='', str filter='', QFileDialog.Options options=0) -> str """
        return ""

    def getOpenFileNameAndFilter(self, QWidget_parent=None, str_caption='', str_directory='', str_filter='', str_initialFilter='', QFileDialog_Options_options=0): # real signature unknown; restored from __doc__
        """ QFileDialog.getOpenFileNameAndFilter(QWidget parent=None, str caption='', str directory='', str filter='', str initialFilter='', QFileDialog.Options options=0) -> (str, str) """
        pass

    def getOpenFileNames(self, QWidget_parent=None, str_caption='', str_directory='', str_filter='', QFileDialog_Options_options=0): # real signature unknown; restored from __doc__
        """ QFileDialog.getOpenFileNames(QWidget parent=None, str caption='', str directory='', str filter='', QFileDialog.Options options=0) -> list-of-str """
        pass

    def getOpenFileNamesAndFilter(self, QWidget_parent=None, str_caption='', str_directory='', str_filter='', str_initialFilter='', QFileDialog_Options_options=0): # real signature unknown; restored from __doc__
        """ QFileDialog.getOpenFileNamesAndFilter(QWidget parent=None, str caption='', str directory='', str filter='', str initialFilter='', QFileDialog.Options options=0) -> (str, str) """
        pass

    def getSaveFileName(self, QWidget_parent=None, str_caption='', str_directory='', str_filter='', QFileDialog_Options_options=0): # real signature unknown; restored from __doc__
        """ QFileDialog.getSaveFileName(QWidget parent=None, str caption='', str directory='', str filter='', QFileDialog.Options options=0) -> str """
        return ""

    def getSaveFileNameAndFilter(self, QWidget_parent=None, str_caption='', str_directory='', str_filter='', str_initialFilter='', QFileDialog_Options_options=0): # real signature unknown; restored from __doc__
        """ QFileDialog.getSaveFileNameAndFilter(QWidget parent=None, str caption='', str directory='', str filter='', str initialFilter='', QFileDialog.Options options=0) -> (str, str) """
        pass

    def history(self): # real signature unknown; restored from __doc__
        """ QFileDialog.history() -> list-of-str """
        pass

    def iconProvider(self): # real signature unknown; restored from __doc__
        """ QFileDialog.iconProvider() -> QFileIconProvider """
        return QFileIconProvider

    def isNameFilterDetailsVisible(self): # real signature unknown; restored from __doc__
        """ QFileDialog.isNameFilterDetailsVisible() -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ QFileDialog.isReadOnly() -> bool """
        return False

    def itemDelegate(self): # real signature unknown; restored from __doc__
        """ QFileDialog.itemDelegate() -> QAbstractItemDelegate """
        return QAbstractItemDelegate

    def labelText(self, QFileDialog_DialogLabel): # real signature unknown; restored from __doc__
        """ QFileDialog.labelText(QFileDialog.DialogLabel) -> str """
        return ""

    def nameFilters(self): # real signature unknown; restored from __doc__
        """ QFileDialog.nameFilters() -> list-of-str """
        pass

    def open(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFileDialog.open()
        QFileDialog.open(QObject, SLOT())
        QFileDialog.open(callable)
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ QFileDialog.options() -> QFileDialog.Options """
        pass

    def proxyModel(self): # real signature unknown; restored from __doc__
        """ QFileDialog.proxyModel() -> QAbstractProxyModel """
        return QAbstractProxyModel

    def resolveSymlinks(self): # real signature unknown; restored from __doc__
        """ QFileDialog.resolveSymlinks() -> bool """
        return False

    def restoreState(self, QByteArray): # real signature unknown; restored from __doc__
        """ QFileDialog.restoreState(QByteArray) -> bool """
        return False

    def saveState(self): # real signature unknown; restored from __doc__
        """ QFileDialog.saveState() -> QByteArray """
        pass

    def selectedFiles(self): # real signature unknown; restored from __doc__
        """ QFileDialog.selectedFiles() -> list-of-str """
        pass

    def selectedFilter(self): # real signature unknown; restored from __doc__
        """ QFileDialog.selectedFilter() -> str """
        return ""

    def selectedNameFilter(self): # real signature unknown; restored from __doc__
        """ QFileDialog.selectedNameFilter() -> str """
        return ""

    def selectFile(self, p_str): # real signature unknown; restored from __doc__
        """ QFileDialog.selectFile(str) """
        pass

    def selectFilter(self, p_str): # real signature unknown; restored from __doc__
        """ QFileDialog.selectFilter(str) """
        pass

    def selectNameFilter(self, p_str): # real signature unknown; restored from __doc__
        """ QFileDialog.selectNameFilter(str) """
        pass

    def setAcceptMode(self, QFileDialog_AcceptMode): # real signature unknown; restored from __doc__
        """ QFileDialog.setAcceptMode(QFileDialog.AcceptMode) """
        pass

    def setConfirmOverwrite(self, bool): # real signature unknown; restored from __doc__
        """ QFileDialog.setConfirmOverwrite(bool) """
        pass

    def setDefaultSuffix(self, p_str): # real signature unknown; restored from __doc__
        """ QFileDialog.setDefaultSuffix(str) """
        pass

    def setDirectory(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFileDialog.setDirectory(str)
        QFileDialog.setDirectory(QDir)
        """
        pass

    def setFileMode(self, QFileDialog_FileMode): # real signature unknown; restored from __doc__
        """ QFileDialog.setFileMode(QFileDialog.FileMode) """
        pass

    def setFilter(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFileDialog.setFilter(str)
        QFileDialog.setFilter(QDir.Filters)
        """
        pass

    def setFilters(self, list_of_str): # real signature unknown; restored from __doc__
        """ QFileDialog.setFilters(list-of-str) """
        pass

    def setHistory(self, list_of_str): # real signature unknown; restored from __doc__
        """ QFileDialog.setHistory(list-of-str) """
        pass

    def setIconProvider(self, QFileIconProvider): # real signature unknown; restored from __doc__
        """ QFileDialog.setIconProvider(QFileIconProvider) """
        pass

    def setItemDelegate(self, QAbstractItemDelegate): # real signature unknown; restored from __doc__
        """ QFileDialog.setItemDelegate(QAbstractItemDelegate) """
        pass

    def setLabelText(self, QFileDialog_DialogLabel, p_str): # real signature unknown; restored from __doc__
        """ QFileDialog.setLabelText(QFileDialog.DialogLabel, str) """
        pass

    def setNameFilter(self, p_str): # real signature unknown; restored from __doc__
        """ QFileDialog.setNameFilter(str) """
        pass

    def setNameFilterDetailsVisible(self, bool): # real signature unknown; restored from __doc__
        """ QFileDialog.setNameFilterDetailsVisible(bool) """
        pass

    def setNameFilters(self, list_of_str): # real signature unknown; restored from __doc__
        """ QFileDialog.setNameFilters(list-of-str) """
        pass

    def setOption(self, QFileDialog_Option, bool_on=True): # real signature unknown; restored from __doc__
        """ QFileDialog.setOption(QFileDialog.Option, bool on=True) """
        pass

    def setOptions(self, QFileDialog_Options): # real signature unknown; restored from __doc__
        """ QFileDialog.setOptions(QFileDialog.Options) """
        pass

    def setProxyModel(self, QAbstractProxyModel): # real signature unknown; restored from __doc__
        """ QFileDialog.setProxyModel(QAbstractProxyModel) """
        pass

    def setReadOnly(self, bool): # real signature unknown; restored from __doc__
        """ QFileDialog.setReadOnly(bool) """
        pass

    def setResolveSymlinks(self, bool): # real signature unknown; restored from __doc__
        """ QFileDialog.setResolveSymlinks(bool) """
        pass

    def setSidebarUrls(self, list_of_QUrl): # real signature unknown; restored from __doc__
        """ QFileDialog.setSidebarUrls(list-of-QUrl) """
        pass

    def setViewMode(self, QFileDialog_ViewMode): # real signature unknown; restored from __doc__
        """ QFileDialog.setViewMode(QFileDialog.ViewMode) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ QFileDialog.setVisible(bool) """
        pass

    def sidebarUrls(self): # real signature unknown; restored from __doc__
        """ QFileDialog.sidebarUrls() -> list-of-QUrl """
        pass

    def testOption(self, QFileDialog_Option): # real signature unknown; restored from __doc__
        """ QFileDialog.testOption(QFileDialog.Option) -> bool """
        return False

    def viewMode(self): # real signature unknown; restored from __doc__
        """ QFileDialog.viewMode() -> QFileDialog.ViewMode """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Accept = 3
    AcceptMode = None # (!) real value is ''
    AcceptOpen = 0
    AcceptSave = 1
    AnyFile = 0
    Detail = 0
    DialogLabel = None # (!) real value is ''
    Directory = 2
    DirectoryOnly = 4
    DontConfirmOverwrite = 4
    DontResolveSymlinks = 2
    DontUseCustomDirectoryIcons = 128
    DontUseNativeDialog = 16
    DontUseSheet = 8
    ExistingFile = 1
    ExistingFiles = 3
    FileMode = None # (!) real value is ''
    FileName = 1
    FileType = 2
    HideNameFilterDetails = 64
    List = 1
    LookIn = 0
    Option = None # (!) real value is ''
    Options = None # (!) real value is ''
    ReadOnly = 32
    Reject = 4
    ShowDirsOnly = 1
    ViewMode = None # (!) real value is ''


