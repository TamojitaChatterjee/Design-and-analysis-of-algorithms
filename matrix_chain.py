#matrix chain multiplication using dynamic programming
'''
You have been given a chain of matrices, and you need to find out “what is the minimum number of scalar multiplications needed to multiply these matrices?”. 
It is to be noted that since matrix multiplication is associative, so the order in which we are multiplying the matrices will determine the number of multiplications needed. 
'''
def matrix_chain_multiplication(dims):
    n = len(dims) - 1  # Number of matrices
    dp = [[0] * n for _ in range(n)]  # dp[i][j] stores min cost of multiplying matrix i to j

    for l in range(2, n + 1):  # l is chain length
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]
