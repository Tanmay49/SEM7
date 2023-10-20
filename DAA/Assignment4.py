def is_valid(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    
    def backtrack(row):
        if row == n:
            solutions.append(["".join(["Q" if c == 1 else "." for c in row]) for row in board])
            return
        
        for col in range(n):
            if is_valid(board, row, col):
                board[row][col] = 1  
                backtrack(row + 1)   
                board[row][col] = 0  
                
    solutions = []
    backtrack(0)      
    return solutions

n = 5
solutions = solve_n_queens(n)
for solution in solutions:
    print(len(solutions))
    print(solution)
