import sys, os
import numpy as np

curr_path = os.path.dirname(__file__)
root_path = os.path.dirname(curr_path)
sys.path.append(root_path)

from rle import encode_simple, decode_simple

arr = np.array([1,1,1,2,3,3,3,3,4,4,4], dtype = np.uint8)
print("Original array: ", arr)

encoded = encode_simple(arr)
print("Encoded array: ", encoded)

decoded = decode_simple(encoded)
print("Decoded array: ", decoded)
