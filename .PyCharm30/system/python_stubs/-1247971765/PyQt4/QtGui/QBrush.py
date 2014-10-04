# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QBrush(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QBrush()
    QBrush(Qt.BrushStyle)
    QBrush(QColor, Qt.BrushStyle style=Qt.SolidPattern)
    QBrush(Qt.GlobalColor, Qt.BrushStyle style=Qt.SolidPattern)
    QBrush(QColor, QPixmap)
    QBrush(Qt.GlobalColor, QPixmap)
    QBrush(QPixmap)
    QBrush(QImage)
    QBrush(QGradient)
    QBrush(QBrush)
    QBrush(object)
    """
    def color(self): # real signature unknown; restored from __doc__
        """ QBrush.color() -> QColor """
        return QColor

    def gradient(self): # real signature unknown; restored from __doc__
        """ QBrush.gradient() -> QGradient """
        return QGradient

    def isOpaque(self): # real signature unknown; restored from __doc__
        """ QBrush.isOpaque() -> bool """
        return False

    def matrix(self): # real signature unknown; restored from __doc__
        """ QBrush.matrix() -> QMatrix """
        return QMatrix

    def setColor(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QBrush.setColor(QColor)
        QBrush.setColor(Qt.GlobalColor)
        """
        pass

    def setMatrix(self, QMatrix): # real signature unknown; restored from __doc__
        """ QBrush.setMatrix(QMatrix) """
        pass

    def setStyle(self, Qt_BrushStyle): # real signature unknown; restored from __doc__
        """ QBrush.setStyle(Qt.BrushStyle) """
        pass

    def setTexture(self, QPixmap): # real signature unknown; restored from __doc__
        """ QBrush.setTexture(QPixmap) """
        pass

    def setTextureImage(self, QImage): # real signature unknown; restored from __doc__
        """ QBrush.setTextureImage(QImage) """
        pass

    def setTransform(self, QTransform): # real signature unknown; restored from __doc__
        """ QBrush.setTransform(QTransform) """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ QBrush.style() -> Qt.BrushStyle """
        pass

    def swap(self, QBrush): # real signature unknown; restored from __doc__
        """ QBrush.swap(QBrush) """
        pass

    def texture(self): # real signature unknown; restored from __doc__
        """ QBrush.texture() -> QPixmap """
        return QPixmap

    def textureImage(self): # real signature unknown; restored from __doc__
        """ QBrush.textureImage() -> QImage """
        return QImage

    def transform(self): # real signature unknown; restored from __doc__
        """ QBrush.transform() -> QTransform """
        return QTransform

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


    __hash__ = None


