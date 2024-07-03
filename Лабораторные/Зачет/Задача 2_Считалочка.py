"""
Считалочка
Дано N человек, считалка из K слогов.
Считалка начинает считать с первого человека.
Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает.
Игра происходит до тех пор, пока не останется последний человек.
Для данных N и К дать номер последнего оставшегося человека.
"""


def counting(N, K):
    list_people = [i for i in range(1, N + 1)]
    while len(list_people) > 0:
        if len(list_people) == 1:
            return list_people[0]
        else:
            lost = (len(list_people) + K - 1) % len(list_people)
            list_people.pop(lost)

print(counting(8, 5))
