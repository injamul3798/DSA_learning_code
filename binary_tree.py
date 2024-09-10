# Create a empty node with left right node set to zero initally
class Node():
    def __init__(self,data):
        self.data = data
        self.left  = None
        self.right  = None

# add element into the tree
def insert_node(root,value):
    if root is None:
        return Node(value)   # make it frist node while checking 

    if value < root.data:
        root.left = insert_node(root.left,value)  # insert in left  position
    elif value > root.data:
        root.right  = insert_node(root.right,value) # insert the right positon
    else :
        pass
    return root

# In order traversal
def print_tree_using_inorder(root):
    if root:
        print_tree_using_inorder(root.left)
        print(root.data, end = " ")
        print_tree_using_inorder(root.right)

# Pre- order traversal
def print_using_pre_order(root):
    if root:
        print(root.data,end  = " ")
        print_using_pre_order(root.left)
        print_using_pre_order(root.right)

# Post order traversal
def print_using_post_order(root):
    if root:
        print_using_post_order(root.left)
        print_using_post_order(root.right)
        print(root.data,end  = " ")    

root = None
nodes = [20, 10, 30, 5, 15, 25, 35]

for node in nodes:
    root = insert_node(root,node)

print('Tree using Pre order : ' )
print_using_pre_order(root)


print('\nTree using In order : ' )
print_tree_using_inorder(root)

print('\nTree using Post order : ' )
print_using_post_order(root)


print("\nSuccessfully print the tree")
