def inertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        initial_step = arr[i]
        j = i-1
        while(j>=0 and initial_step<arr[j]):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = initial_step
    print("Sorted List here: ",arr)
lis = [3,2,23,2,32,-1,2,2,-44]
inertion_sort(lis)