class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def reverse_lis(self, head):
        current = head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def print_list(self, head):
        current = head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()  # Newline for readability


t = int(input())
for _ in range(t):
    n = int(input())
    lis = LinkedList()
    for _ in range(n):
        lis.insert_at_end(int(input()))
    
    reversed_head = lis.reverse_lis(lis.head)
    lis.print_list(reversed_head)
