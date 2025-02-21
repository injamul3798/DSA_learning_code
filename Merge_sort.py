def merge(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge(arr[:mid])
    print('Left : ',left)
    right = merge(arr[mid:])
    print('Right: ',right)
    return merge_two_sorted_list(left, right)
     

def merge_two_sorted_list(a, b):
    i = j = k = 0
    len_a = len(a)
    len_b = len(b)
    ln = len_a + len_b
    ans  = [0]*ln
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            ans[k] = a[i]
            i += 1
        else:
            ans[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        ans[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        ans[k] = b[j]
        j += 1
        k += 1
    return ans
        

test_cases = [
    # [10, 3, 15, 7, 8, 23, 98, 29],
    [10, 3, 15, 7],
    [20,1,4],
    [3,2,1,5,6]
]

for test in test_cases:
    print("Sorted list: ",merge(test))
#user_input = [10, 3, 15, 7, 8, 23, 98, 29]
#print("Sorted list: ",merge(user_input))
