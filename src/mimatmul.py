"""Multiplicación de matrices implementada desde cero."""

from __future__ import annotations


def mimatmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    """Multiplica dos matrices A (m×n) y B (n×p) sin librerías externas."""
    if not A or not B or not A[0] or not B[0]:
        raise ValueError("Las matrices no pueden estar vacías")

    filas_a, columnas_a = len(A), len(A[0])
    filas_b, columnas_b = len(B), len(B[0])

    if columnas_a != filas_b:
        raise ValueError(
            f"Dimensiones incompatibles: A es {filas_a}x{columnas_a} y B es "
            f"{filas_b}x{columnas_b}"
        )

    resultado: list[list[float]] = [[0.0] * columnas_b for _ in range(filas_a)]

    for i in range(filas_a):
        for j in range(columnas_b):
            total = 0.0
            for k in range(columnas_a):
                total += A[i][k] * B[k][j]
            resultado[i][j] = total

    return resultado
