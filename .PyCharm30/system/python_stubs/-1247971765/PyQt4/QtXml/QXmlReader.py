# encoding: utf-8
# module PyQt4.QtXml
# from /usr/lib/python3/dist-packages/PyQt4/QtXml.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc
# no imports

class QXmlReader(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QXmlReader()
    QXmlReader(QXmlReader)
    """
    def contentHandler(self): # real signature unknown; restored from __doc__
        """ QXmlReader.contentHandler() -> QXmlContentHandler """
        return QXmlContentHandler

    def declHandler(self): # real signature unknown; restored from __doc__
        """ QXmlReader.declHandler() -> QXmlDeclHandler """
        return QXmlDeclHandler

    def DTDHandler(self): # real signature unknown; restored from __doc__
        """ QXmlReader.DTDHandler() -> QXmlDTDHandler """
        return QXmlDTDHandler

    def entityResolver(self): # real signature unknown; restored from __doc__
        """ QXmlReader.entityResolver() -> QXmlEntityResolver """
        return QXmlEntityResolver

    def errorHandler(self): # real signature unknown; restored from __doc__
        """ QXmlReader.errorHandler() -> QXmlErrorHandler """
        return QXmlErrorHandler

    def feature(self, p_str): # real signature unknown; restored from __doc__
        """ QXmlReader.feature(str) -> (bool, bool) """
        pass

    def hasFeature(self, p_str): # real signature unknown; restored from __doc__
        """ QXmlReader.hasFeature(str) -> bool """
        return False

    def hasProperty(self, p_str): # real signature unknown; restored from __doc__
        """ QXmlReader.hasProperty(str) -> bool """
        return False

    def lexicalHandler(self): # real signature unknown; restored from __doc__
        """ QXmlReader.lexicalHandler() -> QXmlLexicalHandler """
        return QXmlLexicalHandler

    def parse(self, QXmlInputSource): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlReader.parse(QXmlInputSource) -> bool
        QXmlReader.parse(QXmlInputSource) -> bool
        """
        return False

    def property(self, p_str): # real signature unknown; restored from __doc__
        """ QXmlReader.property(str) -> (sip.voidptr, bool) """
        pass

    def setContentHandler(self, QXmlContentHandler): # real signature unknown; restored from __doc__
        """ QXmlReader.setContentHandler(QXmlContentHandler) """
        pass

    def setDeclHandler(self, QXmlDeclHandler): # real signature unknown; restored from __doc__
        """ QXmlReader.setDeclHandler(QXmlDeclHandler) """
        pass

    def setDTDHandler(self, QXmlDTDHandler): # real signature unknown; restored from __doc__
        """ QXmlReader.setDTDHandler(QXmlDTDHandler) """
        pass

    def setEntityResolver(self, QXmlEntityResolver): # real signature unknown; restored from __doc__
        """ QXmlReader.setEntityResolver(QXmlEntityResolver) """
        pass

    def setErrorHandler(self, QXmlErrorHandler): # real signature unknown; restored from __doc__
        """ QXmlReader.setErrorHandler(QXmlErrorHandler) """
        pass

    def setFeature(self, p_str, bool): # real signature unknown; restored from __doc__
        """ QXmlReader.setFeature(str, bool) """
        pass

    def setLexicalHandler(self, QXmlLexicalHandler): # real signature unknown; restored from __doc__
        """ QXmlReader.setLexicalHandler(QXmlLexicalHandler) """
        pass

    def setProperty(self, p_str, sip_voidptr): # real signature unknown; restored from __doc__
        """ QXmlReader.setProperty(str, sip.voidptr) """
        pass

    def __init__(self, QXmlReader=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



