# check the stack is empty or not 
def is_empty(stack):
    return len(stack) == 0

# get the first element
def top_element(stack):
    return stack[0]


from collections import deque

stack = deque()


# append element into stack 
stack.append('Injam')
stack.append('Najmus')
stack.append('Shakil')

print("Stack List : ",stack)



# Pop element from the list
stack.pop()
stack.pop()

print("Stack List : ",stack)

print('Stack is empty: ',is_empty(stack))
print('Top element: ',top_element(stack))



