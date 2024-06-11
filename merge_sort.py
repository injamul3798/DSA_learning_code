def merge(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge(left)
    merge(right)
    merge_two_sorted_list(left, right, arr)
    return arr

def merge_two_sorted_list(a, b, arr):
    i = j = k = 0
    len_a = len(a)
    len_b = len(b)

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1
        

test_cases = [
    [10, 3, 15, 7, 8, 23, 98, 29],
    [10, 3, 15, 7],
    [20,1,4],
    [3,2,1,5,6]
]

for test in test_cases:
    print("Sorted list: ",merge(test))
#user_input = [10, 3, 15, 7, 8, 23, 98, 29]
#print("Sorted list: ",merge(user_input))
