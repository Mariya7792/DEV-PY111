from typing import List
"""
Оценить асимптотическую сложность приведенного ниже алгоритма:
a = len(arr) - 1  O(1)
out = list() O(1)
while a > 0: O(n)
out.append(arr[a]) O(1)
a = a // 1.7 O(1) 
out.merge_sort() O(n * log(n))
Сложность: O(n * log(n))
"""

def merge(left:list, right:list) -> list:
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
def merge_sort(container: List[int]) -> List[int]:
    if len(container) <= 1:
        return container
    middle = len(container) // 2
    left = merge_sort(container[:middle])
    right = merge_sort(container[middle:])
    return merge(left, right)

def algorithm(arr):
    a = len(arr) - 1
    out = list()
    while a > 0:
        out.append(arr[a])
        a = round(a // 1.7)
    sorted_out = merge_sort(out)
    return sorted_out
print(algorithm([1,2,3]))
