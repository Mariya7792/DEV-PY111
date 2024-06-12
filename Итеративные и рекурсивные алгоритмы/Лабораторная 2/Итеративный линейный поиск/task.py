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
    min_value = 0
    if arr:
        for index in range(len(arr)):
            if arr[index] < arr[min_value]:
                min_value = index
        return min_value
    raise ValueError

     # TODO реализовать итеративный линейный поиск