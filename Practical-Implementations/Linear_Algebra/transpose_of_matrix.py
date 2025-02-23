# So transform of A (any matrix) is a matrix which is obtained by changing rows to columns and columns to rows , and that's what we doing here .
# Like : 3x4 matrix becomes 4x3 matrix after Transpose.
# Example :
"""  
| 1 2 3 |
| 4 5 6 | => | 1 4 |
             | 2 5 |
             | 3 6 |


"""
def transpose_matrix(matrix):
    """
    Transpose a given matrix by swapping rows with columns.

    Args:
    matrix (list of list of int): The matrix to be transposed.

    Returns:
    list of list of int: The transposed matrix.
    """
    # Number of rows and columns
    rows = len(matrix)
    cols = len(matrix[0])

    # Create an empty matrix with transposed dimensions , here we interchanging rows and columns
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Iterate through rows and columns to transpose the matrix
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed

# Example usage
matrix = [[1, 2, 3], [4, 5, 6]]
transposed_matrix = transpose_matrix(matrix)
print('Returned matrix:\n',transposed_matrix)

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)


# Example with numpy 
import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]])
transposed_matrix = matrix.T

print("Original Matrix:")
print(matrix)

print("\nTransposed Matrix:")
print(transposed_matrix)
