# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from .QDialog import QDialog

class QPrintPreviewDialog(QDialog):
    """
    QPrintPreviewDialog(QWidget parent=None, Qt.WindowFlags flags=0)
    QPrintPreviewDialog(QPrinter, QWidget parent=None, Qt.WindowFlags flags=0)
    """
    def done(self, p_int): # real signature unknown; restored from __doc__
        """ QPrintPreviewDialog.done(int) """
        pass

    def open(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QPrintPreviewDialog.open()
        QPrintPreviewDialog.open(QObject, SLOT())
        QPrintPreviewDialog.open(callable)
        """
        pass

    def paintRequested(self, *args, **kwargs): # real signature unknown
        """ QPrintPreviewDialog.paintRequested[QPrinter] [signal] """
        pass

    def printer(self): # real signature unknown; restored from __doc__
        """ QPrintPreviewDialog.printer() -> QPrinter """
        return QPrinter

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ QPrintPreviewDialog.setVisible(bool) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


