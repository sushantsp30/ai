print("\nprims algorithm\n")
import heapq
from collections import defaultdict

def prim(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start, None)]  # (cost, node, parent)

    while min_heap:
        cost, u, parent = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        if parent is not None:
            mst.append((parent, u, cost))
        for v, weight in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (weight, v, u))

    return mst

# Example usage:
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

mst = prim(graph, 'A')
print("Edges in the Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u} - {v} : {w}")
