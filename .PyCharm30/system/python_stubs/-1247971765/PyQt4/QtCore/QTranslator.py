# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


from .QObject import QObject

class QTranslator(QObject):
    """ QTranslator(QObject parent=None) """
    def isEmpty(self): # real signature unknown; restored from __doc__
        """ QTranslator.isEmpty() -> bool """
        return False

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTranslator.load(str, str directory='', str searchDelimiters='', str suffix='') -> bool
        QTranslator.load(QLocale, str, str prefix='', str directory='', str suffix='') -> bool
        """
        return False

    def loadFromData(self, p_str): # real signature unknown; restored from __doc__
        """ QTranslator.loadFromData(str) -> bool """
        return False

    def translate(self, p_str, p_str_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTranslator.translate(str, str, str disambiguation=None) -> str
        QTranslator.translate(str, str, str, int) -> str
        """
        return ""

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


