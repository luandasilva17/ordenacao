# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

# Exemplo de uso para Quick Sort
arr_quick_sort = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr_quick_sort = quick_sort(arr_quick_sort)
print("Quick Sort:")
print("Array original:", arr_quick_sort)
print("Array ordenado:", sorted_arr_quick_sort)
print()

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Exemplo de uso para Merge Sort
arr_merge_sort = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr_merge_sort = merge_sort(arr_merge_sort)
print("Merge Sort:")
print("Array original:", arr_merge_sort)
print("Array ordenado:", sorted_arr_merge_sort)
print()

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Exemplo de uso para Bubble Sort
arr_bubble_sort = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
bubble_sort(arr_bubble_sort)
print("Bubble Sort:")
print("Array original:", arr_bubble_sort)
print("Array ordenado:", arr_bubble_sort)
