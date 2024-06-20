from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    lenght = len(container)
    for index1 in range(lenght - 1):
        for index2 in range(index1 + 1, lenght):
            if container[index1] > container[index2]:
                container[index2], container[index1] = container[index1], container[index2]
    return container

print(sort([4,1,6,5]))

"""
 Сортировка пузырьком

   1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
   2. Если элементы не находятся в нужном порядке, меняйте их местами.
   3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
   4. Повторяйте шаги 1-3, пока не отсортируете весь массив.
 :param container: Массив, который надо отсортировать
:return: Отсортированный в порядке возрастания массив
"""
#     # TODO реализовать алгоритм сортировки пузырьком
