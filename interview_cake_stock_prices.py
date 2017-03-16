#O(n) time complexity using greedy approach and O(1) space complexity
def get_max_profit(stock_prices_yesterday):
    """Write an efficient function that takes stock_prices_yesterday 
       and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

       >>> print get_max_profit([10, 7, 5, 8, 11, 9])  
       6

       >>> print get_max_profit([4,8,3,5])
       4
    """

    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires atleast two prices')

    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday):

        # skip the first (0th) time
        # we can't sell at the first time, since we must buy first,
        # and we can't buy and sell at the same time!
        # if we took this out, we'd try to buy *and* sell at time 0.
        # this would give a profit of 0, which is a problem if our
        # max_profit is supposed to be *negative*--we'd return 0!

        if index == 0:
            continue

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price    
        
        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # update min_price so it's always
        # the lowest price we've seen so far
        min_price = min(min_price, current_price)

    return max_profit 
 

# O(n^2 runtime)
def my_function(runtime,movie_lengths):
    # write the body of your function here
    for i in xrange(len(movie_lengths) - 1):
        for j in xrange(i+1,len(movie_lengths)):
            movie1 = movie_lengths[i]
            if movie_lengths[j] == runtime - movie1:
                return True
    return False


# O(n) runtime and spacetime due to the set
def solution2(runtime,movie_lengths):
    """
        >>> print solution2(5,[2,4,6,1]) 
        True
    """
    movie_lengths_seen = set()

    for first_movie in movie_lengths:
        second_movie = runtime - first_movie
        if second_movie in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie)
    return False            




# O(n) time complexity and O(1) space complexity
def find_unique_delivery_id(delivery_ids):
    """ Given the list of IDs, which contains many duplicate integers and one unique integer, 
    find the unique integer.

        >>> delivery_ids = [2,5,6,3,3,2,6]
        >>> print find_unique_delivery_id(delivery_ids)
        5
    """

    unique_id = 0

    for delivery_id in delivery_ids:
        unique_id ^= delivery_id

    return unique_id
    

# O(n) runtime and O(1) space complexity
def max_product_of_3(nums):
    """ Given a list of integers, find the highest product you can get from three of the integers.

        >>> nums = [1, 10, -5, 1, -100]
        >>> print max_product_of_3(nums)
        5000
    """

    if len(nums) < 3:
        raise Exception("Less than 3 items!")


    highest = max(nums[0], nums[1])
    lowest = min(nums[0], nums[1])

    highest_product_of_2 = nums[0] * nums[1]
    lowest_product_of_2 = nums[0] * nums[1]

    highest_product_of_3 = nums[0] * nums[1] * nums[2]

    for current in nums[2:]:

        # Debugging
        # print "highest_product_of_3: ", highest_product_of_3
        # print "highest_product_of_2: ", highest_product_of_2
        # print "lowest_product_of_2: ", lowest_product_of_2
        # print "highest: ", highest
        # print "lowest: ", lowest


        highest_product_of_3 = max(highest_product_of_3, current * highest_product_of_2, current * lowest_product_of_2) 

        highest_product_of_2 = max(highest_product_of_2, current * highest, current * lowest)

        lowest_product_of_2 = min(lowest_product_of_2, current * highest, current * lowest)

        highest = max(highest, current)

        lowest = min(lowest, current)

    return highest_product_of_3    


# O(n) runtime and O(1) space complexity
def fibonacii(n):
    """ Return the nth fibonacii number
        >>> fibonacii(3)
        2

        >>> fibonacii(1)
        1

        >>> fibonacii(4)
        3
    """

    if n in [0, 1]:
        return n

    prev_prev = 0
    prev = 1

    for i in xrange(2,n+1):
        result = prev_prev + prev
        prev_prev = prev
        prev = result
    return result        


# O(n*k) time complexity and O(k) space complexity where n is the number of types of cakes, k is the capacity of the duffel bag.
def max_duffel_bag_value(cake_tuples,weight_capacity):
    """ Write a function max_duffel_bag_value() that takes a list of cake type tuples and a weight capacity,
     and returns the maximum monetary value the duffel bag can hold.

        >>> cake_tuples = [(7, 160), (3, 90), (2, 15)]
        >>> capacity    = 20
        >>> max_duffel_bag_value(cake_tuples, capacity)
        555
    """

    max_values_at_capacities = [0] * (weight_capacity + 1)

    for current_capacity in xrange(weight_capacity + 1):

        max_value_at_current_capacity = 0

        for cake_weight, cake_value in cake_tuples:

            if cake_weight == 0 and cake_value != 0:
                return float("inf")

            if cake_weight <= current_capacity:
                
                max_value_at_current_capacity = max(max_value_at_current_capacity, cake_value + max_values_at_capacities[current_capacity - cake_weight])

        max_values_at_capacities[current_capacity] = max_value_at_current_capacity

    return max_values_at_capacities[weight_capacity]


# Our m enqueue and dequeue operations put m or fewer items into the system, giving a total runtime of O(m). 
#  total cost per item passing through the queue is O(1) rather than the cost per enqueue() and dequeue()
class QueueTwoStacks(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                newest_item = self.in_stack.pop()
                self.out_stack.append(newest_item)

            if len(self.out_stack) == 0:
                raise IndexError("Can't dequeue from an empty queue")

        return self.out_stack.pop()                    


class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop() 

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]  

        
# O(1) time for push(), pop(), and get_max(). O(m) additional space, where m is the number of operations performed on the stack.
class MaxStack(object):
    def __init__(self):
        self.stack = Stack()
        self.maxs_stack = Stack()


    def push(self, item):
        self.stack.push(item)
        if self.maxs_stack.peek() is None or item >= self.maxs_stack.peek():
            self.maxs_stack.push(item) 


    def pop(self):
        item = self.stack.pop()

        if item == self.maxs_stack.peek():
            self.maxs_stack.pop()

        return item
        
    def get_max(self):
        return self.maxs_stack.peek()                


# Delete node from linked list without traversing. O(1) time and O(1) space complexity. Not a very good solution as
# it has side effects like the deleted node has a new value, it is not deleted, also the next node becomes dangling and can't
# be reached while traversing the list.
def delete_node(node_to_delete):
    """ Delete a node from a linked list given only a reference to the node to be deleted"""

    next_node = node_to_delete.next

    if next_node:
        node_to_delete.value = next_node.value
        node_to_delete.next = next_node.next

    else:
        raise Exception("Cannot delete last node using this method")    


# O(n) time and O(1) space complexity
def contains_cycle(first_node):
    """ Write a function contains_cycle() that takes the first node in a singly-linked list
     and returns a boolean indicating whether the list contains a cycle. """

    slow_runner = first_node
    fast_runner = first_node

    while fast_runner is not None and fast_runner.next is not None:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        if fast_runner is slow_runner:
            return True

    return False  


# O(n) time and O(1) space complexity
def reverse_in_place(head):
    """ Reverse a linked list in place"""

    current = head
    prev = None
    next = None

    while current: 
        next = current.next

        current.next = prev

        prev = current
        current = next

    return prev    


# O(n) time and O(1) space complexity
def kth_to_last_node(k, head):
    """ Return the kth to the last node from the linked list"""

    if k < 1:
        raise Exception("Cannot return a node which is less than one from the last node")

    left = head    
    right = head

    # Positioning the right pointer k nodes apart from the left pointer
    for i in xrange(k-1):

        if not right.next:
            raise valueError("k is larger than the length of the linked list")

        right = right.next

    while right.next:
        left = left.next
        right = right.next

    # since left is k nodes behind right, left is the kth node to the last node!    
    return left    


# O(n) time complexity and O(1) space complexity
def reverse_string(word):
    """ Reverse a string in place
        >>> print reverse_string("acbdl")
        ldbca

        >>> print reverse_string("a")
        a

    """

    left_pointer = 0
    right_pointer = len(word) - 1

    str_list = list(word)

    while left_pointer < right_pointer:
        str_list[left_pointer], str_list[right_pointer] = str_list[right_pointer], str_list[left_pointer]

        left_pointer += 1
        right_pointer -= 1

    return "".join(str_list)    


def reverse_characters(str_list, begin, end):

    while begin < end:
        str_list[begin], str_list[end] = str_list[end], str_list[begin]

        begin += 1
        end -= 1

    return str_list   

# O(n) time and O(n) space due to the msg_list
def reverse_words_not_using_inbuilt(message):
    """ Reverse the word order in the whole message

        >>> message = 'find you will pain only go you recordings security the into if'
        >>> print reverse_words_not_using_inbuilt(message)
        if into the security recordings you go only pain will you find
    """

    msg_list = list(message)

    reverse_characters(msg_list, 0, len(msg_list)-1)

    current_word_start_index = 0

    for i in xrange(len(msg_list) + 1):

        #  Found end of word
        if i == len(msg_list) or msg_list[i] == " ":
            reverse_characters(msg_list, current_word_start_index, i - 1)

            # next word's start is 1 character ahead
            current_word_start_index = i + 1

    return "".join(msg_list)        
   
            

            

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()

    if not result.failed:
        print "All tests passed! GOOD WORK!"
    print    

