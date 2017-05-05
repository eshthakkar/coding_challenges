from queue import *

# make it for n seconds 
class WebHits(object):
    def __init__(self, n=300):
        self.queue = Queue(maxsize=n - 1)
        self.last_second = 0
        self.sec_hits_count = 0
        self.last_n-1th_hit_count = 0

    def record_hit(self):
        """ Record the hit for the corresponding time whenever there is a visitor on the webpage"""

        self.reset()
        self.sec_hits_count += 1

    def get_last_n_seconds_hit_count(self):
        """ Get the web hit count for the last n seconds"""

        self.reset()
        return self.last_n-1th_hit_count + self.sec_hits_count

    def reset():
        """ Reset the appropriate variables to the most updated values 
            before recording a hit and giving out last 5 min hit count"""

        while epoch_time() != self.last_second:

            oldest_item = self.queue.get()
            self.queue.put(self.sec_hits_count) 
            self.last_n-1th_hit_count = self.last_n-1th_hit_count - oldest_item + self.sec_hits_count
            self.sec_hits_count = 0
            self.last_second += 1      


# #(time_in_seconds, "type of function", expected value)

# [ 
#   (0.1, "hit", 0), 
#   (0.2, "hit", 0), 
#   (0.22, "count", 2), 
#   (1.2, "hit", 0), 
#   (1.5, "count", 0)
# ]