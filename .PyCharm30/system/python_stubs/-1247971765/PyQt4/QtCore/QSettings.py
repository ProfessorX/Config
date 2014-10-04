# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


from .QObject import QObject

class QSettings(QObject):
    """
    QSettings(str, str application='', QObject parent=None)
    QSettings(QSettings.Scope, str, str application='', QObject parent=None)
    QSettings(QSettings.Format, QSettings.Scope, str, str application='', QObject parent=None)
    QSettings(str, QSettings.Format, QObject parent=None)
    QSettings(QObject parent=None)
    """
    def allKeys(self): # real signature unknown; restored from __doc__
        """ QSettings.allKeys() -> list-of-str """
        pass

    def applicationName(self): # real signature unknown; restored from __doc__
        """ QSettings.applicationName() -> str """
        return ""

    def beginGroup(self, p_str): # real signature unknown; restored from __doc__
        """ QSettings.beginGroup(str) """
        pass

    def beginReadArray(self, p_str): # real signature unknown; restored from __doc__
        """ QSettings.beginReadArray(str) -> int """
        return 0

    def beginWriteArray(self, p_str, int_size=-1): # real signature unknown; restored from __doc__
        """ QSettings.beginWriteArray(str, int size=-1) """
        pass

    def childGroups(self): # real signature unknown; restored from __doc__
        """ QSettings.childGroups() -> list-of-str """
        pass

    def childKeys(self): # real signature unknown; restored from __doc__
        """ QSettings.childKeys() -> list-of-str """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ QSettings.clear() """
        pass

    def contains(self, p_str): # real signature unknown; restored from __doc__
        """ QSettings.contains(str) -> bool """
        return False

    def defaultFormat(self): # real signature unknown; restored from __doc__
        """ QSettings.defaultFormat() -> QSettings.Format """
        pass

    def endArray(self): # real signature unknown; restored from __doc__
        """ QSettings.endArray() """
        pass

    def endGroup(self): # real signature unknown; restored from __doc__
        """ QSettings.endGroup() """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QSettings.event(QEvent) -> bool """
        return False

    def fallbacksEnabled(self): # real signature unknown; restored from __doc__
        """ QSettings.fallbacksEnabled() -> bool """
        return False

    def fileName(self): # real signature unknown; restored from __doc__
        """ QSettings.fileName() -> str """
        return ""

    def format(self): # real signature unknown; restored from __doc__
        """ QSettings.format() -> QSettings.Format """
        pass

    def group(self): # real signature unknown; restored from __doc__
        """ QSettings.group() -> str """
        return ""

    def iniCodec(self): # real signature unknown; restored from __doc__
        """ QSettings.iniCodec() -> QTextCodec """
        return QTextCodec

    def isWritable(self): # real signature unknown; restored from __doc__
        """ QSettings.isWritable() -> bool """
        return False

    def organizationName(self): # real signature unknown; restored from __doc__
        """ QSettings.organizationName() -> str """
        return ""

    def remove(self, p_str): # real signature unknown; restored from __doc__
        """ QSettings.remove(str) """
        pass

    def scope(self): # real signature unknown; restored from __doc__
        """ QSettings.scope() -> QSettings.Scope """
        pass

    def setArrayIndex(self, p_int): # real signature unknown; restored from __doc__
        """ QSettings.setArrayIndex(int) """
        pass

    def setDefaultFormat(self, QSettings_Format): # real signature unknown; restored from __doc__
        """ QSettings.setDefaultFormat(QSettings.Format) """
        pass

    def setFallbacksEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QSettings.setFallbacksEnabled(bool) """
        pass

    def setIniCodec(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSettings.setIniCodec(QTextCodec)
        QSettings.setIniCodec(str)
        """
        pass

    def setPath(self, QSettings_Format, QSettings_Scope, p_str): # real signature unknown; restored from __doc__
        """ QSettings.setPath(QSettings.Format, QSettings.Scope, str) """
        pass

    def setSystemIniPath(self, p_str): # real signature unknown; restored from __doc__
        """ QSettings.setSystemIniPath(str) """
        pass

    def setUserIniPath(self, p_str): # real signature unknown; restored from __doc__
        """ QSettings.setUserIniPath(str) """
        pass

    def setValue(self, p_str, p_object): # real signature unknown; restored from __doc__
        """ QSettings.setValue(str, object) """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ QSettings.status() -> QSettings.Status """
        pass

    def sync(self): # real signature unknown; restored from __doc__
        """ QSettings.sync() """
        pass

    def value(self, p_str, object_defaultValue=None, object_type=None): # real signature unknown; restored from __doc__
        """ QSettings.value(str, object defaultValue=None, object type=None) -> object """
        return object()

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AccessError = 1
    Format = None # (!) real value is ''
    FormatError = 2
    IniFormat = 1
    InvalidFormat = 16
    NativeFormat = 0
    NoError = 0
    Scope = None # (!) real value is ''
    Status = None # (!) real value is ''
    SystemScope = 1
    UserScope = 0


