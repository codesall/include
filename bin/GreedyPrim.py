import heapq
from collections import defaultdict

def prim_mst(graph, start):
    mst = []  # List to store the edges in the MST
    visited = set([start])  # Start with the starting vertex
    edges = []

    # Add all edges from the start node to the priority queue
    for to, weight in graph[start]:
        heapq.heappush(edges, (weight, start, to))

    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))

            # Add all edges from the new node
            for next_to, next_weight in graph[to]:
                if next_to not in visited:
                    heapq.heappush(edges, (next_weight, to, next_to))

    return mst

# Example undirected, weighted graph as adjacency list
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4), ('E', 5)],
    'D': [('B', 1), ('C', 4), ('E', 1)],
    'E': [('C', 5), ('D', 1)]
}

# Run Prim's algorithm
mst_result = prim_mst(graph, 'A')

# Output
print("Edges in the Minimum Spanning Tree using Greedy Prim's Algorithm:")
for frm, to, weight in mst_result:
    print(f"{frm} - {to}: {weight}")
