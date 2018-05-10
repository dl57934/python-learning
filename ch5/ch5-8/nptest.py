import pandas as pd
import numpy as np

v = np.zeros(10,dtype=np.float32)
print(v)

v = np.arange(10,dtype=np.int32)
print(v)

v*=4
print(v)

print(v.mean())
