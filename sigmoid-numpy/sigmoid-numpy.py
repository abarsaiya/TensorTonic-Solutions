import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    if not isinstance(x,np.ndarray):
        x = np.array(x)
    s =1/(1+np.exp(-x))
    return s