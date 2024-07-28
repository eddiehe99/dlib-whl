import sys

print(f"python version: {sys.version}")


import dlib

print(f"dlib.__version__: {dlib.__version__}")
print(f"dlib.DLIB_USE_CUDA: {dlib.DLIB_USE_CUDA}")
print(f"dlib.cuda.get_num_devices(): {dlib.cuda.get_num_devices()}")
