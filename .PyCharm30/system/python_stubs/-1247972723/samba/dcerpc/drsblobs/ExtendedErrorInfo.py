# encoding: utf-8
# module samba.dcerpc.drsblobs
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/drsblobs.so
# by generator 1.135
""" drsblobs DCE/RPC """

# imports
import dcerpc as __dcerpc
import talloc as __talloc


class ExtendedErrorInfo(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ndr_pack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_pack(object) -> blob
        NDR pack
        """
        pass

    def __ndr_print__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_print(object) -> None
        NDR print
        """
        pass

    def __ndr_unpack__(self, *args, **kwargs): # real signature unknown
        """
        S.ndr_unpack(class, blob, allow_remaining=False) -> None
        NDR unpack
        """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    computer_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    detection_location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    generating_component = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_params = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    params = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



