"""
EXP 03 - Matrix Multiplication using MapReduce (simulation in Python)
"""
from collections import defaultdict

# Input matrices (replace with your own)
matrix_A = [
    [1, 2],
    [3, 4]
]
matrix_B = [
    [5, 6],
    [7, 8]
]

rows_A, cols_A = len(matrix_A), len(matrix_A[0])
rows_B, cols_B = len(matrix_B), len(matrix_B[0])

if cols_A != rows_B:
    raise ValueError("Number of columns in matrix A must be equal to the number of rows in matrix B.")

# Prepare the input for MapReduce: "matrix,i,j,value"
input_data = [
    f"A,{i},{j},{value}" for i, row in enumerate(matrix_A) for j, value in enumerate(row)
] + [
    f"B,{i},{j},{value}" for i, row in enumerate(matrix_B) for j, value in enumerate(row)
]


def mapper(input_data):
    """Emit key = (i,k) of the result cell, value = (matrix, index, value)."""
    for line in input_data:
        matrix, i, j, value = line.strip().split(",")
        if matrix == "A":
            for k in range(cols_B):
                yield f"{i},{k},A,{j},{value}"        # A[i][j] contributes to C[i][k]
        else:
            for k in range(rows_A):
                yield f"{k},{j},B,{i},{value}"        # B[i][j] contributes to C[k][j]


def reducer(mapped_data):
    """Group by result cell (i,j), multiply matching A and B entries and sum."""
    groups = defaultdict(lambda: {"A": {}, "B": {}})
    for line in mapped_data:
        i, j, matrix_id, index, value = line.strip().split(",")
        groups[(int(i), int(j))][matrix_id][int(index)] = float(value)

    for (i, j), vals in sorted(groups.items()):
        total = sum(vals["A"][x] * vals["B"][x] for x in vals["A"] if x in vals["B"])
        yield f"{i},{j},{total}"


# Execute the MapReduce simulation
mapped_data = mapper(input_data)
reduced_data = reducer(mapped_data)
results = [line for line in reduced_data]

# Prepare the result matrix
result_matrix = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
for line in results:
    i, j, value = line.strip().split(",")
    result_matrix[int(i)][int(j)] = float(value)

# Print the result
for row in result_matrix:
    print(row)
