# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from .QAction import QAction

class QWidgetAction(QAction):
    """ QWidgetAction(QObject) """
    def createdWidgets(self): # real signature unknown; restored from __doc__
        """ QWidgetAction.createdWidgets() -> list-of-QWidget """
        pass

    def createWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QWidgetAction.createWidget(QWidget) -> QWidget """
        return QWidget

    def defaultWidget(self): # real signature unknown; restored from __doc__
        """ QWidgetAction.defaultWidget() -> QWidget """
        return QWidget

    def deleteWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QWidgetAction.deleteWidget(QWidget) """
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QWidgetAction.event(QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ QWidgetAction.eventFilter(QObject, QEvent) -> bool """
        return False

    def releaseWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QWidgetAction.releaseWidget(QWidget) """
        pass

    def requestWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QWidgetAction.requestWidget(QWidget) -> QWidget """
        return QWidget

    def setDefaultWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QWidgetAction.setDefaultWidget(QWidget) """
        pass

    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass


