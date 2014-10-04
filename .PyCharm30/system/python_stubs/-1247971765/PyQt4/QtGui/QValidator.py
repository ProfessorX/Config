# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QValidator(__PyQt4_QtCore.QObject):
    """ QValidator(QObject parent=None) """
    def fixup(self, p_str): # real signature unknown; restored from __doc__
        """ QValidator.fixup(str) -> str """
        return ""

    def locale(self): # real signature unknown; restored from __doc__
        """ QValidator.locale() -> QLocale """
        pass

    def setLocale(self, QLocale): # real signature unknown; restored from __doc__
        """ QValidator.setLocale(QLocale) """
        pass

    def validate(self, p_str, p_int): # real signature unknown; restored from __doc__
        """ QValidator.validate(str, int) -> (QValidator.State, str, int) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    Acceptable = 2
    Intermediate = 1
    Invalid = 0
    State = None # (!) real value is ''


