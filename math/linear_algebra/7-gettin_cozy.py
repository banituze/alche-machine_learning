#!/usr/bin/env python3
"""Concatenates two-dimensional matrices."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Returns matrices concatenated along the specified axis."""
    if axis == 0 and len(mat1[0]) == len(mat2[0]):
        return [row[:] for row in mat1 + mat2]
    if axis == 1 and len(mat1) == len(mat2):
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    return None
