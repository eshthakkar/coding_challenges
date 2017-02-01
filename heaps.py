import math

def max_heapify(A,i,n):
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < n and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A,largest,n)  


#O(n) runtime to build a max heap from an unordered linear array
def build_max_heap(A):
    """ Build max heap from an array

        >>> nums = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        >>> build_max_heap(nums)
        >>> print nums
        [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    """

    n = len(A)
    for i in xrange(int(math.floor(n/2)),-1,-1):
        max_heapify(A,i,n)


#O(nlogn) runtime
def heap_sort(A):
    """Heap sort given array of numbers using max heap and max heapify logic.
        >>> nums = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        >>> heap_sort(nums)
        >>> print nums
        [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]

    """
    build_max_heap(A)
    n = len(A)

    for i in xrange(n-1,0,-1):
        A[0], A[i] = A[i], A[0]
        n -= 1
        max_heapify(A,0,n)

        


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print        