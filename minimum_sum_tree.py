def minimum_sum(root):
    """ Return the minimum sum of a path from root to leaf in a binary tree
        Time complexity : O(n)
        Space complexity : O(n)
        
        >>> root = Node(10)
        >>> root.left = Node(-2)
        >>> root.right = Node(7)
        >>> root.left.left = Node(8)
        >>> root.left.right = Node(-4)
        >>> ms = minimum_sum(root)
        >>> print ms[0]
        4
        >>> print ms[1][::-1]
        [10, -2, -4]

        >>> root = Node(6)
        >>> root.left = Node(8)
        >>> root.right = Node(2)
        >>> root.left.left = Node(5)
        >>> root.left.right = Node(7)
        >>> root.right.left = Node(3)
        >>> root.right.right = Node(4)
        >>> ms = minimum_sum(root)
        >>> print ms[0]
        11
        >>> print ms[1][::-1]
        [6, 2, 3]


        >>> ms = minimum_sum(None)
        >>> print ms[0]
        0
        >>> print ms[1][::-1]
        []


        >>> ms = minimum_sum(Node(7))
        >>> print ms[0]
        7
        >>> print ms[1][::-1]
        [7]

        >>> root = Node(6)
        >>> root.left = Node(-2)
        >>> ms = minimum_sum(root)
        >>> print ms[0]
        4
        >>> print ms[1][::-1]
        [6, -2]


    """

    if root is None:
        return (0,[])

    l = minimum_sum(root.left)  
    left_sum = root.value + l[0]
    left_path = l[1] + [root.value]

    r = minimum_sum(root.right)
    right_sum = root.value + r[0]
    right_path = r[1] + [root.value]

    if left_sum < right_sum:
        return (left_sum, left_path)
    else:
        return (right_sum, right_path)    


class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None 


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print    

