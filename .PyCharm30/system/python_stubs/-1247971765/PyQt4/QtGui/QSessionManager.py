# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QSessionManager(__PyQt4_QtCore.QObject):
    # no doc
    def allowsErrorInteraction(self): # real signature unknown; restored from __doc__
        """ QSessionManager.allowsErrorInteraction() -> bool """
        return False

    def allowsInteraction(self): # real signature unknown; restored from __doc__
        """ QSessionManager.allowsInteraction() -> bool """
        return False

    def cancel(self): # real signature unknown; restored from __doc__
        """ QSessionManager.cancel() """
        pass

    def discardCommand(self): # real signature unknown; restored from __doc__
        """ QSessionManager.discardCommand() -> list-of-str """
        pass

    def isPhase2(self): # real signature unknown; restored from __doc__
        """ QSessionManager.isPhase2() -> bool """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """ QSessionManager.release() """
        pass

    def requestPhase2(self): # real signature unknown; restored from __doc__
        """ QSessionManager.requestPhase2() """
        pass

    def restartCommand(self): # real signature unknown; restored from __doc__
        """ QSessionManager.restartCommand() -> list-of-str """
        pass

    def restartHint(self): # real signature unknown; restored from __doc__
        """ QSessionManager.restartHint() -> QSessionManager.RestartHint """
        pass

    def sessionId(self): # real signature unknown; restored from __doc__
        """ QSessionManager.sessionId() -> str """
        return ""

    def sessionKey(self): # real signature unknown; restored from __doc__
        """ QSessionManager.sessionKey() -> str """
        return ""

    def setDiscardCommand(self, list_of_str): # real signature unknown; restored from __doc__
        """ QSessionManager.setDiscardCommand(list-of-str) """
        pass

    def setManagerProperty(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QSessionManager.setManagerProperty(str, str)
        QSessionManager.setManagerProperty(str, list-of-str)
        """
        pass

    def setRestartCommand(self, list_of_str): # real signature unknown; restored from __doc__
        """ QSessionManager.setRestartCommand(list-of-str) """
        pass

    def setRestartHint(self, QSessionManager_RestartHint): # real signature unknown; restored from __doc__
        """ QSessionManager.setRestartHint(QSessionManager.RestartHint) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    RestartAnyway = 1
    RestartHint = None # (!) real value is ''
    RestartIfRunning = 0
    RestartImmediately = 2
    RestartNever = 3


