#!/usr/bin/env python3
"""Calculates the adjugate matrix of a square matrix."""


def determinant(matrix):
    """Calculates the determinant of a matrix."""
    if matrix == [] or matrix == [[]]:
        return 1

    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if not all(len(matrix) == len(row) for row in matrix):
        raise ValueError("matrix must be a square matrix")

    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    size = len(matrix)
    answer = 0
    for j in range(size):
        sign = (-1) ** j
        sub_matrix = [row[:j] + row[j + 1:] for row in matrix[1:]]
        answer += sign * matrix[0][j] * determinant(sub_matrix)
    return answer


def minor(matrix):
    """Calculates the minor matrix of a square matrix."""
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if not matrix or not all(len(matrix) == len(row) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    size = len(matrix)
    if size == 1:
        return [[1]]

    minor_matrix = []
    for i in range(size):
        minor_row = []
        for j in range(size):
            sub_matrix = [row[:j] + row[j + 1:]
                          for row in matrix[:i] + matrix[i + 1:]]
            minor_row.append(determinant(sub_matrix))
        minor_matrix.append(minor_row)
    return minor_matrix


def cofactor(matrix):
    """Calculates the cofactor matrix of a square matrix."""
    minor_matrix = minor(matrix)
    size = len(minor_matrix)
    return [[(-1) ** (i + j) * minor_matrix[i][j]
             for j in range(size)] for i in range(size)]


def adjugate(matrix):
    """Calculates the adjugate matrix of a square matrix."""
    cofactor_matrix = cofactor(matrix)
    return [list(row) for row in zip(*cofactor_matrix)]
