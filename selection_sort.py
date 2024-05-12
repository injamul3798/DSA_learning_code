def selection_sort(arr):
    n = len(arr)
    for i in range(0,n):
        min_index = i
        for j in range(i+1,n):
            if(arr[min_index]>arr[j]):
               min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    print("Sorted List is : ",arr)
lis = [2,232,12,12,-1,23,2,-12]
selection_sort(lis)