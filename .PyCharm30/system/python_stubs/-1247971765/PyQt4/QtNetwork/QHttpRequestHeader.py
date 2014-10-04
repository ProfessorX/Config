# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt4/QtNetwork.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from .QHttpHeader import QHttpHeader

class QHttpRequestHeader(QHttpHeader):
    """
    QHttpRequestHeader()
    QHttpRequestHeader(str, str, int major=1, int minor=1)
    QHttpRequestHeader(QHttpRequestHeader)
    QHttpRequestHeader(str)
    """
    def majorVersion(self): # real signature unknown; restored from __doc__
        """ QHttpRequestHeader.majorVersion() -> int """
        return 0

    def method(self): # real signature unknown; restored from __doc__
        """ QHttpRequestHeader.method() -> str """
        return ""

    def minorVersion(self): # real signature unknown; restored from __doc__
        """ QHttpRequestHeader.minorVersion() -> int """
        return 0

    def parseLine(self, p_str, p_int): # real signature unknown; restored from __doc__
        """ QHttpRequestHeader.parseLine(str, int) -> bool """
        return False

    def path(self): # real signature unknown; restored from __doc__
        """ QHttpRequestHeader.path() -> str """
        return ""

    def setRequest(self, p_str, p_str_1, int_major=1, int_minor=1): # real signature unknown; restored from __doc__
        """ QHttpRequestHeader.setRequest(str, str, int major=1, int minor=1) """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ QHttpRequestHeader.toString() -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


