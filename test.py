import ctypes
lib = ctypes.CDLL('libflibex.dylib')

lib.init_()

ptr = ctypes.c_void_p(0)
lib.getpointer_(ctypes.byref(ptr))
print(ptr)

# cast
dary = ctypes.cast(ptr, ctypes.POINTER(ctypes.c_float))

import numpy

# create a numpy array that shares the same address as the fortran array
ary = numpy.ctypeslib.as_array(dary, shape=(20, 10))
print(ary)



