class Stack():
    def __init__(self):
        self.item = []
    def append(self,item):
        self.item.append(item)
    def pop(self):
        if self.is_empty():
            return None
        else:
            self.item.pop()
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.item[-1]
    def display(self):
        print(self.item[::-1])
    def is_empty(self):
        return len(self.item) == 0
s = Stack()
s.append(1)
s.append(3)
s.append(4)
s.display()
print(s.peek())
s.pop()
print("After pop: ")
s.display()