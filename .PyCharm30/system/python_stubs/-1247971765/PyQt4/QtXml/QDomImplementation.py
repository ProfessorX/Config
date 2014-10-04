# encoding: utf-8
# module PyQt4.QtXml
# from /usr/lib/python3/dist-packages/PyQt4/QtXml.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc
# no imports

class QDomImplementation(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QDomImplementation()
    QDomImplementation(QDomImplementation)
    """
    def createDocument(self, p_str, p_str_1, QDomDocumentType): # real signature unknown; restored from __doc__
        """ QDomImplementation.createDocument(str, str, QDomDocumentType) -> QDomDocument """
        return QDomDocument

    def createDocumentType(self, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
        """ QDomImplementation.createDocumentType(str, str, str) -> QDomDocumentType """
        return QDomDocumentType

    def hasFeature(self, p_str, p_str_1): # real signature unknown; restored from __doc__
        """ QDomImplementation.hasFeature(str, str) -> bool """
        return False

    def invalidDataPolicy(self): # real signature unknown; restored from __doc__
        """ QDomImplementation.invalidDataPolicy() -> QDomImplementation.InvalidDataPolicy """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ QDomImplementation.isNull() -> bool """
        return False

    def setInvalidDataPolicy(self, QDomImplementation_InvalidDataPolicy): # real signature unknown; restored from __doc__
        """ QDomImplementation.setInvalidDataPolicy(QDomImplementation.InvalidDataPolicy) """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, QDomImplementation=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AcceptInvalidChars = 0
    DropInvalidChars = 1
    InvalidDataPolicy = None # (!) real value is ''
    ReturnNullNode = 2
    __hash__ = None


