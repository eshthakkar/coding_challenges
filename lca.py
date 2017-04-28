class Node(object):
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

def insert(n,data):

    # if tree is empty, return a new node
    if n is None:
        return Node(data)

    if data < n.data:
        n.left = insert(n.left,data)
        n.left.parent = n

    elif data > n.data:
        n.right = insert(n.right,data)
        n.right.parent = n
    
    # Return the unchanged node pointer 
    return n       
             


def depth(n):
    """ Calculates and returns the depth of a node"""

    d = -1
    while(n):
        d += 1
        n = n.parent
    return d    


def LCA(n1,n2):
    """ Find the lowest common ancestor of the two given nodes"""

    # Find the depth of the two nodes and their differences
    d1 = depth(n1)
    d2 = depth(n2)
    diff = d1 - d2

    # if n2 is deeper than n1, swap n1 and n2
    if diff < 0:
        n1, n2 = n2, n1
        diff = -diff

    # move n1 up until both n1 and n2 are at same level
    while diff != 0:
        n1 = n1.parent
        diff -= 1

    while(n1 and n2):
        if n1 == n2:
            return n1
        n1 = n1.parent
        n2 = n2.parent

    return None  

# Driver program
root = None
root = insert(root, 20)    
root = insert(root, 8)          
root = insert(root, 22)          
root = insert(root, 4)          
root = insert(root, 12)          
root = insert(root, 10)          
root = insert(root, 14) 

n1 = root.left.right.left
n2 = root.right

result = LCA(n1,n2)
print "LCA of %d and %d is %d" %(n1.data, n2.data, result.data)         


class Node(object):
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

def lca_binary_tree(root, n1, n2):
    """ Find the lowest common ancestor of the two given nodes in a binary tree when parent field is not given in a node of the tree.
        This method assumes that n1 and n2 are present in the binary tree.
        Time complexity: O(n)

    """

    if root is None:
        return None

    if root.value == n1 or root.value == n2:
        return root

    left_ret = lca_binary_tree(root.left, n1, n2)
    right_ret = lca_binary_tree(root.right, n1, n2)

    if left_ret and right_ret:
        return root

    if left_ret:
        return left_ret

    if right_ret:
        return right_ret  


# Driver program and tests
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print "LCA(4, 5): ", lca_binary_tree(root, 4, 5).value                      
print "LCA(4, 6): ", lca_binary_tree(root, 4, 6).value                      
print "LCA(3, 4): ", lca_binary_tree(root, 3, 4).value                      
print "LCA(2, 4): ", lca_binary_tree(root, 2, 4).value                      





