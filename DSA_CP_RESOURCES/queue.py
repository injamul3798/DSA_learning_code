class Queue:
    def __init__(self):
        self.queue = []
    
    def enque(self,val):
        self.queue.append(val)
    def deque(self):
        if self.queue:
            self.queue.pop(0)
    def print_queue(self):
        if self.queue:
            # for i in range(len(self.queue)):
            #     print(self.queue[i])
            print(self.queue[0])
        
        

if __name__ =='__main__':
    t = int(input())
    values = Queue()
    for _ in range(t):
        lis = list(map(int,input().split()))
        if len(lis) ==2 and lis[0] == 1:
            values.enque(lis[1])
        elif lis[0] == 2:
            values.deque()
        elif lis[0] == 3:
            values.print_queue()
        