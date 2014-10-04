# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from .QAbstractSpinBox import QAbstractSpinBox

class QSpinBox(QAbstractSpinBox):
    """ QSpinBox(QWidget parent=None) """
    def cleanText(self): # real signature unknown; restored from __doc__
        """ QSpinBox.cleanText() -> str """
        return ""

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QSpinBox.event(QEvent) -> bool """
        return False

    def fixup(self, p_str): # real signature unknown; restored from __doc__
        """ QSpinBox.fixup(str) -> str """
        return ""

    def maximum(self): # real signature unknown; restored from __doc__
        """ QSpinBox.maximum() -> int """
        return 0

    def minimum(self): # real signature unknown; restored from __doc__
        """ QSpinBox.minimum() -> int """
        return 0

    def prefix(self): # real signature unknown; restored from __doc__
        """ QSpinBox.prefix() -> str """
        return ""

    def setMaximum(self, p_int): # real signature unknown; restored from __doc__
        """ QSpinBox.setMaximum(int) """
        pass

    def setMinimum(self, p_int): # real signature unknown; restored from __doc__
        """ QSpinBox.setMinimum(int) """
        pass

    def setPrefix(self, p_str): # real signature unknown; restored from __doc__
        """ QSpinBox.setPrefix(str) """
        pass

    def setRange(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QSpinBox.setRange(int, int) """
        pass

    def setSingleStep(self, p_int): # real signature unknown; restored from __doc__
        """ QSpinBox.setSingleStep(int) """
        pass

    def setSuffix(self, p_str): # real signature unknown; restored from __doc__
        """ QSpinBox.setSuffix(str) """
        pass

    def setValue(self, p_int): # real signature unknown; restored from __doc__
        """ QSpinBox.setValue(int) """
        pass

    def singleStep(self): # real signature unknown; restored from __doc__
        """ QSpinBox.singleStep() -> int """
        return 0

    def suffix(self): # real signature unknown; restored from __doc__
        """ QSpinBox.suffix() -> str """
        return ""

    def textFromValue(self, p_int): # real signature unknown; restored from __doc__
        """ QSpinBox.textFromValue(int) -> str """
        return ""

    def validate(self, p_str, p_int): # real signature unknown; restored from __doc__
        """ QSpinBox.validate(str, int) -> (QValidator.State, str, int) """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ QSpinBox.value() -> int """
        return 0

    def valueChanged(self, *args, **kwargs): # real signature unknown
        """
        QSpinBox.valueChanged[int] [signal]
        QSpinBox.valueChanged[str] [signal]
        """
        pass

    def valueFromText(self, p_str): # real signature unknown; restored from __doc__
        """ QSpinBox.valueFromText(str) -> int """
        return 0

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass


