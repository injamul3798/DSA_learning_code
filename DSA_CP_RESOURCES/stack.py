class Stack:
    def __init__(self):
        self.max_stack_value = None
        self.stack = []
    
    def addItem(self,val):
        self.stack.append(val)
        if not self.max_stack_value or val > self.max_stack_value:
            self.max_stack_value = val
    def removeItem(self):
        # if self.stack:
        #     self.stack.pop()
        # if self.max_stack_value:
        #     self.max_stack_value.pop()
        if self.stack:
            curr = self.stack.pop()
            if curr== self.max_stack_value:
                if self.stack:
                    self.max_stack_value = max(self.stack)
                else:  
                
                    self.max_stack_value  = None
    def print_stack(self):
        if self.max_stack_value:
            # for i in range(len(self.queue)):
            #     print(self.queue[i])
            # print(self.max_stack_value[-1])
            print(self.max_stack_value)
        
        

if __name__ =='__main__':
    t = int(input())
    values = Stack()
    for _ in range(t):
        lis = list(map(int,input().split()))
        if len(lis) ==2 and lis[0] == 1:
            values.addItem(lis[1])
        elif lis[0] == 2:
            values.removeItem()
        elif lis[0] == 3:
            values.print_stack()
        
