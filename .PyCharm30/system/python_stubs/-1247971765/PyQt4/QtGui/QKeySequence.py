# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QKeySequence(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QKeySequence()
    QKeySequence(QKeySequence)
    QKeySequence(str, QKeySequence.SequenceFormat)
    QKeySequence(int, int key2=0, int key3=0, int key4=0)
    QKeySequence(object)
    """
    def count(self): # real signature unknown; restored from __doc__
        """ QKeySequence.count() -> int """
        return 0

    def fromString(self, p_str, QKeySequence_SequenceFormat_format=None): # real signature unknown; restored from __doc__
        """ QKeySequence.fromString(str, QKeySequence.SequenceFormat format=QKeySequence.PortableText) -> QKeySequence """
        return QKeySequence

    def isDetached(self): # real signature unknown; restored from __doc__
        """ QKeySequence.isDetached() -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QKeySequence.isEmpty() -> bool """
        return False

    def keyBindings(self, QKeySequence_StandardKey): # real signature unknown; restored from __doc__
        """ QKeySequence.keyBindings(QKeySequence.StandardKey) -> list-of-QKeySequence """
        pass

    def matches(self, QKeySequence): # real signature unknown; restored from __doc__
        """ QKeySequence.matches(QKeySequence) -> QKeySequence.SequenceMatch """
        pass

    def mnemonic(self, p_str): # real signature unknown; restored from __doc__
        """ QKeySequence.mnemonic(str) -> QKeySequence """
        return QKeySequence

    def swap(self, QKeySequence): # real signature unknown; restored from __doc__
        """ QKeySequence.swap(QKeySequence) """
        pass

    def toString(self, QKeySequence_SequenceFormat_format=None): # real signature unknown; restored from __doc__
        """ QKeySequence.toString(QKeySequence.SequenceFormat format=QKeySequence.PortableText) -> str """
        return ""

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AddTab = 19
    Back = 13
    Bold = 27
    Close = 4
    Copy = 9
    Cut = 8
    Delete = 7
    DeleteEndOfLine = 60
    DeleteEndOfWord = 59
    DeleteStartOfWord = 58
    ExactMatch = 2
    Find = 22
    FindNext = 23
    FindPrevious = 24
    Forward = 14
    HelpContents = 1
    InsertLineSeparator = 62
    InsertParagraphSeparator = 61
    Italic = 28
    MoveToEndOfBlock = 41
    MoveToEndOfDocument = 43
    MoveToEndOfLine = 39
    MoveToNextChar = 30
    MoveToNextLine = 34
    MoveToNextPage = 36
    MoveToNextWord = 32
    MoveToPreviousChar = 31
    MoveToPreviousLine = 35
    MoveToPreviousPage = 37
    MoveToPreviousWord = 33
    MoveToStartOfBlock = 40
    MoveToStartOfDocument = 42
    MoveToStartOfLine = 38
    NativeText = 0
    New = 6
    NextChild = 20
    NoMatch = 0
    Open = 3
    PartialMatch = 1
    Paste = 10
    PortableText = 1
    Preferences = 64
    PreviousChild = 21
    Print = 18
    Quit = 65
    Redo = 12
    Refresh = 15
    Replace = 25
    Save = 5
    SaveAs = 63
    SelectAll = 26
    SelectEndOfBlock = 55
    SelectEndOfDocument = 57
    SelectEndOfLine = 53
    SelectNextChar = 44
    SelectNextLine = 48
    SelectNextPage = 50
    SelectNextWord = 46
    SelectPreviousChar = 45
    SelectPreviousLine = 49
    SelectPreviousPage = 51
    SelectPreviousWord = 47
    SelectStartOfBlock = 54
    SelectStartOfDocument = 56
    SelectStartOfLine = 52
    SequenceFormat = None # (!) real value is ''
    SequenceMatch = None # (!) real value is ''
    StandardKey = None # (!) real value is ''
    Underline = 29
    Undo = 11
    UnknownKey = 0
    WhatsThis = 2
    ZoomIn = 16
    ZoomOut = 17
    __hash__ = None


