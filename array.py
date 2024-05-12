
#Time complexity of the problem is: O(n)
def find_smallest_value(lis):
    initital_min = lis[0]
    print(initital_min)
   # j = 0
    for j in lis:
        if j<initital_min:
            initital_min = j
            
    print("Minimum value of array is : ",initital_min)
    
arr = [2,3,4,2,33434,1,2]

find_smallest_value(arr)

'''def find_smallest_value(lis):
    initital_min = min(lis)
   
            
    print("Minimum value of array is : ",initital_min)
    
arr = [2,3,4,232,432,1,2]

find_smallest_value(arr)





print("largest")'''

    
    