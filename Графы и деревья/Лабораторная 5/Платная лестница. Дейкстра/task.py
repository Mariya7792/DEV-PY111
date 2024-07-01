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
    predecessor = {node: None for node in graph.nodes}
    predecessor, costs = nx.dijkstra_predecessor_and_distance(graph, 0)
    for node in graph.nodes:
        if node not in costs:
            costs[node] = float('inf')
    return list(costs.values())[-1]
def form_stairway_graph(stairway_cost):
    graph = nx.DiGraph()
    graph.add_nodes_from(list(range(0, len(stairway_cost) + 1)))
    edges = []
    nodes = graph.nodes()
    for i in nodes:
        if i + 2 in nodes:
            edges += (i, i + 1, stairway_cost[i]), (i, i + 2, stairway_cost[i + 1])
        elif i + 1 in nodes:
            edges.append((i, i + 1, stairway_cost[i]))
    graph.add_weighted_edges_from(edges)
    return graph
if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = form_stairway_graph(stairway)
   # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней
    print(stairway_path(stairway_graph))  # 72
