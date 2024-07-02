"""
Дано: массив из 10**6 целых чисел, каждый из которыз лежит на отрезке [13, 25]
Задача: отсортировать массив наиболее эффективным способом
Ответ: лучше всего сортировка подсчетом, так как здесь массив с большим количеством повторяющихся элементов
"""
import random
from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    if not container:
        return container

    min_val = min(container)
    max_val = max(container)
    data = {key: [] for key in range(min_val, max_val+1)}

    sorted_result = []
    for value in container:
        data[value].append(value)

    for value in data.values():
        if value:
            sorted_result.extend(value)

    return sorted_result
container = [random.randint(13, 25) for i in range(10**6)]

print(sort(container))

