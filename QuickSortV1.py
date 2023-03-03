import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)

my_list = []

for i in range(10):
    my_list.append(random.randint(1, 100))
print("List Awal:")
print(my_list)

my_list = quick_sort(my_list)
print("\nList setelah diurutkan dengan Quick Sort:")
print(my_list)