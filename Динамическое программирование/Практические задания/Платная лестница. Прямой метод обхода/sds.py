a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
edges = []
for n in range(0, len(a) - 1):
    print(n)
    edges.append(((n), (n + 1)))
print(edges)
# [0, 1, 5][1, 2, 11][0, 2, 11][3, ]
# for n, m in enumerate(range(0, len(a) - 1)):
#     edges.append((n + 1, stairway[m]))
# print(edges)
# for n, m in enumerate(range(0, len(a) - 1)):
#     edges.append((n, n + 1, stairway[m]))
# print(edges)
