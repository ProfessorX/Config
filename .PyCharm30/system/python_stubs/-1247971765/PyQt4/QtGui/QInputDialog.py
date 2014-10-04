# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from .QDialog import QDialog

class QInputDialog(QDialog):
    """ QInputDialog(QWidget parent=None, Qt.WindowFlags flags=0) """
    def cancelButtonText(self): # real signature unknown; restored from __doc__
        """ QInputDialog.cancelButtonText() -> str """
        return ""

    def comboBoxItems(self): # real signature unknown; restored from __doc__
        """ QInputDialog.comboBoxItems() -> list-of-str """
        pass

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ QInputDialog.done(int) """
        pass

    def doubleDecimals(self): # real signature unknown; restored from __doc__
        """ QInputDialog.doubleDecimals() -> int """
        return 0

    def doubleMaximum(self): # real signature unknown; restored from __doc__
        """ QInputDialog.doubleMaximum() -> float """
        return 0.0

    def doubleMinimum(self): # real signature unknown; restored from __doc__
        """ QInputDialog.doubleMinimum() -> float """
        return 0.0

    def doubleValue(self): # real signature unknown; restored from __doc__
        """ QInputDialog.doubleValue() -> float """
        return 0.0

    def doubleValueChanged(self, *args, **kwargs): # real signature unknown
        """ QInputDialog.doubleValueChanged[float] [signal] """
        pass

    def doubleValueSelected(self, *args, **kwargs): # real signature unknown
        """ QInputDialog.doubleValueSelected[float] [signal] """
        pass

    def getDouble(self, QWidget, p_str, p_str_1, float_value=0, float_min=-2147483647, float_max=2147483647, int_decimals=1, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        """ QInputDialog.getDouble(QWidget, str, str, float value=0, float min=-2147483647, float max=2147483647, int decimals=1, Qt.WindowFlags flags=0) -> (float, bool) """
        pass

    def getInt(self, QWidget, p_str, p_str_1, int_value=0, int_min=-2147483647, int_max=2147483647, int_step=1, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        """ QInputDialog.getInt(QWidget, str, str, int value=0, int min=-2147483647, int max=2147483647, int step=1, Qt.WindowFlags flags=0) -> (int, bool) """
        pass

    def getInteger(self, QWidget, p_str, p_str_1, int_value=0, int_min=-2147483647, int_max=2147483647, int_step=1, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        """ QInputDialog.getInteger(QWidget, str, str, int value=0, int min=-2147483647, int max=2147483647, int step=1, Qt.WindowFlags flags=0) -> (int, bool) """
        pass

    def getItem(self, QWidget, p_str, p_str_1, list_of_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QInputDialog.getItem(QWidget, str, str, list-of-str, int current=0, bool editable=True, Qt.WindowFlags flags=0) -> (str, bool)
        QInputDialog.getItem(QWidget, str, str, list-of-str, int, bool, Qt.WindowFlags, Qt.InputMethodHints) -> (str, bool)
        """
        pass

    def getText(self, QWidget, p_str, p_str_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QInputDialog.getText(QWidget, str, str, QLineEdit.EchoMode mode=QLineEdit.Normal, str text='', Qt.WindowFlags flags=0) -> (str, bool)
        QInputDialog.getText(QWidget, str, str, QLineEdit.EchoMode, str, Qt.WindowFlags, Qt.InputMethodHints) -> (str, bool)
        """
        pass

    def inputMode(self): # real signature unknown; restored from __doc__
        """ QInputDialog.inputMode() -> QInputDialog.InputMode """
        pass

    def intMaximum(self): # real signature unknown; restored from __doc__
        """ QInputDialog.intMaximum() -> int """
        return 0

    def intMinimum(self): # real signature unknown; restored from __doc__
        """ QInputDialog.intMinimum() -> int """
        return 0

    def intStep(self): # real signature unknown; restored from __doc__
        """ QInputDialog.intStep() -> int """
        return 0

    def intValue(self): # real signature unknown; restored from __doc__
        """ QInputDialog.intValue() -> int """
        return 0

    def intValueChanged(self, *args, **kwargs): # real signature unknown
        """ QInputDialog.intValueChanged[int] [signal] """
        pass

    def intValueSelected(self, *args, **kwargs): # real signature unknown
        """ QInputDialog.intValueSelected[int] [signal] """
        pass

    def isComboBoxEditable(self): # real signature unknown; restored from __doc__
        """ QInputDialog.isComboBoxEditable() -> bool """
        return False

    def labelText(self): # real signature unknown; restored from __doc__
        """ QInputDialog.labelText() -> str """
        return ""

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ QInputDialog.minimumSizeHint() -> QSize """
        pass

    def okButtonText(self): # real signature unknown; restored from __doc__
        """ QInputDialog.okButtonText() -> str """
        return ""

    def open(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QInputDialog.open()
        QInputDialog.open(QObject, SLOT())
        QInputDialog.open(callable)
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ QInputDialog.options() -> QInputDialog.InputDialogOptions """
        pass

    def setCancelButtonText(self, p_str): # real signature unknown; restored from __doc__
        """ QInputDialog.setCancelButtonText(str) """
        pass

    def setComboBoxEditable(self, bool): # real signature unknown; restored from __doc__
        """ QInputDialog.setComboBoxEditable(bool) """
        pass

    def setComboBoxItems(self, list_of_str): # real signature unknown; restored from __doc__
        """ QInputDialog.setComboBoxItems(list-of-str) """
        pass

    def setDoubleDecimals(self, p_int): # real signature unknown; restored from __doc__
        """ QInputDialog.setDoubleDecimals(int) """
        pass

    def setDoubleMaximum(self, p_float): # real signature unknown; restored from __doc__
        """ QInputDialog.setDoubleMaximum(float) """
        pass

    def setDoubleMinimum(self, p_float): # real signature unknown; restored from __doc__
        """ QInputDialog.setDoubleMinimum(float) """
        pass

    def setDoubleRange(self, p_float, p_float_1): # real signature unknown; restored from __doc__
        """ QInputDialog.setDoubleRange(float, float) """
        pass

    def setDoubleValue(self, p_float): # real signature unknown; restored from __doc__
        """ QInputDialog.setDoubleValue(float) """
        pass

    def setInputMode(self, QInputDialog_InputMode): # real signature unknown; restored from __doc__
        """ QInputDialog.setInputMode(QInputDialog.InputMode) """
        pass

    def setIntMaximum(self, p_int): # real signature unknown; restored from __doc__
        """ QInputDialog.setIntMaximum(int) """
        pass

    def setIntMinimum(self, p_int): # real signature unknown; restored from __doc__
        """ QInputDialog.setIntMinimum(int) """
        pass

    def setIntRange(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ QInputDialog.setIntRange(int, int) """
        pass

    def setIntStep(self, p_int): # real signature unknown; restored from __doc__
        """ QInputDialog.setIntStep(int) """
        pass

    def setIntValue(self, p_int): # real signature unknown; restored from __doc__
        """ QInputDialog.setIntValue(int) """
        pass

    def setLabelText(self, p_str): # real signature unknown; restored from __doc__
        """ QInputDialog.setLabelText(str) """
        pass

    def setOkButtonText(self, p_str): # real signature unknown; restored from __doc__
        """ QInputDialog.setOkButtonText(str) """
        pass

    def setOption(self, QInputDialog_InputDialogOption, bool_on=True): # real signature unknown; restored from __doc__
        """ QInputDialog.setOption(QInputDialog.InputDialogOption, bool on=True) """
        pass

    def setOptions(self, QInputDialog_InputDialogOptions): # real signature unknown; restored from __doc__
        """ QInputDialog.setOptions(QInputDialog.InputDialogOptions) """
        pass

    def setTextEchoMode(self, QLineEdit_EchoMode): # real signature unknown; restored from __doc__
        """ QInputDialog.setTextEchoMode(QLineEdit.EchoMode) """
        pass

    def setTextValue(self, p_str): # real signature unknown; restored from __doc__
        """ QInputDialog.setTextValue(str) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ QInputDialog.setVisible(bool) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QInputDialog.sizeHint() -> QSize """
        pass

    def testOption(self, QInputDialog_InputDialogOption): # real signature unknown; restored from __doc__
        """ QInputDialog.testOption(QInputDialog.InputDialogOption) -> bool """
        return False

    def textEchoMode(self): # real signature unknown; restored from __doc__
        """ QInputDialog.textEchoMode() -> QLineEdit.EchoMode """
        pass

    def textValue(self): # real signature unknown; restored from __doc__
        """ QInputDialog.textValue() -> str """
        return ""

    def textValueChanged(self, *args, **kwargs): # real signature unknown
        """ QInputDialog.textValueChanged[str] [signal] """
        pass

    def textValueSelected(self, *args, **kwargs): # real signature unknown
        """ QInputDialog.textValueSelected[str] [signal] """
        pass

    def __init__(self, QWidget_parent=None, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        pass

    DoubleInput = 2
    InputDialogOption = None # (!) real value is ''
    InputDialogOptions = None # (!) real value is ''
    InputMode = None # (!) real value is ''
    IntInput = 1
    NoButtons = 1
    TextInput = 0
    UseListViewForComboBoxItems = 2


