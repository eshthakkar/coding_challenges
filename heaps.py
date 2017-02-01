import math

def max_heapify(A,i):
    l = 2 * i + 1
    r = 2 * i + 2

    if l <= len(A)-1 and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r <= len(A)-1 and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A,largest)  


def build_max_heap(A):
    """ Build max heap from an array

        >>> nums = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        >>> build_max_heap(nums)
        >>> print nums
        [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    """

    n = len(A)
    for i in xrange(int(math.floor(n/2)),-1,-1):
        max_heapify(A,i)
        


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print        