"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        """
        self.queue = []

    def enqueue(self, elem: Any) -> None: # O(1)
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self.queue.append(elem)  # TODO реализовать метод enqueue
    def dequeue(self) -> Any: # O(n)
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if self.queue:
            return self.queue.pop(0)  # TODO реализовать метод dequeue
        raise IndexError

    def peek(self, ind: int = 0) -> Any: # O(1)
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if type(ind) is not int:
            raise TypeError
        elif ind > len(self.queue) - 1:
            raise IndexError
        return self.queue[ind]
        # TODO реализовать метод peek

    def clear(self) -> None: # O(1)
        """ Очистка очереди. """
        return self.queue.clear()
        # TODO реализовать метод clear

    def __len__(self): # O(1)
        """ Количество элементов в очереди. """
        return len(self.queue)
        # TODO реализовать метод __len__

a = Queue()
a.queue = [1, 2, 3]
print(a.enqueue(4))