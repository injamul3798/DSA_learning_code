class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.head = None
        
    #Creating Tree
    def build_tree(self,val):
        # Making root Node
        if not self.head:
            self.head = Node(val)
        else:
            current = self.head
            while True:
                # Building Left Tree
                if current.val > val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
       
    def print_tree_using_pre_order(self,root):
        if root:
            print(root.val)
            if root.left:
                self.print_tree_using_pre_order(root.left)
            if root.right:
                self.print_tree_using_pre_order(root.right)
    def print_tree_using_post_order(self,root):
        if root:
            if root.left:
                self.print_tree_using_post_order(root.left)
            if root.right:
                self.print_tree_using_post_order(root.right)
            print(root.val)
        # if root:
        #     print(root.val)
        #     if root.left:
        #         self.print_tree_using_pre_order(root.left)
        #     if root.right:
        #         self.print_tree_using_pre_order(root.right)
    def print_tree_using_in_order(self,root):
        if root:
            if root.left:
                self.print_tree_using_in_order(root.left)
            print(root.val)
            if root.right:
                self.print_tree_using_in_order(root.right)

    # find the hight of the binary treee or level of the binary tree
    def find_hight_of_binary_tree(self,root):
        queue = deque([root])
        cnt = 0
        while queue:
            level = len(queue)
            cnt += 1
            while level:
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                level -= 1
        return cnt-1

    # Print value by Level order Tree
    def levelOrder(root):
        queue = deque([root])
            
        while queue:
            level = len(queue)
            
            while level:
                current = queue.popleft()
                print(current.info,end = ' ')
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                level -= 1

         

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int,input().split()))
        obj = Tree()
        for val in arr:
            obj.build_tree(val)
        print("In-order Traversal:")
        obj.print_tree_using_in_order(obj.head)
        print("\nPre-order Traversal:")
        obj.print_tree_using_pre_order(obj.head)
        print("\nPost-order Traversal:")
        obj.print_tree_using_post_order(obj.head)
        print()
        
        
