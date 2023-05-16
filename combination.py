import numpy as np 

# implement your function to combine two numpy arrays 

def combination(array_1, array_2, axis=0):
    """This function combines two arrays along a specified axis

    Args: 
        array_1: first array to be combined
        array_2: second array to be combined
        axis: axis of the arrays to be combined along

    Returns:
        combined_array: the combined array based on array_1 and array_2
    
    """
    # Removing of unecessary dimensions of the input arrays
    squeeze_1 = array_1.squeeze()
    squeeze_2 = array_2.squeeze()

    try:
        # concatenate the squeezed arrays
        combined_array = np.concatenate((squeeze_1, squeeze_2), axis)
    except:
        # raise an error in case the combination along the specified axis is not possible
        raise ValueError("These two arrays can not be combined along the specified axis due to differences in structure!")
    return combined_array

if __name__ == "__main__":
    """a = np.array([[[[1, 2], [3, 4], [5, 6]]]])
    b = np.ones((2,3))
    print(combination(a,b))"""
    pass
