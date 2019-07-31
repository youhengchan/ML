# Use weight and bias to implement and gate
#     |=   0   (b + w1*x1 + w2*x2) <= 0
# y = |
#     |=   1   (b + w1*x1 + w2*x2) > 0
import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])  # imput parameters
    w = np.array([0.5, 0.5])  # weight
    b = -0.7  # bias
    tmp = np.sum(w * x) + b
    if tmp <= 0:
	    return 0
    return 1

if __name__ == "__main__":
    print("AND({0}, {1}) = {2}".format(0.5, 0.6, AND(0.5, 0.6)))	    
    print("AND({0}, {1}) = {2}".format(0.2, 0.54, AND(0.2, 0.54)))
    print("AND({0}, {1}) = {2}".format(0.35, 0.62, AND(0.35, 0.62)))
    print("AND({0}, {1}) = {2}".format(0.9, 0.89, AND(0.9, 0.89)))
