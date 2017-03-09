def preorder(root):
    """Returns a tree in a list of preorder form

        >>> class Node(object):
        ...     def __init__(self, value):
        ...             self.value=value
        ...             self.left = None
        ...             self.right = None
        ...     def add_node(self, obj):
        ...             if obj.value < self.value:
        ...                 self.left = obj
        ...             else:
        ...                 self.right = obj
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_node(two)
        >>> two.add_node(three)
        >>> print preorder(one)
        [1, 2, 3]

        >>> three = Node(3)
        >>> two = Node(2)
        >>> one = Node(1)
        >>> two.add_node(one)
        >>> two.add_node(three)
        >>> print preorder(two)
        [2, 1, 3]

        >>> three = Node(3)
        >>> two = Node(2)
        >>> one = Node(1)
        >>> three.add_node(two)
        >>> two.add_node(one)
        >>> print preorder(three)
        [3, 2, 1]

    """

    if root is None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)


def inorder(root):
    """Returns a tree in a list of inorder form

        >>> class Node(object):
        ...     def __init__(self, value):
        ...             self.value=value
        ...             self.left = None
        ...             self.right = None
        ...     def add_node(self, obj):
        ...             if obj.value < self.value:
        ...                 self.left = obj
        ...             else:
        ...                 self.right = obj
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_node(two)
        >>> two.add_node(three)
        >>> print inorder(one)
        [1, 2, 3]

        >>> three = Node(3)
        >>> two = Node(2)
        >>> one = Node(1)
        >>> two.add_node(one)
        >>> two.add_node(three)
        >>> print inorder(two)
        [1, 2, 3]

        >>> three = Node(3)
        >>> two = Node(2)
        >>> one = Node(1)
        >>> three.add_node(two)
        >>> two.add_node(one)
        >>> print inorder(three)
        [1, 2, 3]

        >>> from binarytree import bst
        >>> my_bst = bst(height=5)
        >>> out = inorder(my_bst)
        >>> out == sorted(out)
        True

    """

    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


def postorder(root):
    """Returns a tree in a list of postorder form

        >>> class Node(object):
        ...     def __init__(self, value):
        ...             self.value=value
        ...             self.left = None
        ...             self.right = None
        ...     def add_node(self, obj):
        ...             if obj.value < self.value:
        ...                 self.left = obj
        ...             else:
        ...                 self.right = obj
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_node(two)
        >>> two.add_node(three)
        >>> print postorder(one)
        [3, 2, 1]

        >>> three = Node(3)
        >>> two = Node(2)
        >>> one = Node(1)
        >>> two.add_node(one)
        >>> two.add_node(three)
        >>> print postorder(two)
        [1, 3, 2]

        >>> three = Node(3)
        >>> two = Node(2)
        >>> one = Node(1)
        >>> three.add_node(two)
        >>> two.add_node(one)
        >>> print postorder(three)
        [1, 2, 3]

    """ 

    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value] 
    

def count_nodes(root):
    """Counts and returns the number of nodes in a tree using 
    dfs

        >>> class Node(object):
        ...     def __init__(self, value):
        ...             self.value=value
        ...             self.left = None
        ...             self.right = None
        ...     def add_node(self, obj):
        ...             if obj.value < self.value:
        ...                 self.left = obj
        ...             else:
        ...                 self.right = obj
        ...
        >>> three = Node(3)
        >>> two = Node(2)
        >>> one = Node(1)
        >>> three.add_node(two)
        >>> two.add_node(one)
        >>> print count_nodes(three)
        3

    """

    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)  


def BFS(root,data):
    """Search for a node using BFS
       >>> class Node(object):
       ...      def __init__(self,data,children=None):
       ...              self.data = data
       ...              self.children = children or []
       ...      def add_child(self, obj):
       ...             self.children.append(obj)
       ...
       >>> one = Node(1)
       >>> two = Node(2)
       >>> three = Node(3)
       >>> one.add_child(two)
       >>> one.add_child(three)
       >>> BFS(one,3)
       True

       >>> BFS(one,4)
       False
    """

    to_visit = [root]

    while to_visit:
        current = to_visit.pop(0)

        if current.data == data:
            return True

        to_visit.extend(current.children)

    return False   


def preorder_iterative(root):
    """Iterative preorder traversal of a tree

        >>> class TreeNode(object):
        ...     def __init__(self, x):
        ...         self.value = x
        ...         self.left = None
        ...         self.right = None
        ...     def add_node(self, obj):
        ...             if obj.value < self.value:
        ...                 self.left = obj
        ...             else:
        ...                 self.right = obj
        ...
        >>> one = TreeNode(1)
        >>> two = TreeNode(2)
        >>> three = TreeNode(3)
        >>> two.add_node(one)
        >>> two.add_node(three)
        >>> print preorder_iterative(two)
        [2, 1, 3]
    """

    result = []

    if root is None:
        return result

    to_visit = []
    to_visit.append(root)

    while(len(to_visit) > 0):
        node = to_visit.pop()
        result.append(node.value)
        if node.right is not None:    
            to_visit.append(node.right)
        if node.left is not None:
            to_visit.append(node.left)
        

    return result  


def tree_height(root):
    """returns the height of tree

        >>> class Node(object):
        ...     def __init__(self, value):
        ...             self.value=value
        ...             self.left = None
        ...             self.right = None
        ...     def add_node(self, obj):
        ...             if obj.value < self.value:
        ...                 self.left = obj
        ...             else:
        ...                 self.right = obj
        ...
        >>> three = Node(3)
        >>> two = Node(2)
        >>> one = Node(1)
        >>> three.add_node(two)
        >>> two.add_node(one)
        >>> print tree_height(three)
        3

    """

    if root is None:
        return 0

    # print "Node: %d" % root.value
    

    left_height = tree_height(root.left) 
    right_height = tree_height(root.right) 
    ret_value = max(left_height,right_height) + 1

    # print "Root: %d, Left height: %d, Right height: %d,ret_value: %d" % (root.value, left_height, right_height, ret_value)

    return ret_value



# O(n) time and O(n) space complexity            
def is_balanced(root):
    """ Check if the difference between the depths of any two leaf nodes is not greater than 1

        >>> class Node(object):
        ...     def __init__(self, value):
        ...             self.value=value
        ...             self.left = None
        ...             self.right = None
        ...     def add_node(self, obj):
        ...             if obj.value < self.value:
        ...                 self.left = obj
        ...             else:
        ...                 self.right = obj
        ...
        >>> eleven = Node(11)
        >>> twelve = Node(12)
        >>> nine = Node(9)
        >>> six = Node(6)
        >>> ten = Node(10)
        >>> four = Node(4)
        >>> two = Node(2)
        >>> eleven.add_node(twelve)
        >>> eleven.add_node(nine)
        >>> nine.add_node(ten)
        >>> nine.add_node(six)
        >>> six.add_node(four)
        >>> four.add_node(two)
        >>> print is_balanced(eleven)
        False

        >>> eleven = Node(11)
        >>> twelve = Node(12)
        >>> nine = Node(9)
        >>> six = Node(6)
        >>> ten = Node(10)
        >>> eleven.add_node(twelve)
        >>> eleven.add_node(nine)
        >>> nine.add_node(ten)
        >>> nine.add_node(six)
        >>> print is_balanced(eleven)
        True



    """

    if root is None:
        return True

    depths = []
    nodes = []
    nodes.append((root,0))

    while len(nodes):
        node,depth = nodes.pop()

        # If leaf node
        if not node.left and not node.right:

            # New leaf node, not in depths
            if depth not in depths:
                depths.append(depth)

                if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                    return False

        else:
            if node.left:
                nodes.append((node.left,depth + 1)) 
            if node.right:
                nodes.append((node.right,depth + 1)) 

    return True                           


def is_bst_checker(root,lower_bound=-float('inf'),upper_bound=float('inf')):
    """Check if tree is a bst
        >>> class Node(object):
        ...     def __init__(self, value):
        ...             self.value=value
        ...             self.left = None
        ...             self.right = None
        ...     def add_node(self, obj):
        ...             if obj.value < self.value:
        ...                 self.left = obj
        ...             else:
        ...                 self.right = obj
        ...
        >>> eleven = Node(11)
        >>> twelve = Node(12)
        >>> nine = Node(9)
        >>> six = Node(6)
        >>> ten = Node(10)
        >>> four = Node(4)
        >>> two = Node(2)
        >>> eleven.add_node(twelve)
        >>> eleven.add_node(nine)
        >>> nine.add_node(ten)
        >>> nine.add_node(six)
        >>> six.add_node(four)
        >>> four.add_node(two)
        >>> print is_bst_checker(eleven)
        True

        >>> eleven = Node(11)
        >>> twelve = Node(12)
        >>> nine = Node(9)
        >>> six = Node(6)
        >>> ten = Node(10)
        >>> four = Node(4)
        >>> two = Node(2)
        >>> fifteen = Node(15)
        >>> eleven.add_node(twelve)
        >>> eleven.add_node(nine)
        >>> nine.add_node(ten)
        >>> nine.add_node(six)
        >>> six.add_node(four)
        >>> four.add_node(fifteen)
        >>> print is_bst_checker(eleven)
        False


    """

    if root is None:
        return True

    if root.value > upper_bound or root.value < lower_bound:
        return False

    return is_bst_checker(root.left,lower_bound,root.value) and is_bst_checker(root.right,root.value,upper_bound)       


def largest_values(root):
    """
        >>> class TreeNode(object):
        ...     def __init__(self, x):
        ...         self.val = x
        ...         self.left = None
        ...         self.right = None
        ...     def add_left(self, obj):
        ...         self.left = obj
        ...     def add_right(self,obj):
        ...         self.right = obj
        ...
        >>> one = TreeNode(1)
        >>> three = TreeNode(3)
        >>> two = TreeNode(2)
        >>> five = TreeNode(5)
        >>> nine = TreeNode(9)
        >>> thr = TreeNode(3)
        >>> one.add_left(three)
        >>> one.add_right(two)
        >>> three.add_left(five)
        >>> three.add_right(thr)
        >>> two.add_right(nine)
        >>> print largest_values(one)
        [1, 3, 9]
    """
    if not root: return []
    queue, ans = [(0,root)], {}
    while queue:
        level, node = queue.pop(0)
        if level not in ans or node.val > ans[level]:
            ans[level] = node.val
        if node.right:
            queue.append((level+1, node.right))
        if node.left:
            queue.append((level+1, node.left))

        
    return [ans[i] for i in range(level+1)]
 

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


    def add_node(self, obj):
        if obj.value < self.value:
            self.left = obj
        else:
            self.right = obj


def add_node_bst(root,key):
    """Add a node to a BST

        >>> eleven = Node(11)
        >>> twelve = Node(12)
        >>> nine = Node(9)
        >>> six = Node(6)
        >>> ten = Node(10)
        >>> four = Node(4)
        >>> two = Node(2)
        >>> eleven.add_node(twelve)
        >>> eleven.add_node(nine)
        >>> nine.add_node(ten)
        >>> nine.add_node(six)
        >>> six.add_node(four)
        >>> four.add_node(two)
        >>> three = add_node_bst(eleven,3)
        >>> print preorder(eleven)
        [11, 9, 6, 4, 2, 3, 10, 12]

    """

    if root is None:
        return Node(key)

    if key < root.value:
        root.left = add_node_bst(root.left,key)
    elif key > root.value:
        root.right = add_node_bst(root.right,key)

    return root            


def getmin(root):
    """ find the lowest value in the given bst starting from the root"""
    min_val = root.value

    while root.left != None:
        root = root.left
        min_val = root.value  

    return min_val     

 
def delete_node_bst(root,key):
    """ Delete the node whose value is same as key from a bst

        >>> eleven = Node(11)
        >>> twelve = Node(12)
        >>> nine = Node(9)
        >>> six = Node(6)
        >>> ten = Node(10)
        >>> four = Node(4)
        >>> two = Node(2)
        >>> eleven.add_node(twelve)
        >>> eleven.add_node(nine)
        >>> nine.add_node(ten)
        >>> nine.add_node(six)
        >>> six.add_node(four)
        >>> four.add_node(two)
        >>> print preorder(eleven)
        [11, 9, 6, 4, 2, 10, 12]

        >>> print preorder(delete_node_bst(eleven,9))
        [11, 10, 6, 4, 2, 12]

        >>> print preorder(delete_node_bst(eleven,11))
        [12, 10, 6, 4, 2]

    """

    if root is None:
        return root

    if key < root.value:
        root.left = delete_node_bst(root.left,key)
    elif key > root.value:
        root.right = delete_node_bst(root.right,key)

    # when node to be removed is found    
    else:

        # node to be removed has only right child
        if root.left is None:
            return root.right

        # node to be removed has only left child    
        elif root.right is None:
            return root.left

        # node to be removed has both left and right children    
        else:
            root.value = getmin(root.right)
            root.right = delete_node_bst(root.right,root.value)

    return root        


def largest(root):
    """ Return the largest element from a BST"""

    if root is None:
        raise Exception("Tree must have atleast 1 node!")

    if root.right:
        return largest(root.right)

    return root.value        


# O(h) time and space complexity where h is the height of the tree
def largest_2nd(root):
    """ Return the 2nd largest element from a bst
        >>> eleven = Node(11)
        >>> twelve = Node(12)
        >>> nine = Node(9)
        >>> six = Node(6)
        >>> ten = Node(10)
        >>> four = Node(4)
        >>> two = Node(2)
        >>> eleven.add_node(twelve)
        >>> eleven.add_node(nine)
        >>> nine.add_node(ten)
        >>> nine.add_node(six)
        >>> six.add_node(four)
        >>> four.add_node(two)
        >>> print largest_2nd(eleven)
        11

        >>> five = Node(5)
        >>> three = Node(3)
        >>> eight = Node(8)
        >>> two = Node(2)
        >>> four = Node(4)
        >>> six = Node(6)
        >>> ten = Node(10)
        >>> seven = Node(7)
        >>> fifteen = Node(15)
        >>> five.add_node(three)
        >>> five.add_node(eight)
        >>> three.add_node(two)
        >>> three.add_node(four)
        >>> eight.add_node(six)
        >>> eight.add_node(ten)
        >>> six.add_node(seven)
        >>> ten.add_node(fifteen)
        >>> print largest_2nd(five)
        10

       
    """


    if not root or (not root.left and not root.right) :
        raise Exception("There should be atleast 2 nodes in the tree")

    # if we are at the largest and it has only left subtree,
    # 2nd largest is the largest from this subtree    
    if not root.right and root.left:
        return largest(root.left)

    # if we are at the parent of the largest, and largest has no left subtree,
    # in that case current node is the 2nd largest    
    if root.right and not root.right.left and not root.right.right:
        return root.value 

    # otherwise step right    
    return largest_2nd(root.right)     
 


def largest_second(root, count=0, value=None):
    """
        Reverse inorder traversal along with the use of a count

        >>> eleven = Node(11)
        >>> twelve = Node(12)
        >>> nine = Node(9)
        >>> six = Node(6)
        >>> ten = Node(10)
        >>> four = Node(4)
        >>> two = Node(2)
        >>> eleven.add_node(twelve)
        >>> eleven.add_node(nine)
        >>> nine.add_node(ten)
        >>> nine.add_node(six)
        >>> six.add_node(four)
        >>> four.add_node(two)
        >>> print largest_second(eleven)[1] == largest_2nd(eleven) == largest_2nd_iterative(eleven)
        True

        >>> one = Node(110)
        >>> two = Node(65)
        >>> three = Node(95)
        >>> one.add_node(two)
        >>> two.add_node(three)
        >>> print largest_second(one)[1] == largest_2nd(one) == largest_2nd_iterative(one)
        True



    """

    if root.right:
        count, value = largest_second(root.right, count, value)

    count += 1
    
    if count == 2:
        return  count, root.value

    if root.left:
        count, value = largest_second(root.left, count, value)

    return count, value    



def find_largest_iterative(root):
    current = root

    while current:
        if not current.right:
            return current.value

        current = current.right


# Iterative solution doing one walk down the bst in O(h) time in O(1) space instead of O(h) space of the call stack
def largest_2nd_iterative(root):

    if not root or (not root.left and not root.right) :
        raise Exception("There should be atleast 2 nodes in the tree")

    current = root

    while current:
        if not current.right and current.left:
            return find_largest_iterative(current.left)

        if current.right and not current.right.left and not current.right.right:
            return current.value

        current = current.right        


        
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

