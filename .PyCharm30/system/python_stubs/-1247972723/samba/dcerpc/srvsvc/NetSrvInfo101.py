# encoding: utf-8
# module samba.dcerpc.srvsvc
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/srvsvc.so
# by generator 1.135
""" srvsvc DCE/RPC """

# imports
import dcerpc as __dcerpc
import talloc as __talloc


class NetSrvInfo101(__talloc.Object):
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

    comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    platform_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    server_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    server_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version_major = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version_minor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



