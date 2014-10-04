# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


from .QFile import QFile

class QTemporaryFile(QFile):
    """
    QTemporaryFile()
    QTemporaryFile(str)
    QTemporaryFile(QObject)
    QTemporaryFile(str, QObject)
    """
    def autoRemove(self): # real signature unknown; restored from __doc__
        """ QTemporaryFile.autoRemove() -> bool """
        return False

    def createLocalFile(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTemporaryFile.createLocalFile(str) -> QTemporaryFile
        QTemporaryFile.createLocalFile(QFile) -> QTemporaryFile
        """
        return QTemporaryFile

    def fileEngine(self): # real signature unknown; restored from __doc__
        """ QTemporaryFile.fileEngine() -> QAbstractFileEngine """
        return QAbstractFileEngine

    def fileName(self): # real signature unknown; restored from __doc__
        """ QTemporaryFile.fileName() -> str """
        return ""

    def fileTemplate(self): # real signature unknown; restored from __doc__
        """ QTemporaryFile.fileTemplate() -> str """
        return ""

    def open(self, QIODevice_OpenMode=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QTemporaryFile.open() -> bool
        QTemporaryFile.open(QIODevice.OpenMode) -> bool
        """
        return False

    def setAutoRemove(self, bool): # real signature unknown; restored from __doc__
        """ QTemporaryFile.setAutoRemove(bool) """
        pass

    def setFileTemplate(self, p_str): # real signature unknown; restored from __doc__
        """ QTemporaryFile.setFileTemplate(str) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


