#O(logn) runtime
def binarySearch(arr,target,begin,end):
    """ Search the target in a sorted array using binarySearch

        >>> arr = [2, 4, 5, 9, 12, 17]
        >>> print binarySearch(arr, 12, 0, len(arr))
        4

        >>> print binarySearch(arr, 6, 0, len(arr))
        -1

        >>> print binarySearch(arr, 2, 0, len(arr))
        0
    """

    while(begin <= end):
        mid = int(round((begin+end)/2))

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            begin = mid + 1

        else:
            end = mid - 1

    return -1 


def getOrigFirst(arr):
    """ Find and return the pivot index"""

    begin = 0
    end = len(arr)

    while(begin <= end):
        mid = int(round((begin+end)/2))

        if mid == 0 or arr[mid] < arr[mid-1]:
            return mid
        if arr[mid] > arr[0]:
            begin = mid + 1
        else:
            end = mid - 1
    return 0               


#O(logn) runtime
def shiftedArraySearch(shiftArr,num):
    """ Search for a number in a shifted array
        >>> shiftArr = [9, 12, 17, 2, 4, 5]
        >>> print shiftedArraySearch(shiftArr, 5)
        5

        >>> print shiftedArraySearch(shiftArr, 1)
        -1

    """

    originalFirst = getOrigFirst(shiftArr)

    if num == shiftArr[originalFirst]:
        return originalFirst

    if num >= shiftArr[0]:
        return binarySearch(shiftArr, num, 0, originalFirst - 1)

    else:
        n = len(shiftArr)
        return binarySearch(shiftArr, num, originalFirst+1, n-1)
    
    



if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()

    if not result.failed:
        print "All tests passed. Good work!"

    print    
