# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


class QRegExp(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QRegExp()
    QRegExp(str, Qt.CaseSensitivity cs=Qt.CaseSensitive, QRegExp.PatternSyntax syntax=QRegExp.RegExp)
    QRegExp(QRegExp)
    """
    def cap(self, int_nth=0): # real signature unknown; restored from __doc__
        """ QRegExp.cap(int nth=0) -> str """
        return ""

    def captureCount(self): # real signature unknown; restored from __doc__
        """ QRegExp.captureCount() -> int """
        return 0

    def capturedTexts(self): # real signature unknown; restored from __doc__
        """ QRegExp.capturedTexts() -> list-of-str """
        pass

    def caseSensitivity(self): # real signature unknown; restored from __doc__
        """ QRegExp.caseSensitivity() -> Qt.CaseSensitivity """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QRegExp.errorString() -> str """
        return ""

    def escape(self, p_str): # real signature unknown; restored from __doc__
        """ QRegExp.escape(str) -> str """
        return ""

    def exactMatch(self, p_str): # real signature unknown; restored from __doc__
        """ QRegExp.exactMatch(str) -> bool """
        return False

    def indexIn(self, p_str, int_offset=0, QRegExp_CaretMode_caretMode=None): # real signature unknown; restored from __doc__
        """ QRegExp.indexIn(str, int offset=0, QRegExp.CaretMode caretMode=QRegExp.CaretAtZero) -> int """
        return 0

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QRegExp.isEmpty() -> bool """
        return False

    def isMinimal(self): # real signature unknown; restored from __doc__
        """ QRegExp.isMinimal() -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ QRegExp.isValid() -> bool """
        return False

    def lastIndexIn(self, p_str, int_offset=-1, QRegExp_CaretMode_caretMode=None): # real signature unknown; restored from __doc__
        """ QRegExp.lastIndexIn(str, int offset=-1, QRegExp.CaretMode caretMode=QRegExp.CaretAtZero) -> int """
        return 0

    def matchedLength(self): # real signature unknown; restored from __doc__
        """ QRegExp.matchedLength() -> int """
        return 0

    def numCaptures(self): # real signature unknown; restored from __doc__
        """ QRegExp.numCaptures() -> int """
        return 0

    def pattern(self): # real signature unknown; restored from __doc__
        """ QRegExp.pattern() -> str """
        return ""

    def patternSyntax(self): # real signature unknown; restored from __doc__
        """ QRegExp.patternSyntax() -> QRegExp.PatternSyntax """
        pass

    def pos(self, int_nth=0): # real signature unknown; restored from __doc__
        """ QRegExp.pos(int nth=0) -> int """
        return 0

    def setCaseSensitivity(self, Qt_CaseSensitivity): # real signature unknown; restored from __doc__
        """ QRegExp.setCaseSensitivity(Qt.CaseSensitivity) """
        pass

    def setMinimal(self, bool): # real signature unknown; restored from __doc__
        """ QRegExp.setMinimal(bool) """
        pass

    def setPattern(self, p_str): # real signature unknown; restored from __doc__
        """ QRegExp.setPattern(str) """
        pass

    def setPatternSyntax(self, QRegExp_PatternSyntax): # real signature unknown; restored from __doc__
        """ QRegExp.setPatternSyntax(QRegExp.PatternSyntax) """
        pass

    def swap(self, QRegExp): # real signature unknown; restored from __doc__
        """ QRegExp.swap(QRegExp) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CaretAtOffset = 1
    CaretAtZero = 0
    CaretMode = None # (!) real value is ''
    CaretWontMatch = 2
    FixedString = 2
    PatternSyntax = None # (!) real value is ''
    RegExp = 0
    RegExp2 = 3
    W3CXmlSchema11 = 5
    Wildcard = 1
    WildcardUnix = 4
    __hash__ = None


