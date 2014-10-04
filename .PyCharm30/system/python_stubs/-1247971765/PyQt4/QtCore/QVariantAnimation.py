# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


from .QAbstractAnimation import QAbstractAnimation

class QVariantAnimation(QAbstractAnimation):
    """ QVariantAnimation(QObject parent=None) """
    def currentValue(self): # real signature unknown; restored from __doc__
        """ QVariantAnimation.currentValue() -> object """
        return object()

    def duration(self): # real signature unknown; restored from __doc__
        """ QVariantAnimation.duration() -> int """
        return 0

    def easingCurve(self): # real signature unknown; restored from __doc__
        """ QVariantAnimation.easingCurve() -> QEasingCurve """
        return QEasingCurve

    def endValue(self): # real signature unknown; restored from __doc__
        """ QVariantAnimation.endValue() -> object """
        return object()

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QVariantAnimation.event(QEvent) -> bool """
        return False

    def interpolated(self, p_object, p_object_1, p_float): # real signature unknown; restored from __doc__
        """ QVariantAnimation.interpolated(object, object, float) -> object """
        return object()

    def keyValueAt(self, p_float): # real signature unknown; restored from __doc__
        """ QVariantAnimation.keyValueAt(float) -> object """
        return object()

    def keyValues(self): # real signature unknown; restored from __doc__
        """ QVariantAnimation.keyValues() -> list-of-tuple-of-float-QVariant """
        pass

    def setDuration(self, p_int): # real signature unknown; restored from __doc__
        """ QVariantAnimation.setDuration(int) """
        pass

    def setEasingCurve(self, QEasingCurve): # real signature unknown; restored from __doc__
        """ QVariantAnimation.setEasingCurve(QEasingCurve) """
        pass

    def setEndValue(self, p_object): # real signature unknown; restored from __doc__
        """ QVariantAnimation.setEndValue(object) """
        pass

    def setKeyValueAt(self, p_float, p_object): # real signature unknown; restored from __doc__
        """ QVariantAnimation.setKeyValueAt(float, object) """
        pass

    def setKeyValues(self, list_of_tuple_of_float_QVariant): # real signature unknown; restored from __doc__
        """ QVariantAnimation.setKeyValues(list-of-tuple-of-float-QVariant) """
        pass

    def setStartValue(self, p_object): # real signature unknown; restored from __doc__
        """ QVariantAnimation.setStartValue(object) """
        pass

    def startValue(self): # real signature unknown; restored from __doc__
        """ QVariantAnimation.startValue() -> object """
        return object()

    def updateCurrentTime(self, p_int): # real signature unknown; restored from __doc__
        """ QVariantAnimation.updateCurrentTime(int) """
        pass

    def updateCurrentValue(self, p_object): # real signature unknown; restored from __doc__
        """ QVariantAnimation.updateCurrentValue(object) """
        pass

    def updateState(self, QAbstractAnimation_State, QAbstractAnimation_State_1): # real signature unknown; restored from __doc__
        """ QVariantAnimation.updateState(QAbstractAnimation.State, QAbstractAnimation.State) """
        pass

    def valueChanged(self, *args, **kwargs): # real signature unknown
        """ QVariantAnimation.valueChanged[object] [signal] """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


