#!/usr/bin/env python3
"""Concatenates matrices with any number of dimensions."""


def matrix_shape(matrix):
    """Returns the dimensions of a nested matrix."""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape


def copy_matrix(matrix):
    """Returns an independent copy of a nested matrix."""
    if isinstance(matrix, list):
        return [copy_matrix(item) for item in matrix]
    return matrix


def concatenate(mat1, mat2, axis):
    """Returns a concatenation along the specified axis."""
    if axis == 0:
        return copy_matrix(mat1) + copy_matrix(mat2)
    return [concatenate(a, b, axis - 1)
            for a, b in zip(mat1, mat2)]


def cat_matrices(mat1, mat2, axis=0):
    """Returns concatenated matrices when their dimensions match."""
    shape1 = matrix_shape(mat1)
    shape2 = matrix_shape(mat2)
    if len(shape1) != len(shape2) or axis not in range(len(shape1)):
        return None
    for i in range(len(shape1)):
        if i != axis and shape1[i] != shape2[i]:
            return None
    return concatenate(mat1, mat2, axis)
