# ==========================================
# Q1: Matrix Multiplication
# Traditional vs Strassen's Algorithm
# ==========================================

import random
import time


# ==========================================
# Traditional Matrix Multiplication
# ==========================================

def traditional_matrix_multiply(A, B):
    n = len(A)

    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


# ==========================================
# Matrix Addition
# ==========================================

def add_matrix(A, B):
    n = len(A)

    return [
        [A[i][j] + B[i][j] for j in range(n)]
        for i in range(n)
    ]


# ==========================================
# Matrix Subtraction
# ==========================================

def subtract_matrix(A, B):
    n = len(A)

    return [
        [A[i][j] - B[i][j] for j in range(n)]
        for i in range(n)
    ]


# ==========================================
# Strassen's Matrix Multiplication
# ==========================================

def strassen_matrix_multiply(A, B):

    n = len(A)

    # Base case
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Divide point
    mid = n // 2

    # Divide A into four parts
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    # Divide B into four parts
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Seven Strassen multiplications

    M1 = strassen_matrix_multiply(
        add_matrix(A11, A22),
        add_matrix(B11, B22)
    )

    M2 = strassen_matrix_multiply(
        add_matrix(A21, A22),
        B11
    )

    M3 = strassen_matrix_multiply(
        A11,
        subtract_matrix(B12, B22)
    )

    M4 = strassen_matrix_multiply(
        A22,
        subtract_matrix(B21, B11)
    )

    M5 = strassen_matrix_multiply(
        add_matrix(A11, A12),
        B22
    )

    M6 = strassen_matrix_multiply(
        subtract_matrix(A21, A11),
        add_matrix(B11, B12)
    )

    M7 = strassen_matrix_multiply(
        subtract_matrix(A12, A22),
        add_matrix(B21, B22)
    )

    # Calculate result quadrants

    C11 = add_matrix(
        subtract_matrix(
            add_matrix(M1, M4),
            M5
        ),
        M7
    )

    C12 = add_matrix(M3, M5)

    C21 = add_matrix(M2, M4)

    C22 = add_matrix(
        subtract_matrix(
            add_matrix(M1, M3),
            M2
        ),
        M6
    )

    # Combine four quadrants

    C = []

    for i in range(mid):
        C.append(C11[i] + C12[i])

    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C


# ==========================================
# Generate Random Matrix
# ==========================================

def generate_matrix(n):

    return [
        [random.randint(1, 10) for _ in range(n)]
        for _ in range(n)
    ]


# ==========================================
# Test Matrix Sizes
# ==========================================

sizes = [2, 4, 8, 16, 32, 64, 128]


print()
print("==========================================")
print("Matrix Multiplication Performance")
print("==========================================")

print(f"{'Size':<10}{'Traditional':<20}{'Strassen':<20}{'Match'}")
print("-" * 60)


for n in sizes:

    # Generate matrices
    A = generate_matrix(n)
    B = generate_matrix(n)

    # -------------------------------
    # Traditional Method
    # -------------------------------

    start = time.perf_counter()

    traditional_result = traditional_matrix_multiply(A, B)

    traditional_time = time.perf_counter() - start

    # -------------------------------
    # Strassen Method
    # -------------------------------

    start = time.perf_counter()

    strassen_result = strassen_matrix_multiply(A, B)

    strassen_time = time.perf_counter() - start

    # -------------------------------
    # Compare Results
    # -------------------------------

    match = traditional_result == strassen_result

    # -------------------------------
    # Display
    # -------------------------------

    print(
        f"{n}x{n:<7}"
        f"{traditional_time:<20.6f}"
        f"{strassen_time:<20.6f}"
        f"{match}"
    )


# ==========================================
# Display 2x2 Example
# ==========================================

A = generate_matrix(2)
B = generate_matrix(2)

traditional_result = traditional_matrix_multiply(A, B)
strassen_result = strassen_matrix_multiply(A, B)


print()
print("==========================================")
print("2x2 Matrix Example")
print("==========================================")

print()
print("Matrix A:")

for row in A:
    print(row)


print()
print("Matrix B:")

for row in B:
    print(row)


print()
print("Traditional Result:")

for row in traditional_result:
    print(row)


print()
print("Strassen Result:")

for row in strassen_result:
    print(row)


print()
print("Results Match:", traditional_result == strassen_result)