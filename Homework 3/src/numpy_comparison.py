#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""numpy_comparison.py

Code for question 11 about numpy.  This script requires the numpy
dependency.

USAGE: ./numpy_comparison.py
"""

import time
from random import randint

import numpy as np


def dot_product(a, b):
    result = 0
    for a_i, b_i in zip(a, b):
        result += a_i * b_i
    return result

def matrix_multiply(matrix, vector):
    return [dot_product(row_vector, vector) for row_vector in matrix]

# Generate a 1000 element vector, and a 1000 x 1000 element matrix
vector = [randint(0, 10) for _ in range(1000)]
matrix = [[randint(0, 10) for _ in range(1000)] for _ in range(1000)]

# Create numpy arrays
np_vector = np.array(vector)
np_matrix = np.array(matrix)

# Multiply the matrix and vector (using our hand-coded implementation)
start = time.time()
matrix_multiply(matrix, vector)
end = time.time()

# Multiply the matrix and vector (using numpy)
np_start = time.time()
np_matrix.dot(np_vector)
np_end = time.time()

print(f"Hand-coded implementation took {end - start} seconds")
print(f"numpy took {np_end - np_start} seconds")
