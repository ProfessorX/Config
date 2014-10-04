# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib/python3/dist-packages/PyQt4/QtGui.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QGradient(): # skipped bases: <class 'sip.simplewrapper'>
    """
    QGradient()
    QGradient(QGradient)
    """
    def coordinateMode(self): # real signature unknown; restored from __doc__
        """ QGradient.coordinateMode() -> QGradient.CoordinateMode """
        pass

    def setColorAt(self, p_float, QColor): # real signature unknown; restored from __doc__
        """ QGradient.setColorAt(float, QColor) """
        pass

    def setCoordinateMode(self, QGradient_CoordinateMode): # real signature unknown; restored from __doc__
        """ QGradient.setCoordinateMode(QGradient.CoordinateMode) """
        pass

    def setSpread(self, QGradient_Spread): # real signature unknown; restored from __doc__
        """ QGradient.setSpread(QGradient.Spread) """
        pass

    def setStops(self, list_of_tuple_of_float_QColor): # real signature unknown; restored from __doc__
        """ QGradient.setStops(list-of-tuple-of-float-QColor) """
        pass

    def spread(self): # real signature unknown; restored from __doc__
        """ QGradient.spread() -> QGradient.Spread """
        pass

    def stops(self): # real signature unknown; restored from __doc__
        """ QGradient.stops() -> list-of-tuple-of-float-QColor """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ QGradient.type() -> QGradient.Type """
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

    def __init__(self, QGradient=None): # real signature unknown; restored from __doc__ with multiple overloads
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


    ConicalGradient = 2
    CoordinateMode = None # (!) real value is ''
    LinearGradient = 0
    LogicalMode = 0
    NoGradient = 3
    ObjectBoundingMode = 2
    PadSpread = 0
    RadialGradient = 1
    ReflectSpread = 1
    RepeatSpread = 2
    Spread = None # (!) real value is ''
    StretchToDeviceMode = 1
    Type = None # (!) real value is ''
    __hash__ = None


