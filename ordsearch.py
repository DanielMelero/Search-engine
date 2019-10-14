def linear(data, value):
    """Return the index of 'value' in 'data', or -1 if it does not occur"""
    # Go through the data list from index 0 upwards
    i = 0
    # continue until value found or index outside valid range
    while i < len(data) and data[i] != value:
        # increase the index to go to the next data value
        i = i + 1
    # test if we have found the value
    if i == len(data) or data[i] > value:
        # no, we went outside valid range; return -1
        return 'Does not occur'
    else:
        # yes, we found the value; return the index
        return i

def binary(data, value):
    low = 0
    # enter the lowest possible index
    high = len(data)-1
    # enter the highest possible index
    while low <= high != 0:
        mid = (low + high)//2
        # find the midpoint between the low and high indexes
        if data[mid] == value:
            return mid
            # if mid index contains the target value return index number
        elif data[mid] < value:
                low = mid + 1
                # if value in mid index is lower than target value set new low at mid +1
        elif data[mid] > value:
                    high = mid - 1
                    # if value in mid index is higher than target set new high as mid - 1
    return "Does not occur"

def binary_pairs(data, value):
    low = 0
    # enter the lowest possible index
    high = len(data)-1
    # enter the highest possible index
    while low <= high != 0:
        mid = (low + high)//2
        # find the midpoint between the low and high indexes
        if data[mid][0] == value:
            return mid
            # if mid index contains the target value return index number
        elif data[mid][0] < value:
                low = mid + 1
                # if value in mid index is lower than target value set new low at mid +1
        elif data[mid][0] > value:
                    high = mid - 1
                    # if value in mid index is higher than target set new high as mid - 1
    return -1
