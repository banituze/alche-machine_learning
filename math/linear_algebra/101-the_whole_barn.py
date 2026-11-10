#!/usr/bin/env python3
"""Adds matrices with any number of dimensions."""


def matrix_shape(matrix):
    """Returns the dimensions of a nested matrix."""
    if not isinstance(matrix, list):
        return []
    return [len(matrix)] + matrix_shape(matrix[0])


def add_matrices(mat1, mat2):
    """Returns a new element-wise sum for equally shaped matrices."""
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    if isinstance(mat1, list):
        return [add_matrices(a, b) for a, b in zip(mat1, mat2)]
    return mat1 + mat2
