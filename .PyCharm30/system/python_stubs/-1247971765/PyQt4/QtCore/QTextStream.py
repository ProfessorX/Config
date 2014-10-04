# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


class QTextStream(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QTextStream()
    QTextStream(QIODevice)
    QTextStream(QByteArray, QIODevice.OpenMode mode=QIODevice.ReadWrite)
    """
    def atEnd(self): # real signature unknown; restored from __doc__
        """ QTextStream.atEnd() -> bool """
        return False

    def autoDetectUnicode(self): # real signature unknown; restored from __doc__
        """ QTextStream.autoDetectUnicode() -> bool """
        return False

    def codec(self): # real signature unknown; restored from __doc__
        """ QTextStream.codec() -> QTextCodec """
        return QTextCodec

    def device(self): # real signature unknown; restored from __doc__
        """ QTextStream.device() -> QIODevice """
        return QIODevice

    def fieldAlignment(self): # real signature unknown; restored from __doc__
        """ QTextStream.fieldAlignment() -> QTextStream.FieldAlignment """
        pass

    def fieldWidth(self): # real signature unknown; restored from __doc__
        """ QTextStream.fieldWidth() -> int """
        return 0

    def flush(self): # real signature unknown; restored from __doc__
        """ QTextStream.flush() """
        pass

    def generateByteOrderMark(self): # real signature unknown; restored from __doc__
        """ QTextStream.generateByteOrderMark() -> bool """
        return False

    def integerBase(self): # real signature unknown; restored from __doc__
        """ QTextStream.integerBase() -> int """
        return 0

    def locale(self): # real signature unknown; restored from __doc__
        """ QTextStream.locale() -> QLocale """
        return QLocale

    def numberFlags(self): # real signature unknown; restored from __doc__
        """ QTextStream.numberFlags() -> QTextStream.NumberFlags """
        pass

    def padChar(self): # real signature unknown; restored from __doc__
        """ QTextStream.padChar() -> str """
        return ""

    def pos(self): # real signature unknown; restored from __doc__
        """ QTextStream.pos() -> int """
        return 0

    def read(self, p_int): # real signature unknown; restored from __doc__
        """ QTextStream.read(int) -> str """
        return ""

    def readAll(self): # real signature unknown; restored from __doc__
        """ QTextStream.readAll() -> str """
        return ""

    def readLine(self, int_maxLength=0): # real signature unknown; restored from __doc__
        """ QTextStream.readLine(int maxLength=0) -> str """
        return ""

    def realNumberNotation(self): # real signature unknown; restored from __doc__
        """ QTextStream.realNumberNotation() -> QTextStream.RealNumberNotation """
        pass

    def realNumberPrecision(self): # real signature unknown; restored from __doc__
        """ QTextStream.realNumberPrecision() -> int """
        return 0

    def reset(self): # real signature unknown; restored from __doc__
        """ QTextStream.reset() """
        pass

    def resetStatus(self): # real signature unknown; restored from __doc__
        """ QTextStream.resetStatus() """
        pass

    def seek(self, p_int): # real signature unknown; restored from __doc__
        """ QTextStream.seek(int) -> bool """
        return False

    def setAutoDetectUnicode(self, bool): # real signature unknown; restored from __doc__
        """ QTextStream.setAutoDetectUnicode(bool) """
        pass

    def setCodec(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTextStream.setCodec(QTextCodec)
        QTextStream.setCodec(str)
        """
        pass

    def setDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ QTextStream.setDevice(QIODevice) """
        pass

    def setFieldAlignment(self, QTextStream_FieldAlignment): # real signature unknown; restored from __doc__
        """ QTextStream.setFieldAlignment(QTextStream.FieldAlignment) """
        pass

    def setFieldWidth(self, p_int): # real signature unknown; restored from __doc__
        """ QTextStream.setFieldWidth(int) """
        pass

    def setGenerateByteOrderMark(self, bool): # real signature unknown; restored from __doc__
        """ QTextStream.setGenerateByteOrderMark(bool) """
        pass

    def setIntegerBase(self, p_int): # real signature unknown; restored from __doc__
        """ QTextStream.setIntegerBase(int) """
        pass

    def setLocale(self, QLocale): # real signature unknown; restored from __doc__
        """ QTextStream.setLocale(QLocale) """
        pass

    def setNumberFlags(self, QTextStream_NumberFlags): # real signature unknown; restored from __doc__
        """ QTextStream.setNumberFlags(QTextStream.NumberFlags) """
        pass

    def setPadChar(self, p_str): # real signature unknown; restored from __doc__
        """ QTextStream.setPadChar(str) """
        pass

    def setRealNumberNotation(self, QTextStream_RealNumberNotation): # real signature unknown; restored from __doc__
        """ QTextStream.setRealNumberNotation(QTextStream.RealNumberNotation) """
        pass

    def setRealNumberPrecision(self, p_int): # real signature unknown; restored from __doc__
        """ QTextStream.setRealNumberPrecision(int) """
        pass

    def setStatus(self, QTextStream_Status): # real signature unknown; restored from __doc__
        """ QTextStream.setStatus(QTextStream.Status) """
        pass

    def setString(self, *args, **kwargs): # real signature unknown
        pass

    def skipWhiteSpace(self): # real signature unknown; restored from __doc__
        """ QTextStream.skipWhiteSpace() """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ QTextStream.status() -> QTextStream.Status """
        pass

    def string(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AlignAccountingStyle = 3
    AlignCenter = 2
    AlignLeft = 0
    AlignRight = 1
    FieldAlignment = None # (!) real value is ''
    FixedNotation = 1
    ForcePoint = 2
    ForceSign = 4
    NumberFlag = None # (!) real value is ''
    NumberFlags = None # (!) real value is ''
    Ok = 0
    ReadCorruptData = 2
    ReadPastEnd = 1
    RealNumberNotation = None # (!) real value is ''
    ScientificNotation = 2
    ShowBase = 1
    SmartNotation = 0
    Status = None # (!) real value is ''
    UppercaseBase = 8
    UppercaseDigits = 16
    WriteFailed = 3


