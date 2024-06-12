from collections import deque
def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    list_brackets = []
     # TODO реализовать проверку скобочной группы
    try:
        for element in brackets_row:
            if element == "(":
                list_brackets.append(element)
            elif element == ")":
                list_brackets.pop()
        if list_brackets:
            return False
        return True
    except IndexError:
        return False

if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
