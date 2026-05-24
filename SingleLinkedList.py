class Node:
    def __init__(self,info,next =None):
        self.data = info
        self.next = next

class SingleLinkedList:
    def __init__(self,head = None):
        self.head = head
    
    def InsertAtEnd(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next
if __name__ == "__main__":
    sll = SingleLinkedList()
    sll.InsertAtEnd(1)
    sll.InsertAtEnd(2)
    sll.InsertAtEnd(3)
    sll.InsertAtEnd(4)
    sll.InsertAtEnd(5)
    sll.printLL()