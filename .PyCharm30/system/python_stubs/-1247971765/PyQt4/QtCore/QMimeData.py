# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


from .QObject import QObject

class QMimeData(QObject):
    """ QMimeData() """
    def clear(self): # real signature unknown; restored from __doc__
        """ QMimeData.clear() """
        pass

    def colorData(self): # real signature unknown; restored from __doc__
        """ QMimeData.colorData() -> object """
        return object()

    def data(self, p_str): # real signature unknown; restored from __doc__
        """ QMimeData.data(str) -> QByteArray """
        return QByteArray

    def formats(self): # real signature unknown; restored from __doc__
        """ QMimeData.formats() -> list-of-str """
        pass

    def hasColor(self): # real signature unknown; restored from __doc__
        """ QMimeData.hasColor() -> bool """
        return False

    def hasFormat(self, p_str): # real signature unknown; restored from __doc__
        """ QMimeData.hasFormat(str) -> bool """
        return False

    def hasHtml(self): # real signature unknown; restored from __doc__
        """ QMimeData.hasHtml() -> bool """
        return False

    def hasImage(self): # real signature unknown; restored from __doc__
        """ QMimeData.hasImage() -> bool """
        return False

    def hasText(self): # real signature unknown; restored from __doc__
        """ QMimeData.hasText() -> bool """
        return False

    def hasUrls(self): # real signature unknown; restored from __doc__
        """ QMimeData.hasUrls() -> bool """
        return False

    def html(self): # real signature unknown; restored from __doc__
        """ QMimeData.html() -> str """
        return ""

    def imageData(self): # real signature unknown; restored from __doc__
        """ QMimeData.imageData() -> object """
        return object()

    def removeFormat(self, p_str): # real signature unknown; restored from __doc__
        """ QMimeData.removeFormat(str) """
        pass

    def retrieveData(self, p_str, Type): # real signature unknown; restored from __doc__
        """ QMimeData.retrieveData(str, Type) -> object """
        return object()

    def setColorData(self, p_object): # real signature unknown; restored from __doc__
        """ QMimeData.setColorData(object) """
        pass

    def setData(self, p_str, QByteArray): # real signature unknown; restored from __doc__
        """ QMimeData.setData(str, QByteArray) """
        pass

    def setHtml(self, p_str): # real signature unknown; restored from __doc__
        """ QMimeData.setHtml(str) """
        pass

    def setImageData(self, p_object): # real signature unknown; restored from __doc__
        """ QMimeData.setImageData(object) """
        pass

    def setText(self, p_str): # real signature unknown; restored from __doc__
        """ QMimeData.setText(str) """
        pass

    def setUrls(self, list_of_QUrl): # real signature unknown; restored from __doc__
        """ QMimeData.setUrls(list-of-QUrl) """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ QMimeData.text() -> str """
        return ""

    def urls(self): # real signature unknown; restored from __doc__
        """ QMimeData.urls() -> list-of-QUrl """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass


