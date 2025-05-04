from collections import deque

# Define the graph using an adjacency list
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

# Recursive BFS function
def bfs_recursive(queue):
    if not queue:
        return
    
    node = queue.popleft()
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    
    bfs_recursive(queue)

# Initialize queue with starting node
start_node = 'A'
print("Breadth First Search traversal (recursive using queue):")
bfs_recursive(deque([start_node]))
