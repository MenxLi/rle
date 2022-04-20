import ctypes, os
from typing import Optional, TypedDict
import numpy as np

__root_path = os.path.abspath(os.path.dirname(__file__))
C_LIB = os.path.join(__root_path, "librlenc.so")

BUFFER_T = ctypes.c_uint16
BUFFER_PTR = ctypes.POINTER(BUFFER_T)
ARR_T = ctypes.c_uint8
ARR_T_NP = np.uint8
ARR_PTR = ctypes.POINTER(ARR_T)
ARR_SIZE_T = ctypes.c_uint64

librle = ctypes.cdll.LoadLibrary(C_LIB)

class EncodeND(TypedDict):
    encoded: np.ndarray
    arr_shape: tuple

def encode_simple(arr: np.ndarray, buffer_size: Optional[int] = None) -> np.ndarray:
    """
    Encode 1D uint8 numpy array
    """
    assert arr.dtype == ARR_T_NP and len(arr.shape) == 1, f"{ARR_T_NP} 1D array is required."
    if buffer_size is None:
        buffer_size = len(arr)//2   # initial buffer size, will be incremented if not enough
    while True:
        buffer = np.zeros((buffer_size), dtype = BUFFER_T)
        buffer_len = librle.encode_simple(arr.ctypes.data_as(ARR_PTR), ARR_SIZE_T(arr.size),
                    buffer.ctypes.data_as(BUFFER_PTR), ARR_SIZE_T(buffer.size))
        if buffer_len != -1:
            break
        else:
            buffer_size *= 2
    return buffer[:buffer_len]

def decode_simple(encoded: np.ndarray, buffer_size: Optional[int] = None) -> np.ndarray:
    """
    Decode to 1D uint8 numpy array
    """
    if buffer_size is None:
        buffer_size = len(encoded)*2   # initial buffer size, will be incremented if not enough
    while True:
        arr_buffer = np.zeros(buffer_size, dtype = ARR_T_NP)
        arr_len = librle.decode_simple(encoded.ctypes.data_as(BUFFER_PTR), ARR_SIZE_T(encoded.size),
                              arr_buffer.ctypes.data_as(ARR_PTR), ARR_SIZE_T(arr_buffer.size))
        if arr_len != -1:
            break
        else:
            buffer_size *= 2
    return arr_buffer[:arr_len]

def encode_nd(arr: np.ndarray, buffer_size: Optional[int] = None) -> EncodeND:
    """
    Encode N-D uint8 numpy array
    """
    flat_arr = arr.ravel()
    return {
        "encoded": encode_simple(flat_arr, buffer_size),
        "arr_shape": arr.shape
    }

def decode_nd(encoded: np.ndarray, arr_shape: tuple) -> np.ndarray:
    """
    Decode to N-D uint8 numpy array
    """
    arr_size = np.prod(arr_shape)
    decoded_flat = decode_simple(encoded, buffer_size = arr_size)
    return np.reshape(decoded_flat, arr_shape)
