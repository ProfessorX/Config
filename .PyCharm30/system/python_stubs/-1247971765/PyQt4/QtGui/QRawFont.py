# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QRawFont(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QRawFont()
    QRawFont(str, float, QFont.HintingPreference hintingPreference=QFont.PreferDefaultHinting)
    QRawFont(QByteArray, float, QFont.HintingPreference hintingPreference=QFont.PreferDefaultHinting)
    QRawFont(QRawFont)
    """
    def advancesForGlyphIndexes(self, list_of_int): # real signature unknown; restored from __doc__
        """ QRawFont.advancesForGlyphIndexes(list-of-int) -> list-of-QPointF """
        pass

    def alphaMapForGlyph(self, p_int, QRawFont_AntialiasingType_antialiasingType=None, QTransform_transform=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QRawFont.alphaMapForGlyph(int, QRawFont.AntialiasingType antialiasingType=QRawFont.SubPixelAntialiasing, QTransform transform=QTransform()) -> QImage """
        pass

    def ascent(self): # real signature unknown; restored from __doc__
        """ QRawFont.ascent() -> float """
        return 0.0

    def averageCharWidth(self): # real signature unknown; restored from __doc__
        """ QRawFont.averageCharWidth() -> float """
        return 0.0

    def descent(self): # real signature unknown; restored from __doc__
        """ QRawFont.descent() -> float """
        return 0.0

    def familyName(self): # real signature unknown; restored from __doc__
        """ QRawFont.familyName() -> str """
        return ""

    def fontTable(self, p_str): # real signature unknown; restored from __doc__
        """ QRawFont.fontTable(str) -> QByteArray """
        pass

    def fromFont(self, QFont, QFontDatabase_WritingSystem_writingSystem=None): # real signature unknown; restored from __doc__
        """ QRawFont.fromFont(QFont, QFontDatabase.WritingSystem writingSystem=QFontDatabase.Any) -> QRawFont """
        return QRawFont

    def glyphIndexesForString(self, p_str): # real signature unknown; restored from __doc__
        """ QRawFont.glyphIndexesForString(str) -> list-of-int """
        pass

    def hintingPreference(self): # real signature unknown; restored from __doc__
        """ QRawFont.hintingPreference() -> QFont.HintingPreference """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ QRawFont.isValid() -> bool """
        return False

    def leading(self): # real signature unknown; restored from __doc__
        """ QRawFont.leading() -> float """
        return 0.0

    def loadFromData(self, QByteArray, p_float, QFont_HintingPreference): # real signature unknown; restored from __doc__
        """ QRawFont.loadFromData(QByteArray, float, QFont.HintingPreference) """
        pass

    def loadFromFile(self, p_str, p_float, QFont_HintingPreference): # real signature unknown; restored from __doc__
        """ QRawFont.loadFromFile(str, float, QFont.HintingPreference) """
        pass

    def maxCharWidth(self): # real signature unknown; restored from __doc__
        """ QRawFont.maxCharWidth() -> float """
        return 0.0

    def pathForGlyph(self, p_int): # real signature unknown; restored from __doc__
        """ QRawFont.pathForGlyph(int) -> QPainterPath """
        return QPainterPath

    def pixelSize(self): # real signature unknown; restored from __doc__
        """ QRawFont.pixelSize() -> float """
        return 0.0

    def setPixelSize(self, p_float): # real signature unknown; restored from __doc__
        """ QRawFont.setPixelSize(float) """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ QRawFont.style() -> QFont.Style """
        pass

    def styleName(self): # real signature unknown; restored from __doc__
        """ QRawFont.styleName() -> str """
        return ""

    def supportedWritingSystems(self): # real signature unknown; restored from __doc__
        """ QRawFont.supportedWritingSystems() -> list-of-QFontDatabase.WritingSystem """
        pass

    def supportsCharacter(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QRawFont.supportsCharacter(int) -> bool
        QRawFont.supportsCharacter(str) -> bool
        """
        return False

    def unitsPerEm(self): # real signature unknown; restored from __doc__
        """ QRawFont.unitsPerEm() -> float """
        return 0.0

    def weight(self): # real signature unknown; restored from __doc__
        """ QRawFont.weight() -> int """
        return 0

    def xHeight(self): # real signature unknown; restored from __doc__
        """ QRawFont.xHeight() -> float """
        return 0.0

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

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AntialiasingType = None # (!) real value is ''
    PixelAntialiasing = 0
    SubPixelAntialiasing = 1
    __hash__ = None


