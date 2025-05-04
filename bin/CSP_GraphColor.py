def is_safe(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def graph_coloring_util(graph, colors, assignment, node_list, index):
    if index == len(node_list):
        return True

    node = node_list[index]
    for color in colors:
        if is_safe(node, color, assignment, graph):
            assignment[node] = color
            if graph_coloring_util(graph, colors, assignment, node_list, index + 1):
                return True
            # Backtrack
            del assignment[node]
    return False

def graph_coloring(graph, num_colors):
    colors = [f'C{i+1}' for i in range(num_colors)]
    assignment = {}
    node_list = list(graph.keys())

    if graph_coloring_util(graph, colors, assignment, node_list, 0):
        return assignment
    else:
        return None

# Example graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Number of colors
num_colors = 3

# Run the graph coloring
result = graph_coloring(graph, num_colors)

# Output the result
if result:
    print("Color assignment using CSP:")
    for node, color in result.items():
        print(f"{node}: {color}")
else:
    print("No valid coloring found.")
