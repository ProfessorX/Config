# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


class QXmlStreamWriter(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QXmlStreamWriter()
    QXmlStreamWriter(QIODevice)
    QXmlStreamWriter(QByteArray)
    """
    def autoFormatting(self): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.autoFormatting() -> bool """
        return False

    def autoFormattingIndent(self): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.autoFormattingIndent() -> int """
        return 0

    def codec(self): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.codec() -> QTextCodec """
        return QTextCodec

    def device(self): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.device() -> QIODevice """
        return QIODevice

    def hasError(self): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.hasError() -> bool """
        return False

    def setAutoFormatting(self, bool): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.setAutoFormatting(bool) """
        pass

    def setAutoFormattingIndent(self, p_int): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.setAutoFormattingIndent(int) """
        pass

    def setCodec(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlStreamWriter.setCodec(QTextCodec)
        QXmlStreamWriter.setCodec(str)
        """
        pass

    def setDevice(self, QIODevice): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.setDevice(QIODevice) """
        pass

    def writeAttribute(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlStreamWriter.writeAttribute(str, str)
        QXmlStreamWriter.writeAttribute(str, str, str)
        QXmlStreamWriter.writeAttribute(QXmlStreamAttribute)
        """
        pass

    def writeAttributes(self, QXmlStreamAttributes): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeAttributes(QXmlStreamAttributes) """
        pass

    def writeCDATA(self, p_str): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeCDATA(str) """
        pass

    def writeCharacters(self, p_str): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeCharacters(str) """
        pass

    def writeComment(self, p_str): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeComment(str) """
        pass

    def writeCurrentToken(self, QXmlStreamReader): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeCurrentToken(QXmlStreamReader) """
        pass

    def writeDefaultNamespace(self, p_str): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeDefaultNamespace(str) """
        pass

    def writeDTD(self, p_str): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeDTD(str) """
        pass

    def writeEmptyElement(self, p_str, p_str_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlStreamWriter.writeEmptyElement(str)
        QXmlStreamWriter.writeEmptyElement(str, str)
        """
        pass

    def writeEndDocument(self): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeEndDocument() """
        pass

    def writeEndElement(self): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeEndElement() """
        pass

    def writeEntityReference(self, p_str): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeEntityReference(str) """
        pass

    def writeNamespace(self, p_str, str_prefix=''): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeNamespace(str, str prefix='') """
        pass

    def writeProcessingInstruction(self, p_str, str_data=''): # real signature unknown; restored from __doc__
        """ QXmlStreamWriter.writeProcessingInstruction(str, str data='') """
        pass

    def writeStartDocument(self, p_str=None, bool=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlStreamWriter.writeStartDocument()
        QXmlStreamWriter.writeStartDocument(str)
        QXmlStreamWriter.writeStartDocument(str, bool)
        """
        pass

    def writeStartElement(self, p_str, p_str_1=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlStreamWriter.writeStartElement(str)
        QXmlStreamWriter.writeStartElement(str, str)
        """
        pass

    def writeTextElement(self, p_str, p_str_1, p_str_2=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QXmlStreamWriter.writeTextElement(str, str)
        QXmlStreamWriter.writeTextElement(str, str, str)
        """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



