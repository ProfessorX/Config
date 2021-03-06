# encoding: utf-8
# module _imp
# from (built-in)
# by generator 1.135
""" (Extremely) low-level import machinery bits as used by importlib and imp. """
# no imports

# functions

def acquire_lock(*args, **kwargs): # real signature unknown
    """
    Acquires the interpreter's import lock for the current thread.
    
    This lock should be used by import hooks to ensure thread-safety when importing
    modules. On platforms without threads, this function does nothing.
    """
    pass

def extension_suffixes(*args, **kwargs): # real signature unknown
    """ Returns the list of file suffixes used to identify extension modules. """
    pass

def get_frozen_object(*args, **kwargs): # real signature unknown
    """ Create a code object for a frozen module. """
    pass

def init_builtin(*args, **kwargs): # real signature unknown
    """ Initializes a built-in module. """
    pass

def init_frozen(*args, **kwargs): # real signature unknown
    """ Initializes a frozen module. """
    pass

def is_builtin(*args, **kwargs): # real signature unknown
    """ Returns True if the module name corresponds to a built-in module. """
    pass

def is_frozen(*args, **kwargs): # real signature unknown
    """ Returns True if the module name corresponds to a frozen module. """
    pass

def is_frozen_package(*args, **kwargs): # real signature unknown
    """ Returns True if the module name is of a frozen package. """
    pass

def load_dynamic(*args, **kwargs): # real signature unknown
    """ Loads an extension module. """
    pass

def lock_held(*args, **kwargs): # real signature unknown
    """
    Return True if the import lock is currently held, else False.
    
    On platforms without threads, return False.
    """
    pass

def release_lock(*args, **kwargs): # real signature unknown
    """
    Release the interpreter's import lock.
    
    On platforms without threads, this function does nothing.
    """
    pass

def _fix_co_filename(*args, **kwargs): # real signature unknown
    """
    Changes code.co_filename to specify the passed-in file path.
    
      code
        Code object to change.
      path
        File path to use.
    """
    pass

# classes

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

