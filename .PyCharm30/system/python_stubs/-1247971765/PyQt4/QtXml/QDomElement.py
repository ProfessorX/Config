# encoding: utf-8
# module PyQt4.QtXml
# from /usr/lib/python3/dist-packages/PyQt4/QtXml.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc
# no imports

from .QDomNode import QDomNode

class QDomElement(QDomNode):
    """
    QDomElement()
    QDomElement(QDomElement)
    """
    def attribute(self, p_str, str_defaultValue=''): # real signature unknown; restored from __doc__
        """ QDomElement.attribute(str, str defaultValue='') -> str """
        return ""

    def attributeNode(self, p_str): # real signature unknown; restored from __doc__
        """ QDomElement.attributeNode(str) -> QDomAttr """
        return QDomAttr

    def attributeNodeNS(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QDomElement.attributeNodeNS(str, str) -> QDomAttr """
        return QDomAttr

    def attributeNS(self, p_str, p_str_1, str_defaultValue=''): # real signature unknown; restored from __doc__
        """ QDomElement.attributeNS(str, str, str defaultValue='') -> str """
        return ""

    def attributes(self): # real signature unknown; restored from __doc__
        """ QDomElement.attributes() -> QDomNamedNodeMap """
        return QDomNamedNodeMap

    def elementsByTagName(self, p_str): # real signature unknown; restored from __doc__
        """ QDomElement.elementsByTagName(str) -> QDomNodeList """
        return QDomNodeList

    def elementsByTagNameNS(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QDomElement.elementsByTagNameNS(str, str) -> QDomNodeList """
        return QDomNodeList

    def hasAttribute(self, p_str): # real signature unknown; restored from __doc__
        """ QDomElement.hasAttribute(str) -> bool """
        return False

    def hasAttributeNS(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QDomElement.hasAttributeNS(str, str) -> bool """
        return False

    def nodeType(self): # real signature unknown; restored from __doc__
        """ QDomElement.nodeType() -> QDomNode.NodeType """
        pass

    def removeAttribute(self, p_str): # real signature unknown; restored from __doc__
        """ QDomElement.removeAttribute(str) """
        pass

    def removeAttributeNode(self, QDomAttr): # real signature unknown; restored from __doc__
        """ QDomElement.removeAttributeNode(QDomAttr) -> QDomAttr """
        return QDomAttr

    def removeAttributeNS(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QDomElement.removeAttributeNS(str, str) """
        pass

    def setAttribute(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDomElement.setAttribute(str, str)
        QDomElement.setAttribute(str, int)
        QDomElement.setAttribute(str, int)
        QDomElement.setAttribute(str, float)
        QDomElement.setAttribute(str, int)
        """
        pass

    def setAttributeNode(self, QDomAttr): # real signature unknown; restored from __doc__
        """ QDomElement.setAttributeNode(QDomAttr) -> QDomAttr """
        return QDomAttr

    def setAttributeNodeNS(self, QDomAttr): # real signature unknown; restored from __doc__
        """ QDomElement.setAttributeNodeNS(QDomAttr) -> QDomAttr """
        return QDomAttr

    def setAttributeNS(self, p_str, p_str_1, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDomElement.setAttributeNS(str, str, str)
        QDomElement.setAttributeNS(str, str, int)
        QDomElement.setAttributeNS(str, str, int)
        QDomElement.setAttributeNS(str, str, float)
        QDomElement.setAttributeNS(str, str, int)
        """
        pass

    def setTagName(self, p_str): # real signature unknown; restored from __doc__
        """ QDomElement.setTagName(str) """
        pass

    def tagName(self): # real signature unknown; restored from __doc__
        """ QDomElement.tagName() -> str """
        return ""

    def text(self): # real signature unknown; restored from __doc__
        """ QDomElement.text() -> str """
        return ""

    def __init__(self, QDomElement=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass


