import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid =len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)
    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    i = j = 0
    result = []
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1
    result += left_arr[i:]
    result += right_arr[j:]
    return result


my_list = []


for i in range(10):
    my_list.append(random.randint(1, 100))
print("List Awal:")
print(my_list)


print("Sebelum disortir :", my_list)
print("Setelah disortir :", merge_sort(my_list))