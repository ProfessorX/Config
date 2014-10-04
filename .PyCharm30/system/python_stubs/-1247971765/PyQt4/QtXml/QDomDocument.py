# encoding: utf-8
# module PyQt4.QtXml
# from /usr/lib/python3/dist-packages/PyQt4/QtXml.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc
# no imports

from .QDomNode import QDomNode

class QDomDocument(QDomNode):
    """
    QDomDocument()
    QDomDocument(str)
    QDomDocument(QDomDocumentType)
    QDomDocument(QDomDocument)
    """
    def createAttribute(self, p_str): # real signature unknown; restored from __doc__
        """ QDomDocument.createAttribute(str) -> QDomAttr """
        return QDomAttr

    def createAttributeNS(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QDomDocument.createAttributeNS(str, str) -> QDomAttr """
        return QDomAttr

    def createCDATASection(self, p_str): # real signature unknown; restored from __doc__
        """ QDomDocument.createCDATASection(str) -> QDomCDATASection """
        return QDomCDATASection

    def createComment(self, p_str): # real signature unknown; restored from __doc__
        """ QDomDocument.createComment(str) -> QDomComment """
        return QDomComment

    def createDocumentFragment(self): # real signature unknown; restored from __doc__
        """ QDomDocument.createDocumentFragment() -> QDomDocumentFragment """
        return QDomDocumentFragment

    def createElement(self, p_str): # real signature unknown; restored from __doc__
        """ QDomDocument.createElement(str) -> QDomElement """
        return QDomElement

    def createElementNS(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QDomDocument.createElementNS(str, str) -> QDomElement """
        return QDomElement

    def createEntityReference(self, p_str): # real signature unknown; restored from __doc__
        """ QDomDocument.createEntityReference(str) -> QDomEntityReference """
        return QDomEntityReference

    def createProcessingInstruction(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QDomDocument.createProcessingInstruction(str, str) -> QDomProcessingInstruction """
        return QDomProcessingInstruction

    def createTextNode(self, p_str): # real signature unknown; restored from __doc__
        """ QDomDocument.createTextNode(str) -> QDomText """
        return QDomText

    def doctype(self): # real signature unknown; restored from __doc__
        """ QDomDocument.doctype() -> QDomDocumentType """
        return QDomDocumentType

    def documentElement(self): # real signature unknown; restored from __doc__
        """ QDomDocument.documentElement() -> QDomElement """
        return QDomElement

    def elementById(self, p_str): # real signature unknown; restored from __doc__
        """ QDomDocument.elementById(str) -> QDomElement """
        return QDomElement

    def elementsByTagName(self, p_str): # real signature unknown; restored from __doc__
        """ QDomDocument.elementsByTagName(str) -> QDomNodeList """
        return QDomNodeList

    def elementsByTagNameNS(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QDomDocument.elementsByTagNameNS(str, str) -> QDomNodeList """
        return QDomNodeList

    def implementation(self): # real signature unknown; restored from __doc__
        """ QDomDocument.implementation() -> QDomImplementation """
        return QDomImplementation

    def importNode(self, QDomNode, bool): # real signature unknown; restored from __doc__
        """ QDomDocument.importNode(QDomNode, bool) -> QDomNode """
        return QDomNode

    def nodeType(self): # real signature unknown; restored from __doc__
        """ QDomDocument.nodeType() -> QDomNode.NodeType """
        pass

    def setContent(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QDomDocument.setContent(QByteArray, bool) -> (bool, str, int, int)
        QDomDocument.setContent(str, bool) -> (bool, str, int, int)
        QDomDocument.setContent(QIODevice, bool) -> (bool, str, int, int)
        QDomDocument.setContent(QXmlInputSource, bool) -> (bool, str, int, int)
        QDomDocument.setContent(QByteArray) -> (bool, str, int, int)
        QDomDocument.setContent(str) -> (bool, str, int, int)
        QDomDocument.setContent(QIODevice) -> (bool, str, int, int)
        QDomDocument.setContent(QXmlInputSource, QXmlReader) -> (bool, str, int, int)
        """
        pass

    def toByteArray(self, int_indent=1): # real signature unknown; restored from __doc__
        """ QDomDocument.toByteArray(int indent=1) -> QByteArray """
        pass

    def toString(self, int_indent=1): # real signature unknown; restored from __doc__
        """ QDomDocument.toString(int indent=1) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


