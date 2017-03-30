from interview_cake_stock_prices import LinkedList, LL_node, print_list


def split_in_half(head):
    """Problem: Split a linked list in 2 lists at its center, if odd nodes, extra node should go in the first list
       Complexity: O(n) time and space

        Tests:

        1. List with even no. of nodes

        >>> ll = LinkedList()
        >>> ll.append(3)
        >>> ll.append(10)
        >>> ll.append(6)
        >>> ll.append(15)
        >>> ll.append(9)
        >>> ll.append(13)

        Print the original linked list
        >>> print_list(ll.head)
        3 10 6 15 9 13

        Splits the above list in 2 equal halves
        >>> second_list = split_in_half(ll.head)
        >>> print_list(ll.head)
        3 10 6
        >>> print_list(second_list)
        15 9 13

        -----------------------------------------------
        2. Split an empty linked list

        >>> print split_in_half(None)
        None

        -----------------------------------------------
        3. Split a list with just one node

        >>> ll = LinkedList()
        >>> ll.append(3)
        >>> print_list(ll.head)
        3
        >>> print split_in_half(ll.head)
        None

        -----------------------------------------------
        4. Split a list with 2 nodes
        >>> ll = LinkedList()
        >>> ll.append(3)
        >>> ll.append(1)
        >>> print_list(ll.head)
        3 1
        >>> list2 = split_in_half(ll.head)
        >>> print_list(ll.head)
        3
        >>> print_list(list2)
        1

        -------------------------------------------------
        5. Split a list with odd no. of nodes
        >>> ll = LinkedList()
        >>> ll.append(3)
        >>> ll.append(2)
        >>> ll.append(1)
        >>> ll.append(6)
        >>> ll.append(7)
        >>> print_list(ll.head)
        3 2 1 6 7
        >>> l2 = split_in_half(ll.head)
        >>> print_list(ll.head)
        3 2 1
        >>> print_list(l2)
        6 7

    """

    # if the linked list to be divided is empty or has just one node, just return
    if not head or not head.next:
        return

    sr = head
    fr = head

    while (fr.next and fr.next.next):

        fr = fr.next.next
        sr = sr.next

    first_node_for_second_list = sr.next

    sr.next = None
    new_list = LinkedList()

    new_list.head = first_node_for_second_list

    return new_list.head  


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()

    if not result.failed:
        print "All tests passed. Good work!"

    print            
