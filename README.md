# README

## Installation

```
pip install dlib-XX.XX.X-cpXX-cpXX-win_amd64.whl
```

The `XX` depends on your situation.

---

## Configuration

Open file `C:\Users\XXX\AppData\Local\Programs\Python\PythonXX\Lib\site-packages\dlib\_init_.py`.

The `XXX` depends on your situation.

### With CUDA

If you use CUDA, configure the code:

```
if "ON" == "ON":
    add_lib_to_dll_path(
        "C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/vXX.X/lib/x64/cudnn.lib"
    )
    add_lib_to_dll_path(
        "C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/vXX.X/lib/x64/cudart.lib"
    )
```

The `XX.X` depends on your situation.

### Without CUDA

If you don't use CUDA, delete the code:

```
if "ON" == "ON":
    add_lib_to_dll_path(
        "C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/vXX.X/lib/x64/cudnn.lib"
    )
    add_lib_to_dll_path(
        "C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/vXX.X/lib/x64/cudart.lib"
    )
```
