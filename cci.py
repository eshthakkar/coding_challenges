# O(n) time and O(n) space complexity
def majority_element(nums):
    """ Given a positive integers array, find the majority element. If there is no majority element,
    return -1. 

    >>> nums = [3, 1, 7, 1, 3, 7, 3, 7, 1, 7, 7]
    >>> print majority_element(nums)
    -1

    >>> nums = [1, 2, 10]
    >>> print majority_element(nums)
    -1

    >>> nums = [1, 2, 1, 3, 2, 3]
    >>> print majority_element(nums)
    -1

    >>> nums = [1, 2, 5, 9, 5, 9, 5, 5, 5]
    >>> print majority_element(nums)
    5
    """

    frequencies = {}
    n = len(nums)

    half_threshold = 0.5 * n
    majority_element = -1

    for num in nums:
        frequencies[num] = frequencies.get(num,0) + 1
   

    for num in frequencies:  

        if frequencies[num] > half_threshold:
            majority_element = num


    return majority_element           


# O(n^2) time complexity and O(1) space
def majority_element_sol2(nums):
    """
        >>> nums = [3, 1, 7, 1, 3, 7, 3, 7, 1, 7, 7]
        >>> print majority_element_sol2(nums)
        -1

        >>> nums = [1, 2, 10]
        >>> print majority_element_sol2(nums)
        -1

        >>> nums = [1, 2, 1, 3, 2, 3]
        >>> print majority_element_sol2(nums)
        -1

        >>> nums = [1, 2, 5, 9, 5, 9, 5, 5, 5]
        >>> print majority_element_sol2(nums)
        5

        >>> nums = [3, 3, 4, 2, 4, 4, 2, 4]
        >>> print majority_element_sol2(nums)
        -1
    """

    n = len(nums)
    

    for i in nums:
        count = 0

        for j in nums:
            if i == j:
                count += 1

            if count > (n/2):
                return i 

    return -1  


# Moore's voting algorithm, O(n) time complexity and O(1) space complexity
def find_poss_candidate(nums):

    count = 1
    maj_index = 0

    for i in xrange(1, len(nums)):
        if nums[maj_index] == nums[i]:
            count += 1
        else:
            count -= 1

        if count == 0:
            maj_index = i
            count = 1

    return nums[maj_index]                                  


def majority_element_sol3(nums):
    """
        >>> nums = [3, 1, 7, 1, 3, 7, 3, 7, 1, 7, 7]
        >>> print majority_element_sol3(nums)
        -1

        >>> nums = [1, 2, 10]
        >>> print majority_element_sol3(nums)
        -1

        >>> nums = [1, 2, 1, 3, 2, 3]
        >>> print majority_element_sol3(nums)
        -1

        >>> nums = [1, 2, 5, 9, 5, 9, 5, 5, 5]
        >>> print majority_element_sol3(nums)
        5

        >>> nums = [3, 3, 4, 2, 4, 4, 2, 4]
        >>> print majority_element_sol3(nums)
        -1
    """

    majority_num = find_poss_candidate(nums)
    count = 0

    for num in nums:
        if num == majority_num:
            count += 1

    if count > (len(nums))/2:
        return majority_num
    else:
        return -1            



if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print                      