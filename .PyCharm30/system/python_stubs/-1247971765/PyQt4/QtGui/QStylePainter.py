# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from .QPainter import QPainter

class QStylePainter(QPainter):
    """
    QStylePainter()
    QStylePainter(QWidget)
    QStylePainter(QPaintDevice, QWidget)
    """
    def begin(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QStylePainter.begin(QWidget) -> bool
        QStylePainter.begin(QPaintDevice, QWidget) -> bool
        """
        return False

    def drawComplexControl(self, QStyle_ComplexControl, QStyleOptionComplex): # real signature unknown; restored from __doc__
        """ QStylePainter.drawComplexControl(QStyle.ComplexControl, QStyleOptionComplex) """
        pass

    def drawControl(self, QStyle_ControlElement, QStyleOption): # real signature unknown; restored from __doc__
        """ QStylePainter.drawControl(QStyle.ControlElement, QStyleOption) """
        pass

    def drawItemPixmap(self, QRect, p_int, QPixmap): # real signature unknown; restored from __doc__
        """ QStylePainter.drawItemPixmap(QRect, int, QPixmap) """
        pass

    def drawItemText(self, QRect, p_int, QPalette, bool, p_str, QPalette_ColorRole_textRole=None): # real signature unknown; restored from __doc__
        """ QStylePainter.drawItemText(QRect, int, QPalette, bool, str, QPalette.ColorRole textRole=QPalette.NoRole) """
        pass

    def drawPrimitive(self, QStyle_PrimitiveElement, QStyleOption): # real signature unknown; restored from __doc__
        """ QStylePainter.drawPrimitive(QStyle.PrimitiveElement, QStyleOption) """
        pass

    def style(self): # real signature unknown; restored from __doc__
        """ QStylePainter.style() -> QStyle """
        return QStyle

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


