# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from .QAbstractSpinBox import QAbstractSpinBox

class QDoubleSpinBox(QAbstractSpinBox):
    """ QDoubleSpinBox(QWidget parent=None) """
    def cleanText(self): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.cleanText() -> str """
        return ""

    def decimals(self): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.decimals() -> int """
        return 0

    def fixup(self, p_str): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.fixup(str) -> str """
        return ""

    def maximum(self): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.maximum() -> float """
        return 0.0

    def minimum(self): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.minimum() -> float """
        return 0.0

    def prefix(self): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.prefix() -> str """
        return ""

    def setDecimals(self, p_int): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.setDecimals(int) """
        pass

    def setMaximum(self, p_float): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.setMaximum(float) """
        pass

    def setMinimum(self, p_float): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.setMinimum(float) """
        pass

    def setPrefix(self, p_str): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.setPrefix(str) """
        pass

    def setRange(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.setRange(float, float) """
        pass

    def setSingleStep(self, p_float): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.setSingleStep(float) """
        pass

    def setSuffix(self, p_str): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.setSuffix(str) """
        pass

    def setValue(self, p_float): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.setValue(float) """
        pass

    def singleStep(self): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.singleStep() -> float """
        return 0.0

    def suffix(self): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.suffix() -> str """
        return ""

    def textFromValue(self, p_float): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.textFromValue(float) -> str """
        return ""

    def validate(self, p_str, p_int): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.validate(str, int) -> (QValidator.State, str, int) """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.value() -> float """
        return 0.0

    def valueChanged(self, *args, **kwargs): # real signature unknown
        """
        QDoubleSpinBox.valueChanged[float] [signal]
        QDoubleSpinBox.valueChanged[str] [signal]
        """
        pass

    def valueFromText(self, p_str): # real signature unknown; restored from __doc__
        """ QDoubleSpinBox.valueFromText(str) -> float """
        return 0.0

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass


