class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Inserting element at the beginning
    def insert_at_the_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Inserting element at the end
    def insert_at_the_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    # Deleting element at a certain position
    def delete_at_certain_position(self, position):
        if self.head is None:
            print("List is empty")
            return
        if position == 0:
            self.head = self.head.next
            return
        current_node = self.head
        index = 0
        while current_node and index < position - 1:
            current_node = current_node.next
            index += 1
        if current_node is None or current_node.next is None:
            print("Position out of bounds")
            return
        current_node.next = current_node.next.next

    # Inserting element at a specific position
    def insert_at_position(self, value, position):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        current_position = 0
        while current_node and current_position < position - 1:
            current_node = current_node.next
            current_position += 1
        if current_node is None:
            print("Position out of bounds")
            return
        new_node.next = current_node.next
        current_node.next = new_node

    # Updating element at a specific position
    def update_node_at_position(self, value, position):
        current_node = self.head
        index = 0
        while current_node and index != position:
            current_node = current_node.next
            index += 1
        if current_node is None:
            print("Position out of bounds")
            return
        current_node.value = value

    # Print the linked list
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

# Testing the LinkedList implementation
ll = LinkedList()
ll.insert_at_the_beginning(3)
ll.print_list()

ll.insert_at_the_beginning(2)
ll.print_list()

ll.insert_at_the_beginning(1)
ll.print_list()

ll.insert_at_the_end(4)
ll.print_list()

ll.insert_at_the_end(5)
ll.print_list()

ll.insert_at_position(2.5, 2)
ll.print_list()

ll.delete_at_certain_position(3)
ll.print_list()

ll.update_node_at_position(10, 0)
ll.print_list()

ll.update_node_at_position(20, 2)
ll.print_list()
