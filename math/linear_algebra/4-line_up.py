#!/usr/bin/env python3
"""Adds arrays element-wise."""


def add_arrays(arr1, arr2):
    """Returns the element-wise sum of equally sized arrays."""
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
