import numpy as np

def customInnerProduct(x,y):
    """Computes inner product of two vectors (over the last dimension)

    Args:
        x (ndarray): one arg (<dim>,d)
        y (ndarray): another arg  (<dim>,d)
        
    Returns:
    ndarray (<dim>)
    """
    return np.sum(x*y,axis=-1)    