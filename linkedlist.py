class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:

    def __init__(self,value):
        self.head = Node(value)

    def printlist(self):
        node = self.head 
        while node is not None:
            print (node.data)
            node = node.next
    def add(self,value):
        node = self.head
        while node.next is not None:
            node = node.next
        node.next=Node(value)

obj = Linkedlist(1)

obj.add(2)
obj.add(3)
obj.add(4)
obj.add(5)
obj.printlist()