import numpy as np

# implement the function strange pattern

def strange_pattern(input_tuple):
    """Application of strange pattern to a np array

    Args:
        n: number of rows
        m: number of columns 
    """
    n, m = input_tuple
    bool_arr = np.zeros((n, m), dtype='bool')
 
    # assigne the value 1 to every third element in every third row
    bool_arr[::3, ::3] = 1
    # assigne the value 1 to every third element (starting with column index 2) in every third row (starting with row index 1)
    bool_arr[1::3, 2::3] = 1
    # assigne the value 1 to every third element (starting with column index 1) in every third row (starting with row index 2)
    bool_arr[2::3, 1::3] = 1
    
 
    """ print the pattern
    for i in range(n):
        for j in range(m):
            print(bool_arr[i][j], end=" ")
        print() """
    
    return bool_arr


if __name__ == "__main__":
    
    #strange_pattern((6,8))
    pass
