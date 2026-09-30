import numpy as np
np.set_printoptions(precision=3, suppress=True, linewidth=200)

'''
the input into the simplex function is A,b,c where
 c = [40, 30, 50] ----> obj function coeff
 A = [
        [2,1,3]
        [1,2,1]
        [3,2,2]
        ] --------> constraint matrix coeff

b = [100, 80, 120] ----> RHS terms 

'''



def create_tableau(A,b,c):
    '''
    This function takes the coeff of the objective vector, 
    coeff of the constraints matrix, and coeff of the RHS vector
    to create the tableau 
    '''
    # create z column 
    z = np.zeros((A.shape[0], 1))  # (3,1)
    z = np.insert(z, 0, 1, axis=0) # (4,1)
    
    
    # create constraint and objective row matrix
    vertical = np.concatenate((c, A), axis=0)
    
    # concatenate z and constraint/obj matrix
    vertical = np.concatenate((z, vertical), axis=1)

    # create slack variable matrix
    slack = np.eye(A.shape[0])
    zeros = np.zeros((1, A.shape[0]))
    slack = np.concatenate((zeros, slack), axis = 0)

    # concatenate matrix to tableau
    horizontal = np.concatenate((vertical, slack), axis=1)

    # add RHS to tableau 
    b = np.insert(b,0,0, axis=1)
    b = b.T

    tableau = np.concatenate((horizontal, b), axis=1)

    return tableau


c = np.array([[40, 30, 50]])
A = np.array([
    [2,1,3],
    [1,2,1],
    [3,2,2]
    ])

b = np.array([[100, 80, 120]])
tableau = create_tableau(A,b,c)
print(tableau)

def choose_entering_var(tableau):
    '''
    This function finds the largest positive value 
    (with the assumption there is one) from the objective row 
    and defines that as the pivot column'''
    
    #choose the column with the largest positive value
    obj_row = tableau[0]
    enter_var_index = np.argmax(obj_row)
    return enter_var_index

enter_var_index = choose_entering_var(tableau)
print(enter_var_index)

def choose_leaving_var(tableau, enter_var_index):
    '''
    This function takes the pivot column, and divides it by the rhs 
    to get the min ratio value whose index is the pivot row'''

    #find the entering variable column constraint coeff
    enter_var_column = tableau[1:, enter_var_index]

    #find the rhs values
    rhs = tableau[1:,-1]

    # compute the min ratio for each
    min_ratio_vector= rhs / enter_var_column

    # take the index of the smallest min ratio (add one to keep it consistent with the tableau indexing)
    leave_var_index = np.argmin(min_ratio_vector) + 1

    return leave_var_index
    

leaving_var_index = choose_leaving_var(tableau, enter_var_index)
print(leaving_var_index)



def pivot(tableau, enter_index, leave_index):
    '''
    This function uses the pivot indicies to pivot the tableau.
    It does this by normalizing the pivot row, then updating the 
    other pivot column cells to = 0'''
    
    #take the enter & leave row and column indicies, normalize pivot row 
    pivot_cell = tableau[leave_index, enter_index]
    tableau[leave_index, :] = tableau[leave_index, :] / pivot_cell # normalize pivot row
    print(tableau)


pivot(tableau, enter_var_index, leaving_var_index )

# def is_optimal():





# def extract_solution():






# def simplex():



