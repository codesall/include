def is_safe(row, col, board, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
    
    # Check diagonal (/)
    for i in range(row):
        if board[i] - i == col - row:
            return False
    
    # Check diagonal (\)
    for i in range(row):
        if board[i] + i == col + row:
            return False

    return True

def solve_n_queens_util(row, board, n, solutions):
    if row == n:
        # Found a valid configuration
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(row, col, board, n):
            board[row] = col  # Place queen
            solve_n_queens_util(row + 1, board, n, solutions)
            # Backtrack happens automatically on function return

def solve_n_queens(n):
    board = [-1] * n  # board[i] = column of queen in row i
    solutions = []
    solve_n_queens_util(0, board, n, solutions)
    return solutions

# Pretty print the solutions
def print_solutions(solutions, n):
    for idx, solution in enumerate(solutions, 1):
        print(f"\nSolution {idx}:")
        for row in range(n):
            line = ['.'] * n
            line[solution[row]] = 'Q'
            print(' '.join(line))

# Example usage
n = 4
solutions = solve_n_queens(n)
print(f"Total solutions for {n}-Queens: {len(solutions)}")
print_solutions(solutions, n)
