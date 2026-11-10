#!/usr/bin/env python3
"""Transposes two-dimensional matrices."""


def matrix_transpose(matrix):
    """Returns a new transposed matrix."""
    return [[matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]))]
