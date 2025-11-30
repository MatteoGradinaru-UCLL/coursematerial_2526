# Write your code here
class Counter:
    def __init__(self):
        self.counter = 0

    def increment(self):
        self.counter += 1
    
    def get_count(self):
        return self.counter
    
    def reset(self):
        self.counter = 0


counter = Counter()

print(counter.get_count())