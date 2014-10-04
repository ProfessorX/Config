# encoding: utf-8
# module PyKDE4.kutils
# from /usr/lib/python2.7/dist-packages/PyKDE4/kutils.so
# by generator 1.135
# no doc

# imports
import PyKDE4.kdeui as __PyKDE4_kdeui
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


# no functions
# classes

class KCModuleInfo(): # skipped bases: <type 'sip.wrapper'>
    # no doc
    def comment(self, *args, **kwargs): # real signature unknown
        pass

    def docPath(self, *args, **kwargs): # real signature unknown
        pass

    def fileName(self, *args, **kwargs): # real signature unknown
        pass

    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def icon(self, *args, **kwargs): # real signature unknown
        pass

    def keywords(self, *args, **kwargs): # real signature unknown
        pass

    def library(self, *args, **kwargs): # real signature unknown
        pass

    def moduleName(self, *args, **kwargs): # real signature unknown
        pass

    def service(self, *args, **kwargs): # real signature unknown
        pass

    def weight(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class KCModuleLoader(): # skipped bases: <type 'sip.wrapper'>
    # no doc
    def loadModule(self, *args, **kwargs): # real signature unknown
        pass

    def reportError(self, *args, **kwargs): # real signature unknown
        pass

    def showLastLoaderError(self, *args, **kwargs): # real signature unknown
        pass

    def unloadModule(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Both = 3
    Dialog = 2
    ErrorReporting = None # (!) real value is ''
    Inline = 1
    None = 0


class KCModuleProxy(__PyQt4_QtGui.QWidget):
    # no doc
    def aboutData(self, *args, **kwargs): # real signature unknown
        pass

    def buttons(self, *args, **kwargs): # real signature unknown
        pass

    def changed(self, *args, **kwargs): # real signature unknown
        pass

    def childClosed(self, *args, **kwargs): # real signature unknown
        pass

    def componentData(self, *args, **kwargs): # real signature unknown
        pass

    def dbusPath(self, *args, **kwargs): # real signature unknown
        pass

    def dbusService(self, *args, **kwargs): # real signature unknown
        pass

    def defaults(self, *args, **kwargs): # real signature unknown
        pass

    def deleteClient(self, *args, **kwargs): # real signature unknown
        pass

    def load(self, *args, **kwargs): # real signature unknown
        pass

    def minimumSizeHint(self, *args, **kwargs): # real signature unknown
        pass

    def moduleInfo(self, *args, **kwargs): # real signature unknown
        pass

    def quickHelp(self, *args, **kwargs): # real signature unknown
        pass

    def quickHelpChanged(self, *args, **kwargs): # real signature unknown
        pass

    def realModule(self, *args, **kwargs): # real signature unknown
        pass

    def rootOnlyMessage(self, *args, **kwargs): # real signature unknown
        pass

    def save(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def useRootOnlyMessage(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class KCMultiDialog(__PyKDE4_kdeui.KPageDialog):
    # no doc
    def addModule(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def configCommitted(self, *args, **kwargs): # real signature unknown
        pass

    def setButtons(self, *args, **kwargs): # real signature unknown
        pass

    def slotApplyClicked(self, *args, **kwargs): # real signature unknown
        pass

    def slotDefaultClicked(self, *args, **kwargs): # real signature unknown
        pass

    def slotHelpClicked(self, *args, **kwargs): # real signature unknown
        pass

    def slotOkClicked(self, *args, **kwargs): # real signature unknown
        pass

    def slotUser1Clicked(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class KEmoticons(__PyQt4_QtCore.QObject):
    # no doc
    def currentThemeName(self, *args, **kwargs): # real signature unknown
        pass

    def installTheme(self, *args, **kwargs): # real signature unknown
        pass

    def newTheme(self, *args, **kwargs): # real signature unknown
        pass

    def parseMode(self, *args, **kwargs): # real signature unknown
        pass

    def setParseMode(self, *args, **kwargs): # real signature unknown
        pass

    def setTheme(self, *args, **kwargs): # real signature unknown
        pass

    def theme(self, *args, **kwargs): # real signature unknown
        pass

    def themeList(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class KEmoticonsProvider(__PyQt4_QtCore.QObject):
    # no doc
    def addEmoticon(self, *args, **kwargs): # real signature unknown
        pass

    def addEmoticonIndex(self, *args, **kwargs): # real signature unknown
        pass

    def addEmoticonsMap(self, *args, **kwargs): # real signature unknown
        pass

    def clearEmoticonsMap(self, *args, **kwargs): # real signature unknown
        pass

    def createNew(self, *args, **kwargs): # real signature unknown
        pass

    def emoticonsMap(self, *args, **kwargs): # real signature unknown
        pass

    def fileName(self, *args, **kwargs): # real signature unknown
        pass

    def loadTheme(self, *args, **kwargs): # real signature unknown
        pass

    def removeEmoticon(self, *args, **kwargs): # real signature unknown
        pass

    def removeEmoticonIndex(self, *args, **kwargs): # real signature unknown
        pass

    def removeEmoticonsMap(self, *args, **kwargs): # real signature unknown
        pass

    def save(self, *args, **kwargs): # real signature unknown
        pass

    def setThemeName(self, *args, **kwargs): # real signature unknown
        pass

    def themeName(self, *args, **kwargs): # real signature unknown
        pass

    def themePath(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AddEmoticonOption = None # (!) real value is ''
    Copy = 1
    DoNotCopy = 0
    Emoticon = None # (!) real value is ''


class KEmoticonsTheme(): # skipped bases: <type 'sip.wrapper'>
    # no doc
    def addEmoticon(self, *args, **kwargs): # real signature unknown
        pass

    def createNew(self, *args, **kwargs): # real signature unknown
        pass

    def emoticonsMap(self, *args, **kwargs): # real signature unknown
        pass

    def fileName(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def loadTheme(self, *args, **kwargs): # real signature unknown
        pass

    def parseEmoticons(self, *args, **kwargs): # real signature unknown
        pass

    def removeEmoticon(self, *args, **kwargs): # real signature unknown
        pass

    def save(self, *args, **kwargs): # real signature unknown
        pass

    def setThemeName(self, *args, **kwargs): # real signature unknown
        pass

    def themeName(self, *args, **kwargs): # real signature unknown
        pass

    def themePath(self, *args, **kwargs): # real signature unknown
        pass

    def tokenize(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DefaultParse = 0
    Image = 1
    ParseMode = None # (!) real value is ''
    ParseModeEnum = None # (!) real value is ''
    RelaxedParse = 2
    SkipHTML = 4
    StrictParse = 1
    Text = 2
    Token = None # (!) real value is ''
    TokenType = None # (!) real value is ''
    Undefined = 0


class KIdleTime(__PyQt4_QtCore.QObject):
    # no doc
    def addIdleTimeout(self, *args, **kwargs): # real signature unknown
        pass

    def catchNextResumeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def idleTime(self, *args, **kwargs): # real signature unknown
        pass

    def idleTimeouts(self, *args, **kwargs): # real signature unknown
        pass

    def instance(self, *args, **kwargs): # real signature unknown
        pass

    def removeAllIdleTimeouts(self, *args, **kwargs): # real signature unknown
        pass

    def removeIdleTimeout(self, *args, **kwargs): # real signature unknown
        pass

    def resumingFromIdle(self, *args, **kwargs): # real signature unknown
        pass

    def simulateUserActivity(self, *args, **kwargs): # real signature unknown
        pass

    def stopCatchingResumeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timeoutReached(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class KPluginSelector(__PyQt4_QtGui.QWidget):
    # no doc
    def addPlugins(self, *args, **kwargs): # real signature unknown
        pass

    def changed(self, *args, **kwargs): # real signature unknown
        pass

    def configCommitted(self, *args, **kwargs): # real signature unknown
        pass

    def defaults(self, *args, **kwargs): # real signature unknown
        pass

    def isDefault(self, *args, **kwargs): # real signature unknown
        pass

    def load(self, *args, **kwargs): # real signature unknown
        pass

    def save(self, *args, **kwargs): # real signature unknown
        pass

    def updatePluginsState(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    IgnoreConfigFile = 1
    PluginLoadMethod = None # (!) real value is ''
    ReadConfigFile = 0


class KPrintPreview(__PyKDE4_kdeui.KDialog):
    # no doc
    def isAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class KSettings(): # skipped bases: <type 'sip.wrapper'>
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Dialog = None # (!) real value is ''
    Dispatcher = None # (!) real value is ''
    PluginPage = None # (!) real value is ''


