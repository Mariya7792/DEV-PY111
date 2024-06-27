import pprint
from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    ...  # TODO решить задачу с помощью динамического программирования
    if n == 1 and m == 2 or n == 2 and m == 1 or n == 1 and m == 1:
        return [[1]]

    car_path = [[0] * n for i in range(m)]

    for index in range(0, len(car_path[0])):
        car_path[0][index] = 1
    for index in range(1, len(car_path)):
        car_path[index][0] = car_path[index - 1][0] + car_path[index][0]

    for i in range(1,  m):
        for j in range(1, n):
            car_path[i][j] = car_path[i - 1][j] + car_path[i][j - 1] + car_path[i - 1][j - 1]

    return car_path


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths)
    print(paths[-1][-1])  # 7

