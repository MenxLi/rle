import sys, os
import numpy as np

curr_path = os.path.dirname(__file__)
root_path = os.path.dirname(curr_path)
sys.path.append(root_path)

from rle import encode_simple, decode_simple, encode_nd, decode_nd

def enc1d():
    arr = np.array([1,1,1,2,3,3,3,3,4,4,4], dtype = np.uint8)
    print("Original array: ", arr)

    encoded = encode_simple(arr)
    print("Encoded array: ", encoded)

    decoded = decode_simple(encoded)
    print("Decoded array: ", decoded)

def enc2d():
    # Create a circle image
    arr = np.zeros((100, 100), np.uint8)
    _radius_squared = 40**2
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (i-50)**2 + (j-50)**2 <_radius_squared:
                arr[i][j] = 1

    print("Image size before encoding: ", arr.size, arr.shape)
    encoded_dict = encode_nd(arr)
    print("Size after encoding: ", encoded_dict["encoded"].size)
    decoded = decode_nd(**encoded_dict)
    print("Assert equivalent before and after: ", (decoded == arr).all())

if __name__ == "__main__":
    enc1d()
    enc2d()
