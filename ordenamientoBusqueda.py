from funciones import *

# Ejemplo de uso:
arr = [64, 25, 12, 22, 11]
bubble_sort(arr)
print("Bubble Sort:", arr)

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Selection Sort:", arr)

arr = [64, 25, 12, 22, 11]
insertion_sort(arr)
print("Insertion Sort:", arr)

arr = [64, 25, 12, 22, 11]
merge_sort(arr)
print("Merge Sort:", arr)

arr = [64, 25, 12, 22, 11]
linear_search_result = linear_search(arr, 12)
print("Linear Search for 12:", linear_search_result)

sorted_arr = [11, 12, 22, 25, 64]
binary_search_result = binary_search(sorted_arr, 12)
print("Binary Search for 12:", binary_search_result)