#matrix chain multiplication using dynamic programming
'''
You have been given a chain of matrices, and you need to find out “what is the minimum number of scalar multiplications needed to multiply these matrices?”. 
It is to be noted that since matrix multiplication is associative, so the order in which we are multiplying the matrices will determine the number of multiplications needed. 
'''
import math
def matrix_chain_multiplication ( dimensions : list [ int ]) -> tuple [int , list [tuple [int , int ]]]:
    
        
    n = len( dimensions ) - 1 # Number of matrices
    dp = [[0 for _ in range ( n + 1) ] for _ in range ( n + 1) ]
    S = [[0 for _ in range ( n + 1) ] for _ in range ( n + 1) ]
    ## YOUR CODE GOES HERE

    for d in range(1,n+1):
        for i in range(1,n-d+1):
            j=i+d
            m=[-1,-1]
            for k in range(i,j):
                cost=dp[i][k]+dp[k+1][j]+dimensions[i-1]*dimensions[k]*dimensions[j]
                if m[0]==-1 or cost<m[0]:
                    m[0]=cost
                    m[1]=k
            dp[i][j]=m[0]
            S[i][j]=m[1]

    print("no. of computation: ",dp[1][n])
## Print the minimum number of multiplications involved .

    split=[]

    def mul_matrices(i,j):
        if i==j:
            return
        k=S[i][j]
        split.append((i,j))
        mul_matrices(i,k)
        mul_matrices(k+1,j)

    mul_matrices(1,n)

    return (dp[1][n],split)


dimensions = [30, 35, 15, 5, 10, 20, 25]
max_cost, split_list = matrix_chain_multiplication(dimensions)
print("Max number of multiplications:", max_cost)
print("Split positions (i, j):", split_list)
