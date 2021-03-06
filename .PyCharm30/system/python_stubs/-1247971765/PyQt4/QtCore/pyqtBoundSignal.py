# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python3/dist-packages/PyQt4/QtCore.cpython-34m-x86_64-linux-gnu.so
# by generator 1.135
# no doc

# imports
import sip as __sip


from .object import object

class pyqtBoundSignal(object):
    def connect(self, slot, type=None, no_receiver_check=False): # real signature unknown; restored from __doc__
        """
        connect(slot, type=Qt.AutoConnection, no_receiver_check=False)
        
        slot is either a Python callable or another signal.
        type is a Qt.ConnectionType.
        no_receiver_check is True to disable the check that the receiver's C++
        instance still exists when the signal is emitted.
        """
        pass

    def disconnect(self, slot=None): # real signature unknown; restored from __doc__
        """
        disconnect([slot])
        
        slot is an optional Python callable or another signal.  If it is omitted
        then the signal is disconnected from everything it is connected to.
        """
        pass

    def emit(self, *args): # real signature unknown; restored from __doc__
        """
        emit(*args)
        
        *args are the values that will be passed as arguments to all connected
        slots.
        """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    signal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The signature of the signal that would be returned by SIGNAL()"""



