# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


from .QObject import QObject

class QCoreApplication(QObject):
    """ QCoreApplication(list-of-str) """
    def aboutToQuit(self, *args, **kwargs): # real signature unknown
        """ QCoreApplication.aboutToQuit [signal] """
        pass

    def addLibraryPath(self, p_str): # real signature unknown; restored from __doc__
        """ QCoreApplication.addLibraryPath(str) """
        pass

    def applicationDirPath(self): # real signature unknown; restored from __doc__
        """ QCoreApplication.applicationDirPath() -> str """
        return ""

    def applicationFilePath(self): # real signature unknown; restored from __doc__
        """ QCoreApplication.applicationFilePath() -> str """
        return ""

    def applicationName(self): # real signature unknown; restored from __doc__
        """ QCoreApplication.applicationName() -> str """
        return ""

    def applicationPid(self): # real signature unknown; restored from __doc__
        """ QCoreApplication.applicationPid() -> int """
        return 0

    def applicationVersion(self): # real signature unknown; restored from __doc__
        """ QCoreApplication.applicationVersion() -> str """
        return ""

    def argc(self): # real signature unknown; restored from __doc__
        """ QCoreApplication.argc() -> int """
        return 0

    def arguments(self): # real signature unknown; restored from __doc__
        """ QCoreApplication.arguments() -> list-of-str """
        pass

    def argv(self): # real signature unknown; restored from __doc__
        """ QCoreApplication.argv() -> list-of-str """
        pass

    def closingDown(self): # real signature unknown; restored from __doc__
        """ QCoreApplication.closingDown() -> bool """
        return False

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QCoreApplication.event(QEvent) -> bool """
        return False

    def exec(self): # real signature unknown; restored from __doc__
        """ QCoreApplication.exec() -> int """
        return 0

    def exec_(self): # real signature unknown; restored from __doc__
        """ QCoreApplication.exec_() -> int """
        return 0

    def exit(self, int_returnCode=0): # real signature unknown; restored from __doc__
        """ QCoreApplication.exit(int returnCode=0) """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ QCoreApplication.flush() """
        pass

    def hasPendingEvents(self): # real signature unknown; restored from __doc__
        """ QCoreApplication.hasPendingEvents() -> bool """
        return False

    def installTranslator(self, QTranslator): # real signature unknown; restored from __doc__
        """ QCoreApplication.installTranslator(QTranslator) """
        pass

    def instance(self): # real signature unknown; restored from __doc__
        """ QCoreApplication.instance() -> QCoreApplication """
        return QCoreApplication

    def libraryPaths(self): # real signature unknown; restored from __doc__
        """ QCoreApplication.libraryPaths() -> list-of-str """
        pass

    def notify(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QCoreApplication.notify(QObject, QEvent) -> bool """
        return False

    def organizationDomain(self): # real signature unknown; restored from __doc__
        """ QCoreApplication.organizationDomain() -> str """
        return ""

    def organizationName(self): # real signature unknown; restored from __doc__
        """ QCoreApplication.organizationName() -> str """
        return ""

    def postEvent(self, QObject, QEvent, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QCoreApplication.postEvent(QObject, QEvent)
        QCoreApplication.postEvent(QObject, QEvent, int)
        """
        pass

    def processEvents(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QCoreApplication.processEvents(QEventLoop.ProcessEventsFlags flags=QEventLoop.AllEvents)
        QCoreApplication.processEvents(QEventLoop.ProcessEventsFlags, int)
        """
        pass

    def quit(self): # real signature unknown; restored from __doc__
        """ QCoreApplication.quit() """
        pass

    def removeLibraryPath(self, p_str): # real signature unknown; restored from __doc__
        """ QCoreApplication.removeLibraryPath(str) """
        pass

    def removePostedEvents(self, QObject, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QCoreApplication.removePostedEvents(QObject)
        QCoreApplication.removePostedEvents(QObject, int)
        """
        pass

    def removeTranslator(self, QTranslator): # real signature unknown; restored from __doc__
        """ QCoreApplication.removeTranslator(QTranslator) """
        pass

    def sendEvent(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QCoreApplication.sendEvent(QObject, QEvent) -> bool """
        return False

    def sendPostedEvents(self, QObject=None, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QCoreApplication.sendPostedEvents(QObject, int)
        QCoreApplication.sendPostedEvents()
        """
        pass

    def setApplicationName(self, p_str): # real signature unknown; restored from __doc__
        """ QCoreApplication.setApplicationName(str) """
        pass

    def setApplicationVersion(self, p_str): # real signature unknown; restored from __doc__
        """ QCoreApplication.setApplicationVersion(str) """
        pass

    def setAttribute(self, Qt_ApplicationAttribute, bool_on=True): # real signature unknown; restored from __doc__
        """ QCoreApplication.setAttribute(Qt.ApplicationAttribute, bool on=True) """
        pass

    def setLibraryPaths(self, list_of_str): # real signature unknown; restored from __doc__
        """ QCoreApplication.setLibraryPaths(list-of-str) """
        pass

    def setOrganizationDomain(self, p_str): # real signature unknown; restored from __doc__
        """ QCoreApplication.setOrganizationDomain(str) """
        pass

    def setOrganizationName(self, p_str): # real signature unknown; restored from __doc__
        """ QCoreApplication.setOrganizationName(str) """
        pass

    def startingUp(self): # real signature unknown; restored from __doc__
        """ QCoreApplication.startingUp() -> bool """
        return False

    def testAttribute(self, Qt_ApplicationAttribute): # real signature unknown; restored from __doc__
        """ QCoreApplication.testAttribute(Qt.ApplicationAttribute) -> bool """
        return False

    def translate(self, p_str, p_str_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QCoreApplication.translate(str, str, str disambiguation=None, QCoreApplication.Encoding encoding=QCoreApplication.CodecForTr) -> str
        QCoreApplication.translate(str, str, str, QCoreApplication.Encoding, int) -> str
        """
        return ""

    def __init__(self, list_of_str): # real signature unknown; restored from __doc__
        pass

    CodecForTr = 0
    DefaultCodec = 0
    Encoding = None # (!) real value is ''
    UnicodeUTF8 = 1


