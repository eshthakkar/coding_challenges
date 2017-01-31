def find_max_crossing_subarray(A,low,mid,high):
    """ Finds max sum crossing subarray
        >>> nums = [2, 5, -9, 4, 39, 0, -2, 3, -18, 45, 7]
        >>> print find_max_crossing_subarray(nums, 0, 5, 11)
        (3, 10, 78)

        >>> nums = [-2, 8, 1, 30, 10, -2, -15, -4]
        >>> print find_max_crossing_subarray(nums, 0, 4, 8)
        (1, 4, 49)

    """

    left_sum = A[mid-1]
    total = 0
    max_left = 0

    for i in reversed(range(low,mid)):
        total += A[i]
        #print (i,total)

        if total >= left_sum:
            left_sum = total
            max_left = i


    right_sum = A[mid]
    total = 0
    max_right = 0

    for i in xrange(mid,high):
        total += A[i]
        #print (i,total)

        if total >= right_sum:
            right_sum = total
            max_right = i 

    return(max_left,max_right,left_sum+right_sum) 
 

#Divide and conquer approach. O(nlogn) runtime
def find_max_subarray(A,low,high):
    """Return max subarray given an array
        >>> nums = [5, -7, 3, 5, -2, 4, -1]
        >>> print find_max_subarray(nums, 0, 6)
        (2, 5, 10)

    """

    #Base case
    if low == high:
        return (low,high,A[low])

    else:
        mid = (low + high)/2

        (left_low,left_high,left_sum) = find_max_subarray(A,low,mid)
        (right_low,right_high,right_sum) = find_max_subarray(A,mid+1,high)
        (cross_low,cross_high,cross_sum) = find_max_crossing_subarray(A,low,mid,high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return(left_low,left_high,left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return(right_low,right_high,right_sum) 
        else:
            return(cross_low,cross_high,cross_sum)       


#Brute force approach. O(n^3)runtime
def max_slice(A):
    """
        >>> nums = [5, -7, 3, 5, -2, 4, -1]
        >>> print max_slice(nums)
        (2, 5, 10)
    """
    result = 0
    n = len(A)
    max_start_index = 0
    max_end_index = 0

    for i in xrange(n):
        for j in xrange(i,n):
            total = 0
            for p in xrange(i,j+1):
                total += A[p]
            if total > result:    
                result = total
                max_start_index = i 
                max_end_index = j 
    return (max_start_index,max_end_index,result) 


# quadratic runtime O(n^2)
def quadratic_max_slice(A):
    """
        >>> nums = [5, -7, 3, 5, -2, 4, -1]
        >>> print quadratic_max_slice(nums)
        (2, 5, 10)
    """
    n = len(A)
    result = 0
    max_index = 0
    start_index = 0

    for p in xrange(n):
        sum = 0
        for q in xrange(p,n):
            sum += A[q]
            if sum > result:
                result = sum
                max_index = q
                start_index = p
    return (start_index,max_index,result) 


#O(n) runtime using dynamic programming
def dynamic_max_slice(A):
    """
        >>> nums = [5, -7, 3, 5, -2, 4, -1]
        >>> print dynamic_max_slice(nums)
        10
    """
    max_ending = max_slice = 0

    for a in A:
        max_ending = max(0,max_ending + a)
        max_slice = max(max_slice,max_ending)
    return max_slice               






if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print                       