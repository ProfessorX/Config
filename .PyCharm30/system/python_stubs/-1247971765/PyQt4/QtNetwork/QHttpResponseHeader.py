# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib/python3/dist-packages/PyQt4/QtNetwork.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from .QHttpHeader import QHttpHeader

class QHttpResponseHeader(QHttpHeader):
    """
    QHttpResponseHeader()
    QHttpResponseHeader(QHttpResponseHeader)
    QHttpResponseHeader(str)
    QHttpResponseHeader(int, str text='', int major=1, int minor=1)
    """
    def majorVersion(self): # real signature unknown; restored from __doc__
        """ QHttpResponseHeader.majorVersion() -> int """
        return 0

    def minorVersion(self): # real signature unknown; restored from __doc__
        """ QHttpResponseHeader.minorVersion() -> int """
        return 0

    def parseLine(self, p_str, p_int): # real signature unknown; restored from __doc__
        """ QHttpResponseHeader.parseLine(str, int) -> bool """
        return False

    def reasonPhrase(self): # real signature unknown; restored from __doc__
        """ QHttpResponseHeader.reasonPhrase() -> str """
        return ""

    def setStatusLine(self, p_int, str_text='', int_major=1, int_minor=1): # real signature unknown; restored from __doc__
        """ QHttpResponseHeader.setStatusLine(int, str text='', int major=1, int minor=1) """
        pass

    def statusCode(self): # real signature unknown; restored from __doc__
        """ QHttpResponseHeader.statusCode() -> int """
        return 0

    def toString(self): # real signature unknown; restored from __doc__
        """ QHttpResponseHeader.toString() -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


