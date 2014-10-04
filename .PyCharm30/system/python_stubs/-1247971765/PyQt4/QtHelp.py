# encoding: utf-8
# module PyQt4.QtHelp
# from /usr/lib/python3/dist-packages/PyQt4/QtHelp.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


# no functions
# classes

class QHelpContentItem(): # skipped bases: <class 'sip.simplewrapper'>
    # no doc
    def child(self, p_int): # real signature unknown; restored from __doc__
        """ QHelpContentItem.child(int) -> QHelpContentItem """
        return QHelpContentItem

    def childCount(self): # real signature unknown; restored from __doc__
        """ QHelpContentItem.childCount() -> int """
        return 0

    def childPosition(self, QHelpContentItem): # real signature unknown; restored from __doc__
        """ QHelpContentItem.childPosition(QHelpContentItem) -> int """
        return 0

    def parent(self): # real signature unknown; restored from __doc__
        """ QHelpContentItem.parent() -> QHelpContentItem """
        return QHelpContentItem

    def row(self): # real signature unknown; restored from __doc__
        """ QHelpContentItem.row() -> int """
        return 0

    def title(self): # real signature unknown; restored from __doc__
        """ QHelpContentItem.title() -> str """
        return ""

    def url(self): # real signature unknown; restored from __doc__
        """ QHelpContentItem.url() -> QUrl """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QHelpContentModel(__PyQt4_QtCore.QAbstractItemModel):
    # no doc
    def columnCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QHelpContentModel.columnCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def contentItemAt(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QHelpContentModel.contentItemAt(QModelIndex) -> QHelpContentItem """
        return QHelpContentItem

    def contentsCreated(self, *args, **kwargs): # real signature unknown
        """ QHelpContentModel.contentsCreated [signal] """
        pass

    def contentsCreationStarted(self, *args, **kwargs): # real signature unknown
        """ QHelpContentModel.contentsCreationStarted [signal] """
        pass

    def createContents(self, p_str): # real signature unknown; restored from __doc__
        """ QHelpContentModel.createContents(str) """
        pass

    def data(self, QModelIndex, p_int): # real signature unknown; restored from __doc__
        """ QHelpContentModel.data(QModelIndex, int) -> object """
        return object()

    def index(self, p_int, p_int_1, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QHelpContentModel.index(int, int, QModelIndex parent=QModelIndex()) -> QModelIndex """
        pass

    def isCreatingContents(self): # real signature unknown; restored from __doc__
        """ QHelpContentModel.isCreatingContents() -> bool """
        return False

    def parent(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QHelpContentModel.parent(QModelIndex) -> QModelIndex """
        pass

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QHelpContentModel.rowCount(QModelIndex parent=QModelIndex()) -> int """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpContentWidget(__PyQt4_QtGui.QTreeView):
    # no doc
    def indexOf(self, QUrl): # real signature unknown; restored from __doc__
        """ QHelpContentWidget.indexOf(QUrl) -> QModelIndex """
        pass

    def linkActivated(self, *args, **kwargs): # real signature unknown
        """ QHelpContentWidget.linkActivated[QUrl] [signal] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpEngineCore(__PyQt4_QtCore.QObject):
    """ QHelpEngineCore(str, QObject parent=None) """
    def addCustomFilter(self, p_str, list_of_str): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.addCustomFilter(str, list-of-str) -> bool """
        return False

    def autoSaveFilter(self): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.autoSaveFilter() -> bool """
        return False

    def collectionFile(self): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.collectionFile() -> str """
        return ""

    def copyCollectionFile(self, p_str): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.copyCollectionFile(str) -> bool """
        return False

    def currentFilter(self): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.currentFilter() -> str """
        return ""

    def currentFilterChanged(self, *args, **kwargs): # real signature unknown
        """ QHelpEngineCore.currentFilterChanged[str] [signal] """
        pass

    def customFilters(self): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.customFilters() -> list-of-str """
        pass

    def customValue(self, p_str, object_defaultValue=None): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.customValue(str, object defaultValue=None) -> object """
        return object()

    def documentationFileName(self, p_str): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.documentationFileName(str) -> str """
        return ""

    def error(self): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.error() -> str """
        return ""

    def fileData(self, QUrl): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.fileData(QUrl) -> QByteArray """
        pass

    def files(self, p_str, list_of_str, str_extensionFilter=''): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.files(str, list-of-str, str extensionFilter='') -> list-of-QUrl """
        pass

    def filterAttributes(self, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QHelpEngineCore.filterAttributes() -> list-of-str
        QHelpEngineCore.filterAttributes(str) -> list-of-str
        """
        pass

    def filterAttributeSets(self, p_str): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.filterAttributeSets(str) -> list-of-QStringList """
        pass

    def findFile(self, QUrl): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.findFile(QUrl) -> QUrl """
        pass

    def linksForIdentifier(self, p_str): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.linksForIdentifier(str) -> dict-of-QString-QUrl """
        pass

    def metaData(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.metaData(str, str) -> object """
        return object()

    def namespaceName(self, p_str): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.namespaceName(str) -> str """
        return ""

    def registerDocumentation(self, p_str): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.registerDocumentation(str) -> bool """
        return False

    def registeredDocumentations(self): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.registeredDocumentations() -> list-of-str """
        pass

    def removeCustomFilter(self, p_str): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.removeCustomFilter(str) -> bool """
        return False

    def removeCustomValue(self, p_str): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.removeCustomValue(str) -> bool """
        return False

    def setAutoSaveFilter(self, bool): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.setAutoSaveFilter(bool) """
        pass

    def setCollectionFile(self, p_str): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.setCollectionFile(str) """
        pass

    def setCurrentFilter(self, p_str): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.setCurrentFilter(str) """
        pass

    def setCustomValue(self, p_str, p_object): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.setCustomValue(str, object) -> bool """
        return False

    def setupData(self): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.setupData() -> bool """
        return False

    def setupFinished(self, *args, **kwargs): # real signature unknown
        """ QHelpEngineCore.setupFinished [signal] """
        pass

    def setupStarted(self, *args, **kwargs): # real signature unknown
        """ QHelpEngineCore.setupStarted [signal] """
        pass

    def unregisterDocumentation(self, p_str): # real signature unknown; restored from __doc__
        """ QHelpEngineCore.unregisterDocumentation(str) -> bool """
        return False

    def warning(self, *args, **kwargs): # real signature unknown
        """ QHelpEngineCore.warning[str] [signal] """
        pass

    def __init__(self, p_str, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


from .QHelpEngineCore import QHelpEngineCore

class QHelpEngine(QHelpEngineCore):
    """ QHelpEngine(str, QObject parent=None) """
    def contentModel(self): # real signature unknown; restored from __doc__
        """ QHelpEngine.contentModel() -> QHelpContentModel """
        return QHelpContentModel

    def contentWidget(self): # real signature unknown; restored from __doc__
        """ QHelpEngine.contentWidget() -> QHelpContentWidget """
        return QHelpContentWidget

    def indexModel(self): # real signature unknown; restored from __doc__
        """ QHelpEngine.indexModel() -> QHelpIndexModel """
        return QHelpIndexModel

    def indexWidget(self): # real signature unknown; restored from __doc__
        """ QHelpEngine.indexWidget() -> QHelpIndexWidget """
        return QHelpIndexWidget

    def searchEngine(self): # real signature unknown; restored from __doc__
        """ QHelpEngine.searchEngine() -> QHelpSearchEngine """
        return QHelpSearchEngine

    def __init__(self, p_str, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


class QHelpIndexModel(__PyQt4_QtGui.QStringListModel):
    # no doc
    def createIndex(self, p_str): # real signature unknown; restored from __doc__
        """ QHelpIndexModel.createIndex(str) """
        pass

    def filter(self, p_str, str_wildcard=''): # real signature unknown; restored from __doc__
        """ QHelpIndexModel.filter(str, str wildcard='') -> QModelIndex """
        pass

    def indexCreated(self, *args, **kwargs): # real signature unknown
        """ QHelpIndexModel.indexCreated [signal] """
        pass

    def indexCreationStarted(self, *args, **kwargs): # real signature unknown
        """ QHelpIndexModel.indexCreationStarted [signal] """
        pass

    def isCreatingIndex(self): # real signature unknown; restored from __doc__
        """ QHelpIndexModel.isCreatingIndex() -> bool """
        return False

    def linksForKeyword(self, p_str): # real signature unknown; restored from __doc__
        """ QHelpIndexModel.linksForKeyword(str) -> dict-of-QString-QUrl """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpIndexWidget(__PyQt4_QtGui.QListView):
    # no doc
    def activateCurrentItem(self): # real signature unknown; restored from __doc__
        """ QHelpIndexWidget.activateCurrentItem() """
        pass

    def filterIndices(self, p_str, str_wildcard=''): # real signature unknown; restored from __doc__
        """ QHelpIndexWidget.filterIndices(str, str wildcard='') """
        pass

    def linkActivated(self, *args, **kwargs): # real signature unknown
        """ QHelpIndexWidget.linkActivated[QUrl, str] [signal] """
        pass

    def linksActivated(self, *args, **kwargs): # real signature unknown
        """ QHelpIndexWidget.linksActivated[dict-of-QString-QUrl, str] [signal] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QHelpSearchEngine(__PyQt4_QtCore.QObject):
    """ QHelpSearchEngine(QHelpEngineCore, QObject parent=None) """
    def cancelIndexing(self): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.cancelIndexing() """
        pass

    def cancelSearching(self): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.cancelSearching() """
        pass

    def hitCount(self): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.hitCount() -> int """
        return 0

    def hits(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.hits(int, int) -> list-of-tuple-of-QString-QString """
        pass

    def hitsCount(self): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.hitsCount() -> int """
        return 0

    def indexingFinished(self, *args, **kwargs): # real signature unknown
        """ QHelpSearchEngine.indexingFinished [signal] """
        pass

    def indexingStarted(self, *args, **kwargs): # real signature unknown
        """ QHelpSearchEngine.indexingStarted [signal] """
        pass

    def query(self): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.query() -> list-of-QHelpSearchQuery """
        pass

    def queryWidget(self): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.queryWidget() -> QHelpSearchQueryWidget """
        return QHelpSearchQueryWidget

    def reindexDocumentation(self): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.reindexDocumentation() """
        pass

    def resultWidget(self): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.resultWidget() -> QHelpSearchResultWidget """
        return QHelpSearchResultWidget

    def search(self, list_of_QHelpSearchQuery): # real signature unknown; restored from __doc__
        """ QHelpSearchEngine.search(list-of-QHelpSearchQuery) """
        pass

    def searchingFinished(self, *args, **kwargs): # real signature unknown
        """ QHelpSearchEngine.searchingFinished[int] [signal] """
        pass

    def searchingStarted(self, *args, **kwargs): # real signature unknown
        """ QHelpSearchEngine.searchingStarted [signal] """
        pass

    def __init__(self, QHelpEngineCore, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


class QHelpSearchQuery(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QHelpSearchQuery()
    QHelpSearchQuery(QHelpSearchQuery.FieldName, list-of-str)
    QHelpSearchQuery(QHelpSearchQuery)
    """
    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ALL = 4
    ATLEAST = 5
    DEFAULT = 0
    FieldName = None # (!) real value is ''
    FUZZY = 1
    PHRASE = 3
    WITHOUT = 2


class QHelpSearchQueryWidget(__PyQt4_QtGui.QWidget):
    """ QHelpSearchQueryWidget(QWidget parent=None) """
    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def collapseExtendedSearch(self): # real signature unknown; restored from __doc__
        """ QHelpSearchQueryWidget.collapseExtendedSearch() """
        pass

    def expandExtendedSearch(self): # real signature unknown; restored from __doc__
        """ QHelpSearchQueryWidget.expandExtendedSearch() """
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def query(self): # real signature unknown; restored from __doc__
        """ QHelpSearchQueryWidget.query() -> list-of-QHelpSearchQuery """
        pass

    def search(self, *args, **kwargs): # real signature unknown
        """ QHelpSearchQueryWidget.search [signal] """
        pass

    def setQuery(self, list_of_QHelpSearchQuery): # real signature unknown; restored from __doc__
        """ QHelpSearchQueryWidget.setQuery(list-of-QHelpSearchQuery) """
        pass

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass


class QHelpSearchResultWidget(__PyQt4_QtGui.QWidget):
    # no doc
    def linkAt(self, QPoint): # real signature unknown; restored from __doc__
        """ QHelpSearchResultWidget.linkAt(QPoint) -> QUrl """
        pass

    def requestShowLink(self, *args, **kwargs): # real signature unknown
        """ QHelpSearchResultWidget.requestShowLink[QUrl] [signal] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

