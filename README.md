## Intro
A python wrapper for c implemented run length encoding (RLE).

## Representation
### Simple encoding:
e.g. `5 C1 3 C5 1 C2 ...  `
C_ stands for class integer  
would be useful in compressing multiclass mask  

## Usage
API: 
```python
encode_simple(arr: np.ndarray, buffer_size: Optional[int] = None) -> np.ndarray
decode_simple(encoded: np.ndarray, buffer_size: Optional[int] = None) -> np.ndarray
```
Example see `demo.demo`

