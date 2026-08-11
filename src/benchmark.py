"""Benchmark de mimatmul contra numpy (A @ B) en varios tamaños."""

from __future__ import annotations

import csv
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mimatmul import mimatmul

TAMANOS = [8, 16, 32, 64]
REPETICIONES = 3
SEMILLA = 42
ARCHIVO_SALIDA = Path(__file__).resolve().parent.parent / "data" / "benchmark_results.csv"


def generar_matrices(n: int) -> tuple[np.ndarray, np.ndarray]:
    """Genera dos matrices float64 de n×n deterministas."""
    rng = np.random.default_rng(SEMILLA)
    return rng.random((n, n)), rng.random((n, n))


def medir(funcion, repeticiones: int) -> list[float]:
    """Devuelve el tiempo por llamada en segundos de cada repetición."""
    tiempos: list[float] = []
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        funcion()
        tiempos.append(time.perf_counter() - inicio)
    return tiempos


def main() -> int:
    resultados: dict[str, dict] = {}

    print(f"{'Tamaño':>8} {'Método':>9} {'Repeticiones (µs)':>28} {'Media (µs)':>12} {'Ratio':>8}")
    print("-" * 70)

    for n in TAMANOS:
        a, b = generar_matrices(n)
        mimatmul_np = lambda: mimatmul(a.tolist(), b.tolist())  # noqa: E731
        numpy_matmul = lambda: a @ b  # noqa: E731

        medir(mimatmul_np, 1)
        medir(numpy_matmul, 1)

        tiempos_mi = medir(mimatmul_np, REPETICIONES)
        tiempos_np = medir(numpy_matmul, REPETICIONES)
        resultados[str(n)] = {"mimatmul": tiempos_mi, "numpy": tiempos_np}

        us_mi = [t * 1e6 for t in tiempos_mi]
        us_np = [t * 1e6 for t in tiempos_np]
        media_mi = sum(us_mi) / REPETICIONES
        media_np = sum(us_np) / REPETICIONES

        print(f"{n}x{n:>5} {'mimatmul':>9} {str([f'{t:.2f}' for t in us_mi]):>28} {media_mi:>10.2f} {media_mi / media_np:>7.1f}x")
        print(f"{n}x{n:>5} {'numpy':>9} {str([f'{t:.2f}' for t in us_np]):>28} {media_np:>10.2f} {'—':>8}")

    ARCHIVO_SALIDA.parent.mkdir(parents=True, exist_ok=True)
    with ARCHIVO_SALIDA.open("w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["método", "tamaño", "repetición", "tiempo (s)"])
        for n in TAMANOS:
            for repeticion, tiempo in enumerate(resultados[str(n)]["mimatmul"], start=1):
                writer.writerow(["mimatmul", f"{n}x{n}", repeticion, tiempo])
            for repeticion, tiempo in enumerate(resultados[str(n)]["numpy"], start=1):
                writer.writerow(["numpy", f"{n}x{n}", repeticion, tiempo])

    print(f"\nCada repetición guardada en: {ARCHIVO_SALIDA}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
