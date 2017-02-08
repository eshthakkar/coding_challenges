def find4uniques(a,b):
    """ Check if the indices of all 4 numbers are unique and return the list of indices if they are."""

    i = 0
    if a[i] == b[i] or a[i] == b[i+1] or a[i+1] == b[i] or a[i+1] == b[i+1]:
        return None
    else:
        return a + b    

def quad_combinator(arr,s):
    """ Select 4 numbers from given array whose sum is equal to the target and return an array of their indices.

        >>> print quad_combinator([1,2,2,3,10,40],47)
        [1, 2, 3, 5]

        >>> print quad_combinator([3,2,11,5,6,6],3)
        None

        >>> print quad_combinator([],4)
        None

        >>> print quad_combinator([1,2,3],2)
        None

        >>> print quad_combinator([5,2,1,4],8)
        None

        >>> print quad_combinator([1,4,8,0,6],13)
        [0, 3, 1, 2]
    """

    if not arr or s is None:
        return None

    if len(arr) < 4:
        return None

    pairs_dict = {}

    for i in xrange(len(arr)):
        for j in xrange(i+1,len(arr)):
            pairsum = arr[i] + arr[j]
            pairs_dict[pairsum] = [i,j]

    for pairsum in pairs_dict:
        if s - pairsum in pairs_dict:
            pairA = pairs_dict[pairsum]
            pairB = pairs_dict[s - pairsum]
            combination = find4uniques(pairA,pairB)

            if combination is not None:
                return combination
    return None            

#O(n) runtime
def HasPairWithSum(nums,target):
    """ Find if a pair of numbers exist in the sorted list with a sum that is equal to target
        >>> print HasPairWithSum([1,2,4,5],8)
        False

        >>> print HasPairWithSum([1,2,4,4],8)
        True
    """
    i = 0
    j = len(nums) - 1

    while i < j:
        calc_sum = nums[i] + nums[j]

        if calc_sum == target:
            return True
        elif calc_sum < target:
            i += 1
        else:
            j -= 1

    return False

#O(n) runtime
def HasPairWithSum_unsorted(nums,target):
    """ Return True if a pair of numbers from unsorted list add up to target otherwise return False
        >>> print HasPairWithSum_unsorted([1,2,4,5],8)
        False

        >>> print HasPairWithSum_unsorted([1,2,4,4],8)
        True
    """ 

    comp = set()

    for num in nums:
        val = target - num
        if val in comp:
            return True
        else:
            comp.add(val) 

    return False              


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print       

