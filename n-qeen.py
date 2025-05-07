from collections import defaultdict
def solve_n_queens_branch_and_bound(n):
    def backtrack(row):
        if row == n:
            board = [''.join(r) for r in current_board]
            solutions.append(board)
            return
        for col in range(n):
            if not cols[col] and not diag1[row - col] and not diag2[row + col]:
                # Place queen
                current_board[row][col] = 'Q'
                cols[col] = diag1[row - col] = diag2[row + col] = True

                backtrack(row + 1)

                # Remove queen (backtrack)
                current_board[row][col] = '.'
                cols[col] = diag1[row - col] = diag2[row + col] = False

    solutions = []
    current_board = [['.'] * n for _ in range(n)]
    cols = [False] * n
    diag1 = defaultdict(bool)  # row - col
    diag2 = defaultdict(bool)  # row + col

    backtrack(0)
    return solutions

print("give no. of queens\n")
n = int(input())

solutions = solve_n_queens_branch_and_bound(n)

print(f"{len(solutions)} solutions for {n}-Queens using Branch and Bound:\n")
for sol in solutions:
    for row in sol:
        print(row)
    print()
    
