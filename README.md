## Intro
A python wrapper for c implemented run length encoding (RLE).  

## Representation
### Simple encoding:

* e.g. `5 C1 3 C5 1 C2 ...  ` (C_ stands for class integer, 5, 3, 1 are length)  
* Refer to [Run-length encoding - wiki](https://en.wikipedia.org/wiki/Run-length_encoding#Example)  
* Would be useful in compressing multiclass mask  

## Usage
**Use `make` to compile before using with python**  
API: 
```python
encode_simple(arr: np.ndarray, buffer_size: Optional[int] = None) -> np.ndarray
decode_simple(encoded: np.ndarray, buffer_size: Optional[int] = None) -> np.ndarray
encode_nd(arr: np.ndarray, buffer_size: Optional[int] = None) -> EncodeND
decode_nd(encoded: np.ndarray, arr_shape: tuple) -> np.ndarray
```
Example see `demo.demo`

