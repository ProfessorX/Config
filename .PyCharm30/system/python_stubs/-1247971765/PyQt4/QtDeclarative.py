# encoding: utf-8
# module PyQt4.QtDeclarative
# from /usr/lib/python3/dist-packages/PyQt4/QtDeclarative.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


# functions

def QPyDeclarativeListProperty(QObject, list_of_QObject): # real signature unknown; restored from __doc__
    """ QPyDeclarativeListProperty(QObject, list-of-QObject) """
    pass

# classes

class QDeclarativeComponent(__PyQt4_QtCore.QObject):
    """
    QDeclarativeComponent(QDeclarativeEngine, QObject parent=None)
    QDeclarativeComponent(QDeclarativeEngine, str, QObject parent=None)
    QDeclarativeComponent(QDeclarativeEngine, QUrl, QObject parent=None)
    """
    def beginCreate(self, QDeclarativeContext): # real signature unknown; restored from __doc__
        """ QDeclarativeComponent.beginCreate(QDeclarativeContext) -> QObject """
        pass

    def completeCreate(self): # real signature unknown; restored from __doc__
        """ QDeclarativeComponent.completeCreate() """
        pass

    def create(self, QDeclarativeContext_context=None): # real signature unknown; restored from __doc__
        """ QDeclarativeComponent.create(QDeclarativeContext context=None) -> QObject """
        pass

    def creationContext(self): # real signature unknown; restored from __doc__
        """ QDeclarativeComponent.creationContext() -> QDeclarativeContext """
        return QDeclarativeContext

    def errors(self): # real signature unknown; restored from __doc__
        """ QDeclarativeComponent.errors() -> list-of-QDeclarativeError """
        pass

    def isError(self): # real signature unknown; restored from __doc__
        """ QDeclarativeComponent.isError() -> bool """
        return False

    def isLoading(self): # real signature unknown; restored from __doc__
        """ QDeclarativeComponent.isLoading() -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ QDeclarativeComponent.isNull() -> bool """
        return False

    def isReady(self): # real signature unknown; restored from __doc__
        """ QDeclarativeComponent.isReady() -> bool """
        return False

    def loadUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ QDeclarativeComponent.loadUrl(QUrl) """
        pass

    def progress(self): # real signature unknown; restored from __doc__
        """ QDeclarativeComponent.progress() -> float """
        return 0.0

    def progressChanged(self, *args, **kwargs): # real signature unknown
        """ QDeclarativeComponent.progressChanged[float] [signal] """
        pass

    def setData(self, QByteArray, QUrl): # real signature unknown; restored from __doc__
        """ QDeclarativeComponent.setData(QByteArray, QUrl) """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ QDeclarativeComponent.status() -> QDeclarativeComponent.Status """
        pass

    def statusChanged(self, *args, **kwargs): # real signature unknown
        """ QDeclarativeComponent.statusChanged[QDeclarativeComponent.Status] [signal] """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ QDeclarativeComponent.url() -> QUrl """
        pass

    def __init__(self, QDeclarativeEngine, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Error = 3
    Loading = 2
    Null = 0
    Ready = 1
    Status = None # (!) real value is ''


class QDeclarativeContext(__PyQt4_QtCore.QObject):
    """
    QDeclarativeContext(QDeclarativeEngine, QObject parent=None)
    QDeclarativeContext(QDeclarativeContext, QObject parent=None)
    """
    def baseUrl(self): # real signature unknown; restored from __doc__
        """ QDeclarativeContext.baseUrl() -> QUrl """
        pass

    def contextObject(self): # real signature unknown; restored from __doc__
        """ QDeclarativeContext.contextObject() -> QObject """
        pass

    def contextProperty(self, p_str): # real signature unknown; restored from __doc__
        """ QDeclarativeContext.contextProperty(str) -> object """
        return object()

    def engine(self): # real signature unknown; restored from __doc__
        """ QDeclarativeContext.engine() -> QDeclarativeEngine """
        return QDeclarativeEngine

    def isValid(self): # real signature unknown; restored from __doc__
        """ QDeclarativeContext.isValid() -> bool """
        return False

    def parentContext(self): # real signature unknown; restored from __doc__
        """ QDeclarativeContext.parentContext() -> QDeclarativeContext """
        return QDeclarativeContext

    def resolvedUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ QDeclarativeContext.resolvedUrl(QUrl) -> QUrl """
        pass

    def setBaseUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ QDeclarativeContext.setBaseUrl(QUrl) """
        pass

    def setContextObject(self, QObject): # real signature unknown; restored from __doc__
        """ QDeclarativeContext.setContextObject(QObject) """
        pass

    def setContextProperty(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDeclarativeContext.setContextProperty(str, QObject)
        QDeclarativeContext.setContextProperty(str, object)
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QDeclarativeEngine(__PyQt4_QtCore.QObject):
    """ QDeclarativeEngine(QObject parent=None) """
    def addImageProvider(self, p_str, QDeclarativeImageProvider): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.addImageProvider(str, QDeclarativeImageProvider) """
        pass

    def addImportPath(self, p_str): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.addImportPath(str) """
        pass

    def addPluginPath(self, p_str): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.addPluginPath(str) """
        pass

    def baseUrl(self): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.baseUrl() -> QUrl """
        pass

    def clearComponentCache(self): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.clearComponentCache() """
        pass

    def contextForObject(self, QObject): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.contextForObject(QObject) -> QDeclarativeContext """
        return QDeclarativeContext

    def imageProvider(self, p_str): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.imageProvider(str) -> QDeclarativeImageProvider """
        return QDeclarativeImageProvider

    def importPathList(self): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.importPathList() -> list-of-str """
        pass

    def importPlugin(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.importPlugin(str, str) -> (bool, str) """
        pass

    def networkAccessManager(self): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.networkAccessManager() -> QNetworkAccessManager """
        pass

    def networkAccessManagerFactory(self): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.networkAccessManagerFactory() -> QDeclarativeNetworkAccessManagerFactory """
        return QDeclarativeNetworkAccessManagerFactory

    def objectOwnership(self, QObject): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.objectOwnership(QObject) -> QDeclarativeEngine.ObjectOwnership """
        pass

    def offlineStoragePath(self): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.offlineStoragePath() -> str """
        return ""

    def outputWarningsToStandardError(self): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.outputWarningsToStandardError() -> bool """
        return False

    def pluginPathList(self): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.pluginPathList() -> list-of-str """
        pass

    def quit(self, *args, **kwargs): # real signature unknown
        """ QDeclarativeEngine.quit [signal] """
        pass

    def removeImageProvider(self, p_str): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.removeImageProvider(str) """
        pass

    def rootContext(self): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.rootContext() -> QDeclarativeContext """
        return QDeclarativeContext

    def setBaseUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.setBaseUrl(QUrl) """
        pass

    def setContextForObject(self, QObject, QDeclarativeContext): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.setContextForObject(QObject, QDeclarativeContext) """
        pass

    def setImportPathList(self, list_of_str): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.setImportPathList(list-of-str) """
        pass

    def setNetworkAccessManagerFactory(self, QDeclarativeNetworkAccessManagerFactory): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.setNetworkAccessManagerFactory(QDeclarativeNetworkAccessManagerFactory) """
        pass

    def setObjectOwnership(self, QObject, QDeclarativeEngine_ObjectOwnership): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.setObjectOwnership(QObject, QDeclarativeEngine.ObjectOwnership) """
        pass

    def setOfflineStoragePath(self, p_str): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.setOfflineStoragePath(str) """
        pass

    def setOutputWarningsToStandardError(self, bool): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.setOutputWarningsToStandardError(bool) """
        pass

    def setPluginPathList(self, list_of_str): # real signature unknown; restored from __doc__
        """ QDeclarativeEngine.setPluginPathList(list-of-str) """
        pass

    def warnings(self, *args, **kwargs): # real signature unknown
        """ QDeclarativeEngine.warnings[list-of-QDeclarativeError] [signal] """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    CppOwnership = 0
    JavaScriptOwnership = 1
    ObjectOwnership = None # (!) real value is ''


class QDeclarativeError(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDeclarativeError()
    QDeclarativeError(QDeclarativeError)
    """
    def column(self): # real signature unknown; restored from __doc__
        """ QDeclarativeError.column() -> int """
        return 0

    def description(self): # real signature unknown; restored from __doc__
        """ QDeclarativeError.description() -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ QDeclarativeError.isValid() -> bool """
        return False

    def line(self): # real signature unknown; restored from __doc__
        """ QDeclarativeError.line() -> int """
        return 0

    def setColumn(self, p_int): # real signature unknown; restored from __doc__
        """ QDeclarativeError.setColumn(int) """
        pass

    def setDescription(self, p_str): # real signature unknown; restored from __doc__
        """ QDeclarativeError.setDescription(str) """
        pass

    def setLine(self, p_int): # real signature unknown; restored from __doc__
        """ QDeclarativeError.setLine(int) """
        pass

    def setUrl(self, QUrl): # real signature unknown; restored from __doc__
        """ QDeclarativeError.setUrl(QUrl) """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ QDeclarativeError.toString() -> str """
        return ""

    def url(self): # real signature unknown; restored from __doc__
        """ QDeclarativeError.url() -> QUrl """
        pass

    def __init__(self, QDeclarativeError=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDeclarativeExpression(__PyQt4_QtCore.QObject):
    """
    QDeclarativeExpression()
    QDeclarativeExpression(QDeclarativeContext, QObject, str, QObject parent=None)
    """
    def clearError(self): # real signature unknown; restored from __doc__
        """ QDeclarativeExpression.clearError() """
        pass

    def context(self): # real signature unknown; restored from __doc__
        """ QDeclarativeExpression.context() -> QDeclarativeContext """
        return QDeclarativeContext

    def engine(self): # real signature unknown; restored from __doc__
        """ QDeclarativeExpression.engine() -> QDeclarativeEngine """
        return QDeclarativeEngine

    def error(self): # real signature unknown; restored from __doc__
        """ QDeclarativeExpression.error() -> QDeclarativeError """
        return QDeclarativeError

    def evaluate(self): # real signature unknown; restored from __doc__
        """ QDeclarativeExpression.evaluate() -> (object, bool) """
        pass

    def expression(self): # real signature unknown; restored from __doc__
        """ QDeclarativeExpression.expression() -> str """
        return ""

    def hasError(self): # real signature unknown; restored from __doc__
        """ QDeclarativeExpression.hasError() -> bool """
        return False

    def lineNumber(self): # real signature unknown; restored from __doc__
        """ QDeclarativeExpression.lineNumber() -> int """
        return 0

    def notifyOnValueChanged(self): # real signature unknown; restored from __doc__
        """ QDeclarativeExpression.notifyOnValueChanged() -> bool """
        return False

    def scopeObject(self): # real signature unknown; restored from __doc__
        """ QDeclarativeExpression.scopeObject() -> QObject """
        pass

    def setExpression(self, p_str): # real signature unknown; restored from __doc__
        """ QDeclarativeExpression.setExpression(str) """
        pass

    def setNotifyOnValueChanged(self, bool): # real signature unknown; restored from __doc__
        """ QDeclarativeExpression.setNotifyOnValueChanged(bool) """
        pass

    def setSourceLocation(self, p_str, p_int): # real signature unknown; restored from __doc__
        """ QDeclarativeExpression.setSourceLocation(str, int) """
        pass

    def sourceFile(self): # real signature unknown; restored from __doc__
        """ QDeclarativeExpression.sourceFile() -> str """
        return ""

    def valueChanged(self, *args, **kwargs): # real signature unknown
        """ QDeclarativeExpression.valueChanged [signal] """
        pass

    def __init__(self, QDeclarativeContext=None, QObject=None, p_str=None, QObject_parent=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QDeclarativeExtensionPlugin(__PyQt4_QtCore.QObject):
    """ QDeclarativeExtensionPlugin(QObject parent=None) """
    def initializeEngine(self, QDeclarativeEngine, p_str): # real signature unknown; restored from __doc__
        """ QDeclarativeExtensionPlugin.initializeEngine(QDeclarativeEngine, str) """
        pass

    def registerTypes(self, p_str): # real signature unknown; restored from __doc__
        """ QDeclarativeExtensionPlugin.registerTypes(str) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


class QDeclarativeImageProvider(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDeclarativeImageProvider(QDeclarativeImageProvider.ImageType)
    QDeclarativeImageProvider(QDeclarativeImageProvider)
    """
    def imageType(self): # real signature unknown; restored from __doc__
        """ QDeclarativeImageProvider.imageType() -> QDeclarativeImageProvider.ImageType """
        pass

    def requestImage(self, p_str, QSize, QSize_1): # real signature unknown; restored from __doc__
        """ QDeclarativeImageProvider.requestImage(str, QSize, QSize) -> QImage """
        pass

    def requestPixmap(self, p_str, QSize, QSize_1): # real signature unknown; restored from __doc__
        """ QDeclarativeImageProvider.requestPixmap(str, QSize, QSize) -> QPixmap """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Image = 0
    ImageType = None # (!) real value is ''
    Pixmap = 1


class QDeclarativeParserStatus(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDeclarativeParserStatus()
    QDeclarativeParserStatus(QDeclarativeParserStatus)
    """
    def classBegin(self): # real signature unknown; restored from __doc__
        """ QDeclarativeParserStatus.classBegin() """
        pass

    def componentComplete(self): # real signature unknown; restored from __doc__
        """ QDeclarativeParserStatus.componentComplete() """
        pass

    def __init__(self, QDeclarativeParserStatus=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



from .QDeclarativeParserStatus import QDeclarativeParserStatus

class QDeclarativeItem(__PyQt4_QtGui.QGraphicsObject, QDeclarativeParserStatus):
    """ QDeclarativeItem(QDeclarativeItem parent=None) """
    def baselineOffset(self): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.baselineOffset() -> float """
        return 0.0

    def boundingRect(self): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.boundingRect() -> QRectF """
        pass

    def childrenRect(self): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.childrenRect() -> QRectF """
        pass

    def classBegin(self): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.classBegin() """
        pass

    def clip(self): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.clip() -> bool """
        return False

    def componentComplete(self): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.componentComplete() """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.event(QEvent) -> bool """
        return False

    def geometryChanged(self, QRectF, QRectF_1): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.geometryChanged(QRectF, QRectF) """
        pass

    def hasFocus(self): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.hasFocus() -> bool """
        return False

    def heightValid(self): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.heightValid() -> bool """
        return False

    def implicitHeight(self): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.implicitHeight() -> float """
        return 0.0

    def implicitWidth(self): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.implicitWidth() -> float """
        return 0.0

    def inputMethodEvent(self, QInputMethodEvent): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.inputMethodEvent(QInputMethodEvent) """
        pass

    def inputMethodQuery(self, Qt_InputMethodQuery): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.inputMethodQuery(Qt.InputMethodQuery) -> object """
        return object()

    def isComponentComplete(self): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.isComponentComplete() -> bool """
        return False

    def itemChange(self, QGraphicsItem_GraphicsItemChange, p_object): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.itemChange(QGraphicsItem.GraphicsItemChange, object) -> object """
        return object()

    def keepMouseGrab(self): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.keepMouseGrab() -> bool """
        return False

    def keyPressEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.keyPressEvent(QKeyEvent) """
        pass

    def keyReleaseEvent(self, QKeyEvent): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.keyReleaseEvent(QKeyEvent) """
        pass

    def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.paint(QPainter, QStyleOptionGraphicsItem, QWidget) """
        pass

    def parentItem(self): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.parentItem() -> QDeclarativeItem """
        return QDeclarativeItem

    def sceneEvent(self, QEvent): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.sceneEvent(QEvent) -> bool """
        return False

    def setBaselineOffset(self, p_float): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.setBaselineOffset(float) """
        pass

    def setClip(self, bool): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.setClip(bool) """
        pass

    def setHeight(self, p_float): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.setHeight(float) """
        pass

    def setImplicitHeight(self, p_float): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.setImplicitHeight(float) """
        pass

    def setImplicitWidth(self, p_float): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.setImplicitWidth(float) """
        pass

    def setKeepMouseGrab(self, bool): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.setKeepMouseGrab(bool) """
        pass

    def setParentItem(self, QDeclarativeItem): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.setParentItem(QDeclarativeItem) """
        pass

    def setSmooth(self, bool): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.setSmooth(bool) """
        pass

    def setTransformOrigin(self, QDeclarativeItem_TransformOrigin): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.setTransformOrigin(QDeclarativeItem.TransformOrigin) """
        pass

    def setWidth(self, p_float): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.setWidth(float) """
        pass

    def smooth(self): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.smooth() -> bool """
        return False

    def transformOrigin(self): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.transformOrigin() -> QDeclarativeItem.TransformOrigin """
        pass

    def widthValid(self): # real signature unknown; restored from __doc__
        """ QDeclarativeItem.widthValid() -> bool """
        return False

    def __init__(self, QDeclarativeItem_parent=None): # real signature unknown; restored from __doc__
        pass

    Bottom = 7
    BottomLeft = 6
    BottomRight = 8
    Center = 4
    Left = 3
    Right = 5
    Top = 1
    TopLeft = 0
    TopRight = 2
    TransformOrigin = None # (!) real value is ''


class QDeclarativeListReference(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDeclarativeListReference()
    QDeclarativeListReference(QObject, str, QDeclarativeEngine engine=None)
    QDeclarativeListReference(QDeclarativeListReference)
    """
    def append(self, QObject): # real signature unknown; restored from __doc__
        """ QDeclarativeListReference.append(QObject) -> bool """
        return False

    def at(self, p_int): # real signature unknown; restored from __doc__
        """ QDeclarativeListReference.at(int) -> QObject """
        pass

    def canAppend(self): # real signature unknown; restored from __doc__
        """ QDeclarativeListReference.canAppend() -> bool """
        return False

    def canAt(self): # real signature unknown; restored from __doc__
        """ QDeclarativeListReference.canAt() -> bool """
        return False

    def canClear(self): # real signature unknown; restored from __doc__
        """ QDeclarativeListReference.canClear() -> bool """
        return False

    def canCount(self): # real signature unknown; restored from __doc__
        """ QDeclarativeListReference.canCount() -> bool """
        return False

    def clear(self): # real signature unknown; restored from __doc__
        """ QDeclarativeListReference.clear() -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """ QDeclarativeListReference.count() -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ QDeclarativeListReference.isValid() -> bool """
        return False

    def listElementType(self): # real signature unknown; restored from __doc__
        """ QDeclarativeListReference.listElementType() -> QMetaObject """
        pass

    def object(self): # real signature unknown; restored from __doc__
        """ QDeclarativeListReference.object() -> QObject """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDeclarativeNetworkAccessManagerFactory(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDeclarativeNetworkAccessManagerFactory()
    QDeclarativeNetworkAccessManagerFactory(QDeclarativeNetworkAccessManagerFactory)
    """
    def create(self, QObject): # real signature unknown; restored from __doc__
        """ QDeclarativeNetworkAccessManagerFactory.create(QObject) -> QNetworkAccessManager """
        pass

    def __init__(self, QDeclarativeNetworkAccessManagerFactory=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDeclarativeProperty(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDeclarativeProperty()
    QDeclarativeProperty(QObject)
    QDeclarativeProperty(QObject, QDeclarativeContext)
    QDeclarativeProperty(QObject, QDeclarativeEngine)
    QDeclarativeProperty(QObject, str)
    QDeclarativeProperty(QObject, str, QDeclarativeContext)
    QDeclarativeProperty(QObject, str, QDeclarativeEngine)
    QDeclarativeProperty(QDeclarativeProperty)
    """
    def connectNotifySignal(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDeclarativeProperty.connectNotifySignal(QObject, SLOT()) -> bool
        QDeclarativeProperty.connectNotifySignal(callable) -> bool
        QDeclarativeProperty.connectNotifySignal(QObject, int) -> bool
        """
        return False

    def hasNotifySignal(self): # real signature unknown; restored from __doc__
        """ QDeclarativeProperty.hasNotifySignal() -> bool """
        return False

    def index(self): # real signature unknown; restored from __doc__
        """ QDeclarativeProperty.index() -> int """
        return 0

    def isDesignable(self): # real signature unknown; restored from __doc__
        """ QDeclarativeProperty.isDesignable() -> bool """
        return False

    def isProperty(self): # real signature unknown; restored from __doc__
        """ QDeclarativeProperty.isProperty() -> bool """
        return False

    def isResettable(self): # real signature unknown; restored from __doc__
        """ QDeclarativeProperty.isResettable() -> bool """
        return False

    def isSignalProperty(self): # real signature unknown; restored from __doc__
        """ QDeclarativeProperty.isSignalProperty() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QDeclarativeProperty.isValid() -> bool """
        return False

    def isWritable(self): # real signature unknown; restored from __doc__
        """ QDeclarativeProperty.isWritable() -> bool """
        return False

    def method(self): # real signature unknown; restored from __doc__
        """ QDeclarativeProperty.method() -> QMetaMethod """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ QDeclarativeProperty.name() -> str """
        return ""

    def needsNotifySignal(self): # real signature unknown; restored from __doc__
        """ QDeclarativeProperty.needsNotifySignal() -> bool """
        return False

    def object(self): # real signature unknown; restored from __doc__
        """ QDeclarativeProperty.object() -> QObject """
        pass

    def property(self): # real signature unknown; restored from __doc__
        """ QDeclarativeProperty.property() -> QMetaProperty """
        pass

    def propertyType(self): # real signature unknown; restored from __doc__
        """ QDeclarativeProperty.propertyType() -> int """
        return 0

    def propertyTypeCategory(self): # real signature unknown; restored from __doc__
        """ QDeclarativeProperty.propertyTypeCategory() -> QDeclarativeProperty.PropertyTypeCategory """
        pass

    def propertyTypeName(self): # real signature unknown; restored from __doc__
        """ QDeclarativeProperty.propertyTypeName() -> str """
        return ""

    def read(self, QObject=None, p_str=None, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDeclarativeProperty.read() -> object
        QDeclarativeProperty.read(QObject, str) -> object
        QDeclarativeProperty.read(QObject, str, QDeclarativeContext) -> object
        QDeclarativeProperty.read(QObject, str, QDeclarativeEngine) -> object
        """
        return object()

    def reset(self): # real signature unknown; restored from __doc__
        """ QDeclarativeProperty.reset() -> bool """
        return False

    def type(self): # real signature unknown; restored from __doc__
        """ QDeclarativeProperty.type() -> QDeclarativeProperty.Type """
        pass

    def write(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDeclarativeProperty.write(object) -> bool
        QDeclarativeProperty.write(QObject, str, object) -> bool
        QDeclarativeProperty.write(QObject, str, object, QDeclarativeContext) -> bool
        QDeclarativeProperty.write(QObject, str, object, QDeclarativeEngine) -> bool
        """
        return False

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


    Invalid = 0
    InvalidCategory = 0
    List = 1
    Normal = 3
    Object = 2
    Property = 1
    PropertyTypeCategory = None # (!) real value is ''
    SignalProperty = 2
    Type = None # (!) real value is ''


class QDeclarativePropertyMap(__PyQt4_QtCore.QObject):
    """ QDeclarativePropertyMap(QObject parent=None) """
    def clear(self, p_str): # real signature unknown; restored from __doc__
        """ QDeclarativePropertyMap.clear(str) """
        pass

    def contains(self, p_str): # real signature unknown; restored from __doc__
        """ QDeclarativePropertyMap.contains(str) -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """ QDeclarativePropertyMap.count() -> int """
        return 0

    def insert(self, p_str, p_object): # real signature unknown; restored from __doc__
        """ QDeclarativePropertyMap.insert(str, object) """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QDeclarativePropertyMap.isEmpty() -> bool """
        return False

    def keys(self): # real signature unknown; restored from __doc__
        """ QDeclarativePropertyMap.keys() -> list-of-str """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ QDeclarativePropertyMap.size() -> int """
        return 0

    def value(self, p_str): # real signature unknown; restored from __doc__
        """ QDeclarativePropertyMap.value(str) -> object """
        return object()

    def valueChanged(self, *args, **kwargs): # real signature unknown
        """ QDeclarativePropertyMap.valueChanged[str, object] [signal] """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass


class QDeclarativePropertyValueSource(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDeclarativePropertyValueSource()
    QDeclarativePropertyValueSource(QDeclarativePropertyValueSource)
    """
    def setTarget(self, QDeclarativeProperty): # real signature unknown; restored from __doc__
        """ QDeclarativePropertyValueSource.setTarget(QDeclarativeProperty) """
        pass

    def __init__(self, QDeclarativePropertyValueSource=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDeclarativeScriptString(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDeclarativeScriptString()
    QDeclarativeScriptString(QDeclarativeScriptString)
    """
    def context(self): # real signature unknown; restored from __doc__
        """ QDeclarativeScriptString.context() -> QDeclarativeContext """
        return QDeclarativeContext

    def scopeObject(self): # real signature unknown; restored from __doc__
        """ QDeclarativeScriptString.scopeObject() -> QObject """
        pass

    def script(self): # real signature unknown; restored from __doc__
        """ QDeclarativeScriptString.script() -> str """
        return ""

    def setContext(self, QDeclarativeContext): # real signature unknown; restored from __doc__
        """ QDeclarativeScriptString.setContext(QDeclarativeContext) """
        pass

    def setScopeObject(self, QObject): # real signature unknown; restored from __doc__
        """ QDeclarativeScriptString.setScopeObject(QObject) """
        pass

    def setScript(self, p_str): # real signature unknown; restored from __doc__
        """ QDeclarativeScriptString.setScript(str) """
        pass

    def __init__(self, QDeclarativeScriptString=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QDeclarativeView(__PyQt4_QtGui.QGraphicsView):
    """
    QDeclarativeView(QWidget parent=None)
    QDeclarativeView(QUrl, QWidget parent=None)
    """
    def engine(self): # real signature unknown; restored from __doc__
        """ QDeclarativeView.engine() -> QDeclarativeEngine """
        return QDeclarativeEngine

    def errors(self): # real signature unknown; restored from __doc__
        """ QDeclarativeView.errors() -> list-of-QDeclarativeError """
        pass

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QDeclarativeView.eventFilter(QObject, QEvent) -> bool """
        return False

    def initialSize(self): # real signature unknown; restored from __doc__
        """ QDeclarativeView.initialSize() -> QSize """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QDeclarativeView.paintEvent(QPaintEvent) """
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QDeclarativeView.resizeEvent(QResizeEvent) """
        pass

    def resizeMode(self): # real signature unknown; restored from __doc__
        """ QDeclarativeView.resizeMode() -> QDeclarativeView.ResizeMode """
        pass

    def rootContext(self): # real signature unknown; restored from __doc__
        """ QDeclarativeView.rootContext() -> QDeclarativeContext """
        return QDeclarativeContext

    def rootObject(self): # real signature unknown; restored from __doc__
        """ QDeclarativeView.rootObject() -> QGraphicsObject """
        pass

    def sceneResized(self, *args, **kwargs): # real signature unknown
        """ QDeclarativeView.sceneResized[QSize] [signal] """
        pass

    def setResizeMode(self, QDeclarativeView_ResizeMode): # real signature unknown; restored from __doc__
        """ QDeclarativeView.setResizeMode(QDeclarativeView.ResizeMode) """
        pass

    def setSource(self, QUrl): # real signature unknown; restored from __doc__
        """ QDeclarativeView.setSource(QUrl) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QDeclarativeView.sizeHint() -> QSize """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ QDeclarativeView.source() -> QUrl """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ QDeclarativeView.status() -> QDeclarativeView.Status """
        pass

    def statusChanged(self, *args, **kwargs): # real signature unknown
        """ QDeclarativeView.statusChanged[QDeclarativeView.Status] [signal] """
        pass

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ QDeclarativeView.timerEvent(QTimerEvent) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Error = 3
    Loading = 2
    Null = 0
    Ready = 1
    ResizeMode = None # (!) real value is ''
    SizeRootObjectToView = 1
    SizeViewToRootObject = 0
    Status = None # (!) real value is ''


from .QDeclarativePropertyValueSource import QDeclarativePropertyValueSource

class QPyDeclarativePropertyValueSource(__PyQt4_QtCore.QObject, QDeclarativePropertyValueSource):
    """ QPyDeclarativePropertyValueSource(QObject parent=None) """
    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

