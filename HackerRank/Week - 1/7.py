def diagonalDifference(arr):
    primary = 0
    secondary = 0
    n = len(arr)
    
    for i in range(n):
        primary += arr[i][i]
        secondary += arr[i][n - 1 - i]
    
    return abs(primary - secondary)

n = int(input().strip())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(diagonalDifference(matrix))
