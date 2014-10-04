# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt4/QtNetwork.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QLocalServer(__PyQt4_QtCore.QObject):
    """ QLocalServer(QObject parent=None) """
    def close(self): # real signature unknown; restored from __doc__
        """ QLocalServer.close() """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ QLocalServer.errorString() -> str """
        return ""

    def fullServerName(self): # real signature unknown; restored from __doc__
        """ QLocalServer.fullServerName() -> str """
        return ""

    def hasPendingConnections(self): # real signature unknown; restored from __doc__
        """ QLocalServer.hasPendingConnections() -> bool """
        return False

    def incomingConnection(self, sip_voidptr): # real signature unknown; restored from __doc__
        """ QLocalServer.incomingConnection(sip.voidptr) """
        pass

    def isListening(self): # real signature unknown; restored from __doc__
        """ QLocalServer.isListening() -> bool """
        return False

    def listen(self, p_str): # real signature unknown; restored from __doc__
        """ QLocalServer.listen(str) -> bool """
        return False

    def maxPendingConnections(self): # real signature unknown; restored from __doc__
        """ QLocalServer.maxPendingConnections() -> int """
        return 0

    def newConnection(self, *args, **kwargs): # real signature unknown
        """ QLocalServer.newConnection [signal] """
        pass

    def nextPendingConnection(self): # real signature unknown; restored from __doc__
        """ QLocalServer.nextPendingConnection() -> QLocalSocket """
        return QLocalSocket

    def removeServer(self, p_str): # real signature unknown; restored from __doc__
        """ QLocalServer.removeServer(str) -> bool """
        return False

    def serverError(self): # real signature unknown; restored from __doc__
        """ QLocalServer.serverError() -> QAbstractSocket.SocketError """
        pass

    def serverName(self): # real signature unknown; restored from __doc__
        """ QLocalServer.serverName() -> str """
        return ""

    def setMaxPendingConnections(self, p_int): # real signature unknown; restored from __doc__
        """ QLocalServer.setMaxPendingConnections(int) """
        pass

    def waitForNewConnection(self, int_msecs=0): # real signature unknown; restored from __doc__
        """ QLocalServer.waitForNewConnection(int msecs=0) -> (bool, bool) """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


