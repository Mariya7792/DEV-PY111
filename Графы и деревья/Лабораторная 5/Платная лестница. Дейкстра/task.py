from typing import Union

import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    ...  # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы
    starting_node = 0
    predecessor, costs = nx.dijkstra_predecessor_and_distance(graph, starting_node)
    for node in graph.nodes:
        if node not in costs:
            costs[node] = float('inf')
    return predecessor, costs

if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = nx.Graph() # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней
    # print(stairway_path(stairway_graph))  # 72
