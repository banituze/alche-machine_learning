#!/usr/bin/env python3
"""Transposes NumPy arrays."""


def np_transpose(matrix):
    """Returns a transposed NumPy array."""
    return matrix.transpose().copy()
