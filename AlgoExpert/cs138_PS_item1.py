def gaussian_elimination(A, B):
    n, m = len(A), len(A[0])
    
    # Augment A with B to form the augmented matrix [A | B]
    augmented_matrix = [A[i] + [B[i]] for i in range(n)]
    
    # Perform Gaussian elimination to transform matrix into row echelon form
    for i in range(min(n, m)):  # Loop over the smaller dimension (rows or columns)
        # Find the pivot row
        pivot_row = i
        for j in range(i + 1, n):
            if abs(augmented_matrix[j][i]) > abs(augmented_matrix[pivot_row][i]):
                pivot_row = j

        # Swap the current row with the pivot row
        augmented_matrix[i], augmented_matrix[pivot_row] = augmented_matrix[pivot_row], augmented_matrix[i]
        
        # If the pivot element is 0, skip this column
        if augmented_matrix[i][i] == 0:
            continue

        # Eliminate the entries below the pivot
        for j in range(i + 1, n):
            if augmented_matrix[j][i] != 0:
                factor = augmented_matrix[j][i] / augmented_matrix[i][i]
                for k in range(i, m + 1):
                    augmented_matrix[j][k] -= factor * augmented_matrix[i][k]
    print(augmented_matrix)
    # Back substitution to solve for the variables
    x = [0] * m  # Initialize the solution vector

    # Solve for the variables, starting from the last row
    for i in range(min(n, m) - 1, -1, -1):
        sum_ax = 0
        for j in range(i + 1, m):
            sum_ax += augmented_matrix[i][j] * x[j]
        if augmented_matrix[i][i] != 0:
            x[i] = (augmented_matrix[i][m] - sum_ax) / augmented_matrix[i][i]
        else:
            # If no solution for this variable, continue (for underdetermined cases)
            x[i] = 0
    
    return x

# Example usage:
A = [
    [1, -2, -1, 3],
    [2, -4, 1, 0],
    [1, -2, 2, -3]
]

B = [1,5,4]

# Solve the system Ax = B
solution = gaussian_elimination(A, B)
print("Solution:", solution)
