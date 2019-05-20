import numpy as np
A = np.random.randn(4,3)
B = np.sum(A, axis = 0, keepdims = True)
print(A.shape)
