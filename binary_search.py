
# Binary search 
def binary_search(lis,value):
    left = 0
    right = len(lis)
    mid = (left + right)//2

    while(left<right):
        if(lis[mid] == value):
            return mid
        elif(lis[mid] < value):
            left = mid+1
            mid = (left + right) //2
        else:
            right = mid - 1
            mid = (left + right) //2

    return -1

lis = [2,3,4,33,45,66,67,70,77]
target_value = 70
index = binary_search(lis,target_value)
if index != -1:
    print("Element found at index",index)
else:
    print("Element not found")
