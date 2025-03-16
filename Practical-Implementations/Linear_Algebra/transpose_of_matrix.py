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
print('tansposed matrix using numpy',transposed_matrix)


# We also have another way to transpose matrix, numpy.transpose()
""" With the help of Numpy numpy.transpose(), We can perform the simple function of transpose within one line by using numpy.transpose() method of Numpy. It can transpose the 2-D arrays on the other hand it has no effect on 1-D arrays. This method transpose the 2-D numpy array. """

# Parameters: 
"""
axes :tuple or list of ints, optional
If specified, it must be a tuple or list or int which contains a permutation of [0, 1, …, N-1] where N is the number of axes of a. Negative indices can also
be used to specify axes. The i-th axis of the returned array will correspond to the axis numbered axes[i] of the input. If not specified, 
defaults to [axis for axis in range(a.ndim)][::-1], which reverses the order of the axes.

Returns: ndarray 
a matrix with its axes permuted. A view is returned whenever possible.
"""

gfg = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
 
# before transpose
print('\n before transpose\n',gfg, end ='\n\n')

""" after transpose, we give(optionally,because by default it is also(1,0)) (1,0) coz it means 3 rows and 2 columns as 
1 pointing to axis of untransposed matrix columns and 0 pointing to axis row of untransposed matrix rows """
print('\n after transpose\n',gfg.transpose(1, 0), end ='\n\n')