# O(n) time complexity

def activity_selector(activity):
    """Give a solution to choose maximum mutually independent activities that share a resource.
        Activities are initially sorted by their end times
        
        >>> activities = [(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]    
        >>> print activity_selector(activities) 
        [(1, 4), (5, 7), (8, 11), (12, 16)]

        >>> activities = [(2,3),(2,5),(3,6),(3,7),(8,10)] 
        >>> print activity_selector(activities)
        [(2, 3), (3, 6), (8, 10)]
    """

    max_array = [activity[0]]
    k = 0

    for i in xrange(1,len(activity)):
        if activity[i][0] >= activity[k][1]:  # Find next activity whose start time is greater than the previous max activity end time
            max_array.append(activity[i])
            k = i
    return max_array


#O(nlogn) time complexity and O(n) space complexity
def merge_ranges(meetings):
    """ Write a function that takes a list of meeting time ranges and returns a list of condensed ranges.
        >>> meetings = [(1,10), (7,9), (3,5), (2,6)]
        >>> print merge_ranges(meetings)
        [(1, 10)]

        >>> meetings = [(1, 2), (2, 3)]
        >>> print merge_ranges(meetings)
        [(1, 3)]

        >>> meetings = [(1, 5), (2, 3)]
        >>> print merge_ranges(meetings)
        [(1, 5)]

        >>> meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
        >>> print merge_ranges(meetings)
        [(0, 1), (3, 8), (9, 12)]
    """

    # sort the meetings by start time
    meetings.sort(key=lambda tup: tup[0])

    merged_meetings = [meetings[0]]

    for current_meeting_start, current_meeting_end in meetings[1:]:

        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        if current_meeting_start <= last_merged_meeting_end:
            merged_meetings[-1] = (last_merged_meeting_start, max(current_meeting_end,last_merged_meeting_end))

        else:
            merged_meetings.append((current_meeting_start,current_meeting_end)) 

    return merged_meetings           


            





if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

