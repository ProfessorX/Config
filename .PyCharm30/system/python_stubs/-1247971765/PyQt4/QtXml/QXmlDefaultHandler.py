# encoding: utf-8
# module PyQt4.QtXml
# from /usr/lib/python3/dist-packages/PyQt4/QtXml.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc
# no imports

from .QXmlContentHandler import QXmlContentHandler

from .QXmlErrorHandler import QXmlErrorHandler

from .QXmlDTDHandler import QXmlDTDHandler

from .QXmlEntityResolver import QXmlEntityResolver

from .QXmlLexicalHandler import QXmlLexicalHandler

from .QXmlDeclHandler import QXmlDeclHandler

class QXmlDefaultHandler(QXmlContentHandler, QXmlErrorHandler, QXmlDTDHandler, QXmlEntityResolver, QXmlLexicalHandler, QXmlDeclHandler):
    """ QXmlDefaultHandler() """
    def attributeDecl(self, p_str, p_str_1, p_str_2, p_str_3, p_str_4): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.attributeDecl(str, str, str, str, str) -> bool """
        return False

    def characters(self, p_str): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.characters(str) -> bool """
        return False

    def comment(self, p_str): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.comment(str) -> bool """
        return False

    def endCDATA(self): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.endCDATA() -> bool """
        return False

    def endDocument(self): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.endDocument() -> bool """
        return False

    def endDTD(self): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.endDTD() -> bool """
        return False

    def endElement(self, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.endElement(str, str, str) -> bool """
        return False

    def endEntity(self, p_str): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.endEntity(str) -> bool """
        return False

    def endPrefixMapping(self, p_str): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.endPrefixMapping(str) -> bool """
        return False

    def error(self, QXmlParseException): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.error(QXmlParseException) -> bool """
        return False

    def errorString(self): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.errorString() -> str """
        return ""

    def externalEntityDecl(self, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.externalEntityDecl(str, str, str) -> bool """
        return False

    def fatalError(self, QXmlParseException): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.fatalError(QXmlParseException) -> bool """
        return False

    def ignorableWhitespace(self, p_str): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.ignorableWhitespace(str) -> bool """
        return False

    def internalEntityDecl(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.internalEntityDecl(str, str) -> bool """
        return False

    def notationDecl(self, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.notationDecl(str, str, str) -> bool """
        return False

    def processingInstruction(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.processingInstruction(str, str) -> bool """
        return False

    def resolveEntity(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.resolveEntity(str, str) -> (bool, QXmlInputSource) """
        pass

    def setDocumentLocator(self, QXmlLocator): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.setDocumentLocator(QXmlLocator) """
        pass

    def skippedEntity(self, p_str): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.skippedEntity(str) -> bool """
        return False

    def startCDATA(self): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.startCDATA() -> bool """
        return False

    def startDocument(self): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.startDocument() -> bool """
        return False

    def startDTD(self, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.startDTD(str, str, str) -> bool """
        return False

    def startElement(self, p_str, p_str_1, p_str_2, QXmlAttributes): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.startElement(str, str, str, QXmlAttributes) -> bool """
        return False

    def startEntity(self, p_str): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.startEntity(str) -> bool """
        return False

    def startPrefixMapping(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.startPrefixMapping(str, str) -> bool """
        return False

    def unparsedEntityDecl(self, p_str, p_str_1, p_str_2, p_str_3): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.unparsedEntityDecl(str, str, str, str) -> bool """
        return False

    def warning(self, QXmlParseException): # real signature unknown; restored from __doc__
        """ QXmlDefaultHandler.warning(QXmlParseException) -> bool """
        return False

    def __init__(self): # real signature unknown; restored from __doc__
        pass


