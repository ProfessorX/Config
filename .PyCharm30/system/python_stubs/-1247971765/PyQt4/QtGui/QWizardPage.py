# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from .QWidget import QWidget

class QWizardPage(QWidget):
    """ QWizardPage(QWidget parent=None) """
    def buttonText(self, QWizard_WizardButton): # real signature unknown; restored from __doc__
        """ QWizardPage.buttonText(QWizard.WizardButton) -> str """
        return ""

    def cleanupPage(self): # real signature unknown; restored from __doc__
        """ QWizardPage.cleanupPage() """
        pass

    def completeChanged(self, *args, **kwargs): # real signature unknown
        """ QWizardPage.completeChanged [signal] """
        pass

    def field(self, p_str): # real signature unknown; restored from __doc__
        """ QWizardPage.field(str) -> object """
        return object()

    def initializePage(self): # real signature unknown; restored from __doc__
        """ QWizardPage.initializePage() """
        pass

    def isCommitPage(self): # real signature unknown; restored from __doc__
        """ QWizardPage.isCommitPage() -> bool """
        return False

    def isComplete(self): # real signature unknown; restored from __doc__
        """ QWizardPage.isComplete() -> bool """
        return False

    def isFinalPage(self): # real signature unknown; restored from __doc__
        """ QWizardPage.isFinalPage() -> bool """
        return False

    def nextId(self): # real signature unknown; restored from __doc__
        """ QWizardPage.nextId() -> int """
        return 0

    def pixmap(self, QWizard_WizardPixmap): # real signature unknown; restored from __doc__
        """ QWizardPage.pixmap(QWizard.WizardPixmap) -> QPixmap """
        return QPixmap

    def registerField(self, p_str, QWidget, str_property=None, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QWizardPage.registerField(str, QWidget, str property=None, signal changedSignal=0)
        QWizardPage.registerField(str, QWidget, str property=None, SIGNAL() changedSignal=0)
        """
        pass

    def setButtonText(self, QWizard_WizardButton, p_str): # real signature unknown; restored from __doc__
        """ QWizardPage.setButtonText(QWizard.WizardButton, str) """
        pass

    def setCommitPage(self, bool): # real signature unknown; restored from __doc__
        """ QWizardPage.setCommitPage(bool) """
        pass

    def setField(self, p_str, p_object): # real signature unknown; restored from __doc__
        """ QWizardPage.setField(str, object) """
        pass

    def setFinalPage(self, bool): # real signature unknown; restored from __doc__
        """ QWizardPage.setFinalPage(bool) """
        pass

    def setPixmap(self, QWizard_WizardPixmap, QPixmap): # real signature unknown; restored from __doc__
        """ QWizardPage.setPixmap(QWizard.WizardPixmap, QPixmap) """
        pass

    def setSubTitle(self, p_str): # real signature unknown; restored from __doc__
        """ QWizardPage.setSubTitle(str) """
        pass

    def setTitle(self, p_str): # real signature unknown; restored from __doc__
        """ QWizardPage.setTitle(str) """
        pass

    def subTitle(self): # real signature unknown; restored from __doc__
        """ QWizardPage.subTitle() -> str """
        return ""

    def title(self): # real signature unknown; restored from __doc__
        """ QWizardPage.title() -> str """
        return ""

    def validatePage(self): # real signature unknown; restored from __doc__
        """ QWizardPage.validatePage() -> bool """
        return False

    def wizard(self): # real signature unknown; restored from __doc__
        """ QWizardPage.wizard() -> QWizard """
        return QWizard

    def __init__(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        pass


