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

    
            
            
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

