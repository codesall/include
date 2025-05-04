# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# Set to keep track of visited nodes
visited = set()

def dfs_recursive(node):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(neighbor)

# Call DFS starting from vertex 'A'
print("Depth First Search traversal (recursive):")
dfs_recursive('A')
