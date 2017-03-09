# O(1) time complexity for each function and O(1) space related to input as we are not storing all inputs
class TempTracker(object):
    def __init__(self):

        # for mean
        self.sum = 0.0
        self.length = 0
        self.mean = None

        # for min and max
        self.min_temp = None
        self.max_temp = None

        # for mode
        self.occurrences = [0] * 111
        self.max_occurrences = 0
        self.mode = None

    def insert(self,temp):
        """ Records a new temperature"""

        # for min and max
        if self.min_temp is None or temp < self.min_temp:
            self.min_temp = temp

        if self.max_temp is None or temp > self.max_temp:
            self.max_temp = temp
    
        # for mean
        self.sum += temp
        self.length += 1
        self.mean = self.sum/self.length

        # for mode
        self.occurrences[temp] += 1

        if self.occurrences[temp] > self.max_occurrences:
            self.mode = temp
            self.max_occurrences = self.occurrences[temp]



    def get_max(self):
        """ Returns the highest temperature seen so far"""

        return self.max_temp

    def get_min(self):
        """ Returns the lowest temperature seen so far"""

        return self.min_temp

    def get_mean(self):
        """ Returns the mean of all values"""

        return self.mean

    def get_mode(self):
        """ Returns the mode"""

        return self.mode

t = TempTracker()
t.insert(110)
t.insert(72)
t.insert(65)
t.insert(65)
print t.get_max()
print t.get_min()
print t.get_mean()
print t.get_mode()                             