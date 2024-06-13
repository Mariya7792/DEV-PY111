from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализовать алгоритм сортировки подсчетами
    if not container:
        return container
    min_val = min(container)
    max_val = max(container)
    data = {key: [] for key in range(min_val, max_val + 1)}
    sorted_result = []
    for value in container:
        data[value].append(value)

    for key, value in data.values():
        if value:
            sorted_result.extend(value)
    return sorted_result