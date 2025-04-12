def LCS(X, Y):
    # Length of strings
    m = len(X)
    n = len(Y)
    
    # Declaring an array to store the table values
    L = [[0] * (n + 1) for i in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
                
    return L[m][n]

# Driver code to test
X = "ABCDEFG"
Y = "ABCDGHMMOSH"
print(LCS(X, Y))  # Output: 6