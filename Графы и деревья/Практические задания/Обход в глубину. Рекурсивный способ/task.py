from typing import Hashable, List
import networkx as nx
from collections import deque


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Функция выполняет обход в глубину и возвращает список узлов в порядке посещения.
    В данной задаче порядок обхода графа левосторонний или правосторонний не важен,
    главное соблюсти порядок обхода в ширину.

    :param g: Граф NetworkX, по которому нужно совершить обход
    :param start_node: Стартовый узел, откуда нужно начать обход
    :return: Список узлов в порядке посещения.
    """
    ...  # TODO реализовать обход в глубину
    visited = {node: False for node in g.nodes}
    # d = deque()
    path = []

    def rec_dfs(current_node):
        visited[current_node] = True
        path.append(current_node)

    # d.append(start_node)
    # visited[start_node] = True

    # while d:
    #     current_node = d.pop()
    #     path.append(current_node)

        for neighbor in g.neighbors(current_node):
            if not visited[neighbor]:
                rec_dfs(neighbor)
                # d.append(neighbor)
                # visited[neighbor] = True
    rec_dfs(start_node)
    return path


if __name__ == '__main__':
    # TODO записать граф с помощью модуля networkx и прверить обход в ширину
    graph = nx.Graph()
    graph.add_nodes_from('ABCDEGGHIJ')
    graph.add_edges_from([('A', 'B'),
                          ('A', 'C'),
                          ('B', 'D'),
                          ('B', 'E'),
                          ('E', 'G'),
                          ('C', 'F')
                          ])
    print(dfs(graph, 'A'))
    # nx.draw(graph, with_labels=True)
    # plt.show()
