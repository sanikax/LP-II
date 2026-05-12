n = int(input("Enter total number of queens: "))

board = [[0 for i in range(n)] for j in range(n)]

def is_safe(row, col):
     
    for i in range(col):
         if board[row][i] == 1:
             return False
    i = row
    j = col
    
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    i = row
    j = col
    
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
        
    return True
     
    
def solve(col):
    if col >= n:
        return True
    
    for row in range(n):
        if is_safe(row, col):
            board[row][col] = 1;
            
            if solve(col + 1):
                return True
                
            board[row][col] = 0
    
    return False
    
if solve(0):
    print("\n Solution Exists: \n")
    
    for i in range(n):
        for j in range(n):
            print(board[i][j], end = " ")
            
        print()

else:
    print("Solution doesn't Exist!!")