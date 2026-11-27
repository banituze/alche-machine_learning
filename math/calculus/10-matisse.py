#!/usr/bin/env python3
"""Calculates the derivative of a polynomial."""


def poly_derivative(poly):
    """Returns the coefficients of a polynomial's derivative."""
    if not isinstance(poly, list) or not poly:
        return None
    if len(poly) == 1:
        return [0]
    return [poly[i] * i for i in range(1, len(poly))]
