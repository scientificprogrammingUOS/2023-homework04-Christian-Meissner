import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    """
    
    Args:

    Returns:
        mean:
        std:
    """
    checklist = [loc, scale, lower_bound, upper_bound]
    # check if all parameters are of type int or of type float
    for i in checklist:
        if (not isinstance(i, int)) & (not isinstance(i, float)):
            raise TypeError(f"{i} haas to be of type int or of type float")
            
    # check if 'lower_ bound' is smaller than 'upper_bound'
    if lower_bound > upper_bound:
        raise ValueError(f"{lower_bound} is larger than {upper_bound}")

    gaussian_dist = np.random.normal(loc, scale, size=100)

    # create a mask filtering for the 'lower_bound' and 'upper_bound' condition
    filter_list = []
    for i in gaussian_dist:
        if (i > lower_bound) & (i < upper_bound):
            filter_list.append(i)

    #mask = (gaussian_dist > lower_bound) & (gaussian_dist < upper_bound)
    # create an array using the mask
    masked_dist = np.array(filter_list)

    # calculate the mean 
    mean_masked_dist = np.mean(masked_dist)

    # calculate the std
    std_masked_dist = np.std(masked_dist)

    print('mean: ', mean_masked_dist, 'std: ', std_masked_dist)

    return (mean_masked_dist, std_masked_dist)



if __name__ == "__main__":
    #gaussian_analysis(0, 3, 1, 3)
    pass