""" Given a Binary Tree, convert it to a Circular Doubly Linked List (In-Place)."""

class Node(object):
    def __init__(self, value):
        self.value = value 
        self.right = None 
        self.left = None 
        self.small = None 
        self.large = None 

    def convert_to_doubly_linked_list(self):
        if not self.left and not self.right:    
            self.small = self 
            self.large = self 
            return (self, self) 

        if self.left and not self.right:       
            (head, tail) = self.left.convert_to_doubly_linked_list()     
            tail.large = self 
            self.small = tail 
            return (head, self)

        if not self.left and self.right:       
            (head, tail) = self.right.convert_to_doubly_linked_list()
            self.large = head 
            tail.large = self 
            self.small = tail 
            head.small = self 
            return (self, tail)

        (leftHead, leftTail) = self.left.convert_to_doubly_linked_list()
        (rightHead, rightTail) = self.right.convert_to_doubly_linked_list()
        self.small = leftTail 
        self.large = rightHead 
        leftHead.small = rightTail 
        leftTail.large = self 
        rightHead.small = self 
        rightTail.large = leftHead 
        return (leftHead, rightTail)   


# Tests 
root = Node(6)
root.left = Node(4)
root.right = Node(10)
root.right.right = Node(11)
root.left.left = Node(2)
root.left.right = Node(5)
root.left.left.left = Node(1)
root.left.left.right = Node(3)
(head, tail) = root.convert_to_doubly_linked_list()

cur = head
for i in xrange(1, 20):
    print cur.value, 
    cur = cur.large

print 
cur = tail
for i in xrange(1, 20):
    print cur.value,
    cur = cur.small

print
