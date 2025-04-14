#n-queens
def solve_nqueens(n: int) ->list[list[int]]:
    '''
    Args:
        n: size of chessboard
    Returns:
        list of lists where each inner list represents a valid board configuration
    '''
    
    solutions=[]
    
    def is_safe(position, row, col):
        for r in range(row):
            c = position[r]
            if c == col or abs(c - col) == abs(r-row):
                return False
            return True
        
    def solve(row, position):
        if row == n:
            solutions.append(position[:])
            return
        for col in range(n):
            if is_safe(position, row, col):
                position.append(col)
                solve(row+1, position)
                position.pop() #backtrack
                
    solve(0, [])
    return solutions