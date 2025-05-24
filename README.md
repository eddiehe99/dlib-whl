# README

Support for CUDA is **ALWAYS** on the way.

## Installation

1. Download `.whl` files form [Releases](https://github.com/eddiehe99/dlib-whl/releases)

2. Install

    ```bash
    pip install dlib-XX.XX.X-cpXX-cpXX-win_amd64.whl
    ```

    The `XX` depends on your situation.

---

## Configuration

Open file `C:\Users\XXX\AppData\Local\Programs\Python\PythonXX\Lib\site-packages\dlib\_init_.py`.

The `XXX` depends on your situation and the whole filepath may be different based on your installation configuration.

### With CUDA

If you use CUDA, configure the code:

```python
if "ON" == "ON":
    add_lib_to_dll_path(
        "C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/vXX.X/lib/x64/cudnn.lib"
    )
    add_lib_to_dll_path(
        "C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/vXX.X/lib/x64/cudart.lib"
    )
```

The `XX.X` depends on your situation or the whole filepath may be different based on your installation configuration.

### Without CUDA

If you do not use CUDA, delete the code:

```python
if "ON" == "ON":
    add_lib_to_dll_path(
        "C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/vXX.X/lib/x64/cudnn.lib"
    )
    add_lib_to_dll_path(
        "C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/vXX.X/lib/x64/cudart.lib"
    )
```

**Probably. I have not tried it.**

---

## Verification

```python
import dlib

print(dlib.DLIB_USE_CUDA)
print(dlib.cuda.get_num_devices())
```

Or

Run the `tempCodeRunnerFile.py`.

---

## Warning

**Whether the `.whl` file works on your computer is a matter of luck!**

If the `.whl` file smooths your installation, you could send an e-mail of gratitude to me. This is enough to delight me for not less than a day and makes you incredibly sexually attractive.

If it does not work, please make an attempt at the following steps.

1. Try to install different versions of `.whl` files on the [Release](https://github.com/eddiehe99/dlib-whl/releases) page.

2. Try `.whl` files on [Dlib_Windows_Python3.x](https://github.com/z-mahmud22/Dlib_Windows_Python3.x).

3. Download the source code from [dlib (official)](https://github.com/davisking/dlib) and install by yourself.

By the way, you could also send an e-mail to me to complain.

## PS

### Configuration for CUDNN Installation

The installation of cuDNN greater than 9.0.0 may cause weird errors. Please check out the issue [davisking/dlib#2979](https://github.com/davisking/dlib/issues/2979).

The following steps may work:

1. Move files from subfolders to parent folders.

    - Move all files from `C:\Program Files\NVIDIA\CUDNN\vx.x\bin\xx.x` to `C:\Program Files\NVIDIA\CUDNN\vx.x\bin`
    - Move all files from `C:\Program Files\NVIDIA\CUDNN\vx.x\include\xx.x` to `C:\Program Files\NVIDIA\CUDNN\vx.x\inlcude`
    - Move all files from `C:\Program Files\NVIDIA\CUDNN\vx.x\lib\xx.x` to `C:\Program Files\NVIDIA\CUDNN\vx.x\lib`

2. Add the system variable `CMAKE_PRIFIX_PATH` whose value is `C:/Program Files/NVIDIA/CUDNN/vx.x`.
