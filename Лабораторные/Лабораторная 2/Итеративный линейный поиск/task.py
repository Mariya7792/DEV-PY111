"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    ...  # TODO реализовать итеративный линейный поиск
    min_ = arr[0]
    for index in range(len(arr)):
        if arr[index] < min_:
            min_ = arr[index]
    return arr.index(min_)

print(min_search([12, 1, 7, 3]))

