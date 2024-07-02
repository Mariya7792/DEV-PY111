"""
Навигатор на сетке.
Дана плоская квадратная двумерная сетка (массив), на которой определена стоимость
захода в каждую ячейку (все стоимости положительные). Необходимо найти путь
минимальной стоимости из заданной ячейки в заданную ячейку и вывести этот путь.
Можно двигаться наверх, вниз или по диагонали
"""
def costs(first_cell, last_cell, table_cost):
    n = len(table_cost)
    m = n
    table = [[0] * m for i in range(n)]

    for index in range(1, len(table[0])):
        table_cost[0][index] = table_cost[0][index - 1] + table[0][index]

    for index in range(1, len(table)):
        table_cost[index][0] = table_cost[index - 1][0] + table[index][0]

    for i in range(1, n):
        for j in range(1, n):
            table_cost[i][j] = min(table_cost[i - 1][j], table_cost[i][j - 1]) + table[i][j]
    return table_cost
if __name__ == '__main__':
    costs_ = [
        [2, 7, 9],
        [12, 4, 1],
        [1, 5, 2]
    ]
    total_coasts = costs(costs_)
    print(total_coasts)
