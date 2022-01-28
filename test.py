import ctypes
lib = ctypes.CDLL('libflibex.dylib')

lib.init_()

ptr = ctypes.POINTER(ctypes.c_float)()
lib.getpointer_(ctypes.byref(ptr))
print(ptr)

import numpy

# create a numpy array that shares the same address as the fortran array
# be aware that the dimension ordering is different between fortran and python
ary = numpy.ctypeslib.as_array(ptr, shape=(20, 10))
print(ary.flags)

del ary

ary2 = numpy.ctypeslib.as_array(ptr, shape=(20, 10))
print(ary2)
