class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_the_first(self,val):
       
        node = Node(val)
        node.next = self.head
        self.head = node
        
    def insert_at_the_end(self,val):
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = node
    def insert_at_position(self,val,pos):
        node = Node(val)
        if not self.head:
            self.head = node
            return
        current = self.head
        for _ in range(pos-1):
            current = current.next
        node.next = current.next
        current.next = node
        
    def delete_at_position(self,pos):
        current = self.head
        for _ in range(pos-1):
            current = current.next
        current.next = current.next.next
        
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

data = int(input('New Data to be inserted: '))
pos = int(input('Position: '))
lis.insert_at_position(data,pos)

lis.print_lis()
val = int(input('New Data to be inserted in front: '))
lis.insert_at_the_first(val)
lis.print_lis()
print('after deleting: ')

lis.delete_at_position(2)
lis.print_lis()