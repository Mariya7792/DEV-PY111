def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if n == 0:
        return 1
    elif n >= 1:
        return n * factorial_recursive(n - 1)
    raise ValueError
     # TODO реализовать рекурсивный алгоритм нахождения факториала
