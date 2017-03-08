import random

# O(nlogn) runtime, O(n) space complexity. Stack space is O(logn). 
def merge_sort(nums):
    """ Merge sort algo and return a sorted list of nums

        >>> nums = [8,1,4,6,9,5]
        >>> print merge_sort(nums)
        [1, 4, 5, 6, 8, 9]

        >>> import random
        >>> my_randoms = random.sample(xrange(1, 101), 10)
        >>> merge_sort(my_randoms) == sorted(my_randoms)
        True

    """

    if len(nums) == 1:
        return nums

    mid = len(nums)/2    
    left_part = merge_sort(nums[:mid]) 
    right_part = merge_sort(nums[mid:]) 
    merged = merge(left_part,right_part) 
    return merged

def merge(l1,l2):
    """ Return sorted merged list"""

    result = []

    while l1 and l2:
        if l1[0] < l2[0]:
            result.append(l1.pop(0))
        else:
            result.append(l2.pop(0))

    while l1:
        result.append(l1.pop(0))

    while l2:
        result.append(l2.pop(0)) 

    return result 

# O(nlogn) best case running time. In space swaps, with O(logn) stack space. worst case running time would be O(n**2)
def quicksort(a,start,end):
    """Quicksort Algo
        >>> nums = [2, 8, 7, 1, 3, 5, 6, 4]
        >>> print quicksort(nums,0,len(nums))
        [1, 2, 3, 4, 5, 6, 7, 8]

        >>> nums = [1]
        >>> print quicksort(nums,0,len(nums))
        [1]

        >>> nums = [2, 1]
        >>> print quicksort(nums,0,len(nums))
        [1, 2]

        >>> nums = [1, 2]
        >>> print quicksort(nums,0,len(nums))
        [1, 2]

        >>> nums = []
        >>> print quicksort(nums,0,len(nums))
        []
    """

    # base case
    if end - start <= 1:
        return a

    #Pivot is the last element
    pivot = end - 1

    i = start - 1

    for j in range(start,pivot):
        if a[j] <= a[pivot]:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[pivot] = a[pivot], a[i+1]

    quicksort(a,start,i+1)
    quicksort(a,i+2,end)  
    
    return a                

    


def quick_sort_3_way(nums,low,high):
    """ The idea of 3 way QuickSort is to process all occurrences of pivot and is based on Dutch National Flag algorithm.
        In 3 Way QuickSort, an array arr[l..r] is divided in 3 parts:
        a) arr[l..i] elements less than pivot.
        b) arr[i+1..j-1] elements equal to pivot.
        c) arr[j..r] elements greater than pivot.
    
        >>> arra = [4, 9, 4, 4, 1, 9, 4, 4, 9, 4, 4, 1, 4]
        >>> quick_sort_3_way(arra, 0, len(arra)-1)
        >>> print arra
        [1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 9, 9, 9]

        >>> nums = [1, 1]
        >>> quick_sort_3_way(nums, 0, len(nums) - 1)
        >>> print nums
        [1, 1]

        >>> nums = [1, 2]
        >>> quick_sort_3_way(nums, 0, len(nums) - 1)
        >>> print nums
        [1, 2]

        >>> nums = [2, 1]
        >>> quick_sort_3_way(nums, 0, len(nums) - 1)
        >>> print nums
        [1, 2]

        >>> nums = [1]
        >>> quick_sort_3_way(nums, 0, len(nums) - 1)
        >>> print nums
        [1]

        >>> nums = []
        >>> quick_sort_3_way(nums, 0, len(nums) - 1)
        >>> print nums
        []

        >>> nums = [3, 2, 2]
        >>> quick_sort_3_way(nums, 0, len(nums) - 1)
        >>> print nums
        [2, 2, 3]

    """

    if not nums:
        return 

    # if the list has only 2 elements
    if high - low == 1:
        if nums[high] < nums[low]:
            nums[low], nums[high] = nums[high], nums[low]
        return 

    mid = low
    pivot = nums[high]

    while (mid <= high):
        if nums[mid] < pivot:

            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == pivot:
            mid += 1

        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1        





    





if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print                      
