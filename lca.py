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




