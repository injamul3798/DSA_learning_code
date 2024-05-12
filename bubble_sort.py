
# Time complexicity : O(n^2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                #swap the values
                arr[j],arr[j+1] = arr[j+1],arr [j]
                
    print("The sorted list is : ",arr)
                
lis = [34,2,3,11,56,3,-3]
bubble_sort(lis)