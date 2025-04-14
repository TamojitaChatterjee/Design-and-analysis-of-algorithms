#strassen's --> matrix chain

import numpy as np
def strassen_matrix_multiply(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    '''
    multiplies two square matrices using strassen's algorithm
    assumes that dimensions of A and B are n x n, where n is a power of 2
    '''
    
    n=A.shape[0]
    
    #base case: for a 1x1 matrix
    if n==1:
        return A*B
    
    #divide A and B into 4 submatrices each
    mid = n//2
    A11 = A[:mid, :mid] #submatrix top left
    A12 = A[:mid, mid:] #submatrix top right
    A21 = A[mid:, :mid] #submatrix bottom left
    A22 = A[mid:, mid:] #submatrix bottom right

    B11 = B[:mid, :mid] #submatrix top left
    B12 = B[:mid, mid:] #submatrix top right
    B21 = B[mid:, :mid] #submatrix bottom left
    B22 = B[mid:, mid:] #submatrix bottom right
    
    #Strassen's 7 products
    P = strassen_matrix_multiply(A11+A22, B11+B22)
    Q = strassen_matrix_multiply(A21+A22, B11)
    R = strassen_matrix_multiply(A11, B12-B22)
    S = strassen_matrix_multiply(A22, B21-B11)
    T = strassen_matrix_multiply(A11+A12, B22)
    U = strassen_matrix_multiply(A21-A11, B11+B12)
    V = strassen_matrix_multiply(A12-A22, B21+B22)
    
    #combine the products to form the elemets of C
    C11 = P+S-T+V
    C12 = R+T
    C21 = Q+S
    C22 = P+R-Q+U
    
    #combine the submatrices to form the final matrix
    top = np.hstack((C11, C12)) #Joins matrices horizontally
    bottom = np.hstack((C21, C22)) #Joins matrices horizontally
    C = np.vstack((top, bottom)) #Joins matrices vertically
    
    return C