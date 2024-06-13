def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if n == 1 or n == 0:
        return 1
    elif n > 1:
        factorial_value = 1
        for i in range(1, n + 1):
            factorial_value *= i
        return factorial_value
    raise ValueError
    # TODO реализовать итеративный алгоритм нахождения факториала

print(factorial_iterative(3))
