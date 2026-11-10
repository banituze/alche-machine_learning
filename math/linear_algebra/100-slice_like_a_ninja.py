#!/usr/bin/env python3
"""Slices NumPy arrays along specified axes."""


def np_slice(matrix, axes={}):
    """Returns a sliced NumPy array along the requested axes."""
    slices = [slice(None)] * matrix.ndim
    for axis, indices in axes.items():
        slices[axis] = slice(*indices)
    return matrix[tuple(slices)].copy()
