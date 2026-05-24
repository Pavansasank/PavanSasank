from collections import deque

class Queue():
    def __init__(self):
        self.queue = deque()
    def enqueue(self,Data):
        self.queue.append(Data)
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        else:
            self.queue.popleft()
    def display(self):
        print(self.queue)
    def size(self):
        print(f"Size of Queue: {len(self.queue)}")
    


q = Queue()
q.enqueue("Pavan")
q.enqueue("ram")
q.enqueue("Ravan")
q.enqueue("Sai")
q.display()
q.dequeue()
q.display()
q.size()

