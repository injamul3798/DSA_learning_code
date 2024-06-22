#Code for Liner search
def search_value(lis,value):
    for i in range(len(lis)):
        if lis[i] == value:
            return i
    return -1
#make a list
lis = [2,23,1,45,66,34,232,13,53,532]
target_value = 23
index = search_value(lis,target_value)
print(index)
if index != -1 :
    print(f"Element {target_value} found at index {index}")
else:
    print("Not found")