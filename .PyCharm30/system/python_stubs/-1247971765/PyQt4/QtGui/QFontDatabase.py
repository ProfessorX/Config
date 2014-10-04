# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QFontDatabase(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QFontDatabase()
    QFontDatabase(QFontDatabase)
    """
    def addApplicationFont(self, p_str): # real signature unknown; restored from __doc__
        """ QFontDatabase.addApplicationFont(str) -> int """
        return 0

    def addApplicationFontFromData(self, QByteArray): # real signature unknown; restored from __doc__
        """ QFontDatabase.addApplicationFontFromData(QByteArray) -> int """
        return 0

    def applicationFontFamilies(self, p_int): # real signature unknown; restored from __doc__
        """ QFontDatabase.applicationFontFamilies(int) -> list-of-str """
        pass

    def bold(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QFontDatabase.bold(str, str) -> bool """
        return False

    def families(self, QFontDatabase_WritingSystem_writingSystem=None): # real signature unknown; restored from __doc__
        """ QFontDatabase.families(QFontDatabase.WritingSystem writingSystem=QFontDatabase.Any) -> list-of-str """
        pass

    def font(self, p_str, p_str_1, p_int): # real signature unknown; restored from __doc__
        """ QFontDatabase.font(str, str, int) -> QFont """
        return QFont

    def isBitmapScalable(self, p_str, str_style=''): # real signature unknown; restored from __doc__
        """ QFontDatabase.isBitmapScalable(str, str style='') -> bool """
        return False

    def isFixedPitch(self, p_str, str_style=''): # real signature unknown; restored from __doc__
        """ QFontDatabase.isFixedPitch(str, str style='') -> bool """
        return False

    def isScalable(self, p_str, str_style=''): # real signature unknown; restored from __doc__
        """ QFontDatabase.isScalable(str, str style='') -> bool """
        return False

    def isSmoothlyScalable(self, p_str, str_style=''): # real signature unknown; restored from __doc__
        """ QFontDatabase.isSmoothlyScalable(str, str style='') -> bool """
        return False

    def italic(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QFontDatabase.italic(str, str) -> bool """
        return False

    def pointSizes(self, p_str, str_style=''): # real signature unknown; restored from __doc__
        """ QFontDatabase.pointSizes(str, str style='') -> list-of-int """
        pass

    def removeAllApplicationFonts(self): # real signature unknown; restored from __doc__
        """ QFontDatabase.removeAllApplicationFonts() -> bool """
        return False

    def removeApplicationFont(self, p_int): # real signature unknown; restored from __doc__
        """ QFontDatabase.removeApplicationFont(int) -> bool """
        return False

    def smoothSizes(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QFontDatabase.smoothSizes(str, str) -> list-of-int """
        pass

    def standardSizes(self): # real signature unknown; restored from __doc__
        """ QFontDatabase.standardSizes() -> list-of-int """
        pass

    def styles(self, p_str): # real signature unknown; restored from __doc__
        """ QFontDatabase.styles(str) -> list-of-str """
        pass

    def styleString(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFontDatabase.styleString(QFont) -> str
        QFontDatabase.styleString(QFontInfo) -> str
        """
        return ""

    def supportsThreadedFontRendering(self): # real signature unknown; restored from __doc__
        """ QFontDatabase.supportsThreadedFontRendering() -> bool """
        return False

    def weight(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QFontDatabase.weight(str, str) -> int """
        return 0

    def writingSystemName(self, QFontDatabase_WritingSystem): # real signature unknown; restored from __doc__
        """ QFontDatabase.writingSystemName(QFontDatabase.WritingSystem) -> str """
        return ""

    def writingSystems(self, p_str=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QFontDatabase.writingSystems() -> list-of-QFontDatabase.WritingSystem
        QFontDatabase.writingSystems(str) -> list-of-QFontDatabase.WritingSystem
        """
        pass

    def writingSystemSample(self, QFontDatabase_WritingSystem): # real signature unknown; restored from __doc__
        """ QFontDatabase.writingSystemSample(QFontDatabase.WritingSystem) -> str """
        return ""

    def __init__(self, QFontDatabase=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Any = 0
    Arabic = 6
    Armenian = 4
    Bengali = 10
    Cyrillic = 3
    Devanagari = 9
    Georgian = 23
    Greek = 2
    Gujarati = 12
    Gurmukhi = 11
    Hebrew = 5
    Japanese = 27
    Kannada = 16
    Khmer = 24
    Korean = 28
    Lao = 20
    Latin = 1
    Malayalam = 17
    Myanmar = 22
    Nko = 33
    Ogham = 31
    Oriya = 13
    Other = 30
    Runic = 32
    SimplifiedChinese = 25
    Sinhala = 18
    Symbol = 30
    Syriac = 7
    Tamil = 14
    Telugu = 15
    Thaana = 8
    Thai = 19
    Tibetan = 21
    TraditionalChinese = 26
    Vietnamese = 29
    WritingSystem = None # (!) real value is ''


