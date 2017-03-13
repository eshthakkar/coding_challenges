# O(n) time and O(n) space complexity
def majority_element(nums):
    """ Given a positive integers array, find the majority element. If there is no majority element,
    return -1. 

    >>> nums = [3, 1, 7, 1, 3, 7, 3, 7, 1, 7, 7]
    >>> print majority_element(nums)
    7

    >>> nums = [1, 2, 10]
    >>> print majority_element(nums)
    -1

    >>> nums = [1, 2, 1, 3, 2, 3]
    >>> print majority_element(nums)
    -1
    """

    frequencies = {}
    prev_max_frequency = 1
    current_max_frequency = 1
    majority_element = -1

    for num in nums:
        frequencies[num] = frequencies.get(num,0) + 1
   

    for num in frequencies:  

        if frequencies[num] >= current_max_frequency:
            prev_max_frequency = current_max_frequency
            current_max_frequency = frequencies[num]
            majority_element = num


    if current_max_frequency > prev_max_frequency:        
        return majority_element 
    else:
        return -1           


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print                      