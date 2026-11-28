#!/usr/bin/env python3
"""Calculates the integral of a polynomial."""


def poly_integral(poly, C=0):
    """Returns the coefficients of a polynomial's integral."""
    if not isinstance(poly, list) or not poly or not isinstance(C, int):
        return None
    for coefficient in poly:
        if type(coefficient) not in (int, float):
            return None
    integral = [C]
    for power, coefficient in enumerate(poly):
        divisor = power + 1
        if coefficient % divisor == 0:
            integral.append(coefficient // divisor)
        else:
            integral.append(coefficient / divisor)
    while integral[-1] == 0 and len(integral) > 1:
        integral.pop()
    return integral
