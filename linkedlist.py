class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Linkedlist:

    def __init__(self,value=None):
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

    def we(self,value):
        node = self.head 
        while node is not None:
            print (node.next.data)
            # if node.next.data == value:
            #     node.next = node.next.next
            node = node.next


    def delete_alt(self, data):
        if data is None:
            return
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prev_node = self.head
        curr_node = self.head.next
        while curr_node is not None:
            if curr_node.data == data:
                prev_node.next = curr_node.next
                return
            prev_node = curr_node
            curr_node = curr_node.next

    def insert_to_frent(self,value=None):
        if value is None:
            return None
        node = Node(value, self.head)
        self.head = node
        return node


    def printfirstelemnt(self):
        if self.head  is None:
            return None
        else:
            return self.head.data


    def lastelemet(self):
        node = self.head
        while node.next is not None:
            node  = node.next
        return node.data

obj = Linkedlist(1)
obj.add(2)
obj.add(3)
obj.add(4)
obj.add(5)
obj.add(6)
obj.add(7)
obj.add(8)
# obj.printlist()
# obj.insert_to_frent(10)
# # print ("--------------------")
# print (obj.printfirstelemnt())
# print (obj.lastelemet())
# obj.printlist()
# obj.printlist()
obj.delete_alt()
print ("--------------------")
obj.printlist()
