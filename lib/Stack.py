#impliment a stack, use a list as the underlying data structure
#Call on built-in list methods to build your Stack class' functionality
#Use search() method

class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            self.items = []
        else:
            self.items = list(items)
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            item = self.items.pop()
            return item

    def peek(self):
        pass
    
    def size(self):
        length = len(self.items)
        return length

    def full(self):
        if len(self.items) == self.limit:
            return True
        else: 
            return False

    def search(self, target):
        try:
            index = self.items.index(target)
            print(target, index)
            distance = len(self.items) - index -1
            return distance
        except ValueError:
            return -1
