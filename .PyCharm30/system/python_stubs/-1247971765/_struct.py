# encoding: utf-8
# module _struct
# from (built-in)
# by generator 1.135
"""
Functions to convert between Python values and C structs.
Python bytes objects are used to hold the data representing the C struct
and also as format strings (explained below) to describe the layout of data
in the C struct.

The optional first format char indicates byte order, size and alignment:
  @: native order, size & alignment (default)
  =: native order, std. size & alignment
  <: little-endian, std. size & alignment
  >: big-endian, std. size & alignment
  !: same as >

The remaining chars indicate types of args and must match exactly;
these can be preceded by a decimal repeat count:
  x: pad byte (no data); c:char; b:signed byte; B:unsigned byte;
  ?: _Bool (requires C99; if not available, char is used instead)
  h:short; H:unsigned short; i:int; I:unsigned int;
  l:long; L:unsigned long; f:float; d:double.
Special cases (preceding decimal count indicates length):
  s:string (array of char); p: pascal string (with count byte).
Special cases (only available in native format):
  n:ssize_t; N:size_t;
  P:an integer type that is wide enough to hold a pointer.
Special case (not in native mode unless 'long long' in platform C):
  q:long long; Q:unsigned long long
Whitespace between formats is ignored.

The variable struct.error is an exception raised on errors.
"""
# no imports

# functions

def calcsize(fmt): # known case of _struct.calcsize
    """
    calcsize(fmt) -> integer
    
    Return size in bytes of the struct described by the format string fmt.
    """
    return 0

def iter_unpack(fmt, buffer): # real signature unknown; restored from __doc__
    """
    iter_unpack(fmt, buffer) -> iterator(v1, v2, ...)
    
    Return an iterator yielding tuples unpacked from the given bytes
    source according to the format string, like a repeated invocation of
    unpack_from().  Requires that the bytes length be a multiple of the
    format struct size.
    """
    pass

def pack(fmt, *args): # known case of _struct.pack
    """
    pack(fmt, v1, v2, ...) -> bytes
    
    Return a bytes object containing the values v1, v2, ... packed according
    to the format string fmt.  See help(struct) for more on format strings.
    """
    return b""

def pack_into(fmt, buffer, offset, *args): # known case of _struct.pack_into
    """
    pack_into(fmt, buffer, offset, v1, v2, ...)
    
    Pack the values v1, v2, ... according to the format string fmt and write
    the packed bytes into the writable buffer buf starting at offset.  Note
    that the offset is a required argument.  See help(struct) for more
    on format strings.
    """
    pass

def unpack(fmt, string): # known case of _struct.unpack
    """
    unpack(fmt, buffer) -> (v1, v2, ...)
    
    Return a tuple containing values unpacked according to the format string
    fmt.  Requires len(buffer) == calcsize(fmt). See help(struct) for more
    on format strings.
    """
    pass

def unpack_from(fmt, buffer, offset=0): # known case of _struct.unpack_from
    """
    unpack_from(fmt, buffer, offset=0) -> (v1, v2, ...)
    
    Return a tuple containing values unpacked according to the format string
    fmt.  Requires len(buffer[offset:]) >= calcsize(fmt).  See help(struct)
    for more on format strings.
    """
    pass

def _clearcache(*args, **kwargs): # real signature unknown
    """ Clear the internal cache. """
    pass

# classes

from .Exception import Exception

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



from .object import object

class Struct(object):
    """
    Struct(fmt) --> compiled struct object
    
    Return a new Struct object which writes and reads binary data according to
    the format string fmt.  See help(struct) for more on format strings.
    """
    def iter_unpack(self, buffer): # real signature unknown; restored from __doc__
        """
        S.iter_unpack(buffer) -> iterator(v1, v2, ...)
        
        Return an iterator yielding tuples unpacked from the given bytes
        source, like a repeated invocation of unpack_from().  Requires
        that the bytes length be a multiple of the struct size.
        """
        pass

    def pack(self, *args): # known case of _struct.Struct.pack
        """
        S.pack(v1, v2, ...) -> bytes
        
        Return a bytes object containing values v1, v2, ... packed according
        to the format string S.format.  See help(struct) for more on format
        strings.
        """
        return b""

    def pack_into(self, buffer, offset, *args): # known case of _struct.Struct.pack_into
        """
        S.pack_into(buffer, offset, v1, v2, ...)
        
        Pack the values v1, v2, ... according to the format string S.format
        and write the packed bytes into the writable buffer buf starting at
        offset.  Note that the offset is a required argument.  See
        help(struct) for more on format strings.
        """
        pass

    def unpack(self, string): # known case of _struct.Struct.unpack
        """
        S.unpack(buffer) -> (v1, v2, ...)
        
        Return a tuple containing values unpacked according to the format
        string S.format.  Requires len(buffer) == S.size.  See help(struct)
        for more on format strings.
        """
        pass

    def unpack_from(self, buffer, offset=0): # known case of _struct.Struct.unpack_from
        """
        S.unpack_from(buffer, offset=0) -> (v1, v2, ...)
        
        Return a tuple containing values unpacked according to the format
        string S.format.  Requires len(buffer[offset:]) >= S.size.  See
        help(struct) for more on format strings.
        """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, fmt): # known case of _struct.Struct.__init__
        """
        Struct(fmt) --> compiled struct object
        
        Return a new Struct object which writes and reads binary data according to
        the format string fmt.  See help(struct) for more on format strings.
        # (copied from class doc)
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ S.__sizeof__() -> size of S in memory, in bytes """
        pass

    format = property(lambda self: '')
    """struct format string

    :type: string
    """

    size = property(lambda self: 0)
    """struct size in bytes

    :type: int
    """



from .object import object

class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """ Load a built-in module. """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


# variables with complex values

__spec__ = None # (!) real value is ''

