class TreeNode:
    def __init__(self, data):
        # Each node can have children, a parent, and data
        self.data = data
        self.children = []  # A list that will store the child nodes of this node
        self.parent = None  # Will keep track of the parent node

    def add_child(self, child):
        """
        This method adds a child node to the current node by appending the child to self.children.
        It also sets the parent of the child to the current node (to keep track of relationships).
        """
        child.parent = self
        self.children.append(child)

    def get_levels(self):
        """
        This method calculates the level (depth) of the current node in the tree.
        """
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent  # Move up to the parent node
        return level

    def print_tree(self):
        """
        This method prints the tree structure starting from the current node.
        Indentation is used to show levels of the tree.
        """
        spaces = ' ' * self.get_levels() * 3
        print(spaces + self.data)
        for child in self.children:
            child.print_tree()


def build_tree():
    root = TreeNode("Computer Science")

    node1 = TreeNode("Programming")
    node1.add_child(TreeNode("C++"))
    node1.add_child(TreeNode("Python"))

    node2 = TreeNode("OOP")
    node2.add_child(TreeNode("Abstraction"))
    node2.add_child(TreeNode("Inheritance"))

    node3 = TreeNode("DSA")
    node3.add_child(TreeNode("Tree"))
    node3.add_child(TreeNode("Graph"))

    root.add_child(node1)
    root.add_child(node2)
    root.add_child(node3)

    root.print_tree()


if __name__ == '__main__':
    build_tree()
