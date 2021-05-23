import numpy as np
import math
# grma schmidt method of orthogonalization
def gs(vector):
    dist = 0
    # print(f"testing:{type(vector)}")
    for v in vector:
        dist = dist+(v**2)
    dist = math.sqrt(dist)

    for i in range(0, len(vector)):
        vector[i] = vector[i]/dist
    return vector