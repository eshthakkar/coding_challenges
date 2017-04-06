# Reverse a stack in place problem
def reverse_stack(st):

    if not is_empty(st):
        temp = pop(st)
        reverse_stack(st)
        insert_at_bottom(st, temp)


def insert_at_bottom(st, item):
    if is_empty(st):
        push(st, item)
    else:
        temp = pop(st) 
        insert_at_bottom(st, item)
        push(st, temp)   
      

def create_stack():
    """ Fuction to create an empty stack"""

    stack = []
    return stack


def is_empty(stack):
    """ Function to check if the stack is empty"""

    return len(stack) == 0    


def push(stack, item):
    """ Function to add an item on top of the stack"""

    stack.append(item)


def pop(stack):
    """ Function to pop an item from top of the stack"""

    if is_empty(stack):
        print "Stack Underflow!" 
        exit(1)

    return stack.pop()


def prints(stack):
    """ Function to print the stack"""

    for i in xrange(len(stack)-1, -1, -1):
        print stack[i]
    print
        

# Driver program to test above functions
stack = create_stack()
push(stack, str(5))        
push(stack, str(4))        
push(stack, str(3))        
push(stack, str(2))        
push(stack, str(1))
print("Original Stack ")
prints(stack)

reverse_stack(stack)

print "Reversed Stack "
prints(stack)        

