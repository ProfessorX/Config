# encoding: utf-8
# module PyKDE4.kdecore
# from /usr/lib/python2.7/dist-packages/PyKDE4/kdecore.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtNetwork as __PyQt4_QtNetwork


from KProcess import KProcess

class KPtyProcess(KProcess):
    # no doc
    def isUseUtmp(self, *args, **kwargs): # real signature unknown
        pass

    def pty(self, *args, **kwargs): # real signature unknown
        pass

    def ptyChannels(self, *args, **kwargs): # real signature unknown
        pass

    def setPtyChannels(self, *args, **kwargs): # real signature unknown
        pass

    def setupChildProcess(self, *args, **kwargs): # real signature unknown
        pass

    def setUseUtmp(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AllChannels = 7
    AllOutputChannels = 6
    NoChannels = 0
    PtyChannelFlag = None # (!) real value is ''
    PtyChannels = None # (!) real value is ''
    StderrChannel = 4
    StdinChannel = 1
    StdoutChannel = 2


