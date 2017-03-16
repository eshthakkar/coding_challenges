# O(k) time complexity and O(1) space complexity
def kth_largest(list1,list2,k):
    """ Find the kth largest element from 2 sorted subarrays
        >>> print kth_largest([2, 5, 7, 8], [3, 5, 5, 6], 3)
        6
    """

    i = len(list1) - 1
    j = len(list2) - 1
    count = 0

    while count < k:
        if list1[i] > list2[j]:
            result = list1[i]
            i -= 1
        else:
            result = list2[j]
            j -= 1

        count += 1

    return result            


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()

    if not result.failed:
        print "All tests passed. Good work!"

    print    
