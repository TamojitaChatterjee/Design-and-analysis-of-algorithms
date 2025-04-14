#simplex method --> LPP
import numpy as np
def simplex_method(tableau: np.ndarray) -> tuple[float,dict[str, float]]:
    '''
    Solves a maximization lpp
    input as initial simplex tableau
    args:
        tableau: numpy array representing initial simplex tableau
    returns:
        a tuple containing:
            - optimal value of objective function (float)
            - dictionary mapping basic variable names to their values (float)
    '''
    num_rows, num_cols = tableau.shape
    
    while True:
        #find pivot column (most negative value in last row)
        last_row = tableau[-1, :-1]
        pivot_col = np.argmin(last_row)
        
        #check if all values in last row are non-negative
        if last_row[pivot_col] >= 0:
            break
        
        #find pivot row using minimum ratio test
        column = tableau[:-1, pivot_col]
        rhs = tableau[:-1, -1]
        ratios = []
        
        for i in range(len(column)):
            if column[i] > 0:
                ratios.append(rhs[i] / column[i])
            else:
                ratios.append(np.inf)
                
        pivot_row = np.argmin(ratios)
        
        #perform pivot operation (make pivot element 1 and rest all 0)
        pivot_element = tableau[pivot_row, pivot_col]
        tableau[pivot_row] = tableau[pivot_row] / pivot_element
        
        for i in range(num_rows):
            if i != pivot_row:
                tableau[i] -= tableau[pivot_row] * tableau[i, pivot_col]
                
    #extract result
    optimal_value = tableau[-1, -1]
    variable_values = {}
    
    for j in range(num_cols - 1):
        column = tableau[:-1, j]
        ones = list(column).count(1)
        zeros = list(column).count(0)
        
        if ones == 1 and zeros == len(column) - 1:
            row_index = list(column).index(1)
            value = tableau[row_index][-1]
        else:
            value = 0.0
            
        variable_name = "x"+str(j+1)
        variable_values[variable_name] = value
        
    return optimal_value, variable_values