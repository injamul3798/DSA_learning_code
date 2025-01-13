class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_the_end(self,val):
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = node
    def print_lis(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next


n = int(input())
lis = LinkedList()
for _ in range(n):
    lis.insert_at_the_end(int(input()))
lis.print_lis()
