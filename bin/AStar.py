import heapq

# Define the grid (0 = walkable, 1 = obstacle)
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  # Starting position
end = (4, 4)    # Goal position

# Heuristic function: Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Search
def a_star(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, end), 0, start))  # (f, g, position)

    came_from = {}  # For path reconstruction
    g_score = {start: 0}

    while open_set:
        _, g, current = heapq.heappop(open_set)

        if current == end:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue  # Obstacle

                tentative_g_score = g + 1  # Cost to move is 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score, tentative_g_score, neighbor))
                    came_from[neighbor] = current

    return None  # No path found

# Run A*
path = a_star(grid, start, end)

# Output
if path:
    print("Path found by A*:")
    for step in path:
        print(step)
else:
    print("No path found.")
