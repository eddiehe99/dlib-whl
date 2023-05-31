# README

## Installation

```bash
pip install dlib-XX.XX.X-cpXX-cpXX-win_amd64.whl
```

The `XX` depends on your situation.

---

## Configuration

Open file `C:\Users\XXX\AppData\Local\Programs\Python\PythonXX\Lib\site-packages\dlib\_init_.py`.

The `XXX` depends on your situation or the whole filepath may be totally different based on your installation configuration.

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

The `XX.X` depends on your situation or the whole filepath may be totally different based on your installation configuration.

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

Probably. I have not tried it.

---

## Verification

```python
import dlib

print(dlib.DLIB_USE_CUDA)
print(dlib.cuda.get_num_devices())
```

---

## Warning

It is a matter of luck whether the `.whl` file works on your computer.

If the `.whl` file smooth your installation, you could send a e-mail of gratitude to me. This is enough to delight me not less than a day.

If it does not work, I highly recommend you to download the source code and install by yourself. Besides, you could also send a e-mail full of swear words or other trash to me.
