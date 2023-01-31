class Node:
    def __init__(self, value: int, next = None):
        self.value = value
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < self.size:
            temp = self.head
            while index > 0:
                temp = temp.next
                index -= 1
            return temp.value
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val, next=self.head)
        self.head = node
        self.size += 1


    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        else:
            self.head = node    
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
        elif index < self.size:
            i = 0
            temp = self.head
            while i < index - 1:
                temp = temp.next
                i += 1
            node = Node(val, next=temp.next)
            temp.next = node
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            if index == 0:
                self.head = self.head.next
                return
            i = 0
            temp = self.head
            while i < index - 1:
                temp = temp.next
                i += 1
            if temp.next:
                temp.next = temp.next.next
            self.size -= 1
            
        

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
print(obj.get(1), 2)
obj.deleteAtIndex(1)
print(obj.get(1), 3)