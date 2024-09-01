class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Double_Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_the_beginning(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_the_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        new_node.prev = current_node
        current_node.next = new_node

    def insert_at_position(self, value, position):
        new_node = Node(value)
        if self.head is None:
            print("List is empty, insertion operation can't be performed")
            return
        if position == 0:
            self.insert_at_the_beginning(value)
            return
        current_node = self.head
        current_index = 0
        while current_node.next is not None and current_index < position - 1:
            current_node = current_node.next
            current_index += 1
        if current_node.next is None:
            self.insert_at_the_end(value)
        else:
            new_node.next = current_node.next
            new_node.prev = current_node
            current_node.next.prev = new_node
            current_node.next = new_node

    def update_node_at_position(self, value, position):
        current_node = self.head
        index = 0
        while current_node is not None and index != position:
            current_node = current_node.next
            index += 1
        if current_node is None:
            print("Position out of bounds")
            return
        current_node.value = value

    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty, deletion operation can't be performed")
            return
        if position == 0:
            if self.head.next is not None:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
            return

        current_node = self.head
        current_index = 0
        while current_node.next is not None and current_index < position:
            current_node = current_node.next
            current_index += 1
        
        if current_node is None:
            print("Position out of bounds")
            return

        if current_node.next is not None:
            current_node.next.prev = current_node.prev

        if current_node.prev is not None:
            current_node.prev.next = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print('Node', current_node.value)
            current_node = current_node.next

# Test cases
l1 = Double_Linked_list()
l1.insert_at_the_beginning(5)
l1.insert_at_the_beginning(4)
l1.insert_at_the_beginning(3)

print('Before insertion:')
l1.print_list()

l1.insert_at_position(10, 2)
print('After inserting 10 at position 2:')
l1.print_list()

l1.update_node_at_position(15, 1)
print('After updating node at position 1 to 15:')
l1.print_list()

l1.delete_at_position(2)
print('After deleting node at position 2:')
l1.print_list()

l1.delete_at_position(0)
print('After deleting head node at position 0:')
l1.print_list()
