import pandas as pd
import numpy as np
data = {
    "weight":[80.0,70.4,65.5,45.9,51.2],
    "height":[170,180,155,143,154],
    "type":["f","n","n","t","t"]
}
v = pd.DataFrame(data)

def norm(v,key):
    c = v[key]
    v_min = c.min()
    v_max = c.max()
    print("key=> ",key,"min",v_min,"max",v_max)
    v[key] = (c-v_min)/(v_max-v_min)

norm(v,'weight')
norm(v,'height')

print(v)
