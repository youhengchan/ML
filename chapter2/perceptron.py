import numpy as np
x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7
print(w * x)
print(np.sum(w * x))
print(np.sum(w * x + b))
# Notice that x and w are both one dimentional vector therefore
# I calculate the multiply one by one (in order of index)
# The product is [0 * 0.5, 1 * 0.5]
