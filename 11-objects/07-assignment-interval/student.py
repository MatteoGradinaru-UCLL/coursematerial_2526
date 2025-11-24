class Interval:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    
    def is_empty(self):
        if self.lower > self.upper:
            return True
        else:
            return False
        
    def contains(self, value):
        if self.lower <= value <= self.upper:
            return True
        else:
            return False
        
    def overlaps_with(self, other):
        if ():
            