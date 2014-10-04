# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


class QLibraryInfo(): # skipped bases: <class 'sip.simplewrapper'>
    # no doc
    def buildDate(self): # real signature unknown; restored from __doc__
        """ QLibraryInfo.buildDate() -> QDate """
        return QDate

    def buildKey(self): # real signature unknown; restored from __doc__
        """ QLibraryInfo.buildKey() -> str """
        return ""

    def licensedProducts(self): # real signature unknown; restored from __doc__
        """ QLibraryInfo.licensedProducts() -> str """
        return ""

    def licensee(self): # real signature unknown; restored from __doc__
        """ QLibraryInfo.licensee() -> str """
        return ""

    def location(self, QLibraryInfo_LibraryLocation): # real signature unknown; restored from __doc__
        """ QLibraryInfo.location(QLibraryInfo.LibraryLocation) -> str """
        return ""

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BinariesPath = 4
    DataPath = 6
    DemosPath = 9
    DocumentationPath = 1
    ExamplesPath = 10
    HeadersPath = 2
    ImportsPath = 11
    LibrariesPath = 3
    LibraryLocation = None # (!) real value is ''
    PluginsPath = 5
    PrefixPath = 0
    SettingsPath = 8
    TranslationsPath = 7


