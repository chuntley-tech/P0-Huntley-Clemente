"""Benchmark de mimatmul comparando tamaños de matriz."""

from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mimatmul import mimatmul

A2 = [[1, 2], [3, 4]]
B2 = [[5, 6], [7, 8]]

A10 = [[i * 10 + j + 1 for j in range(10)] for i in range(10)]
B10 = [[(i + j) % 7 + 1 for j in range(10)] for i in range(10)]


def medir(f, repeticiones: int) -> float:
    """Devuelve el tiempo por llamada en microsegundos."""
    inicio = time.perf_counter()
    for _ in range(repeticiones):
        f()
    total = time.perf_counter() - inicio
    return total / repeticiones * 1e6


def main() -> int:
    t2 = medir(lambda: mimatmul(A2, B2), 100_000)
    t10 = medir(lambda: mimatmul(A10, B10), 1_000)
    print(f"2x2  : {t2:8.2f} us por llamada")
    print(f"10x10: {t10:8.2f} us por llamada")
    print(f"La 10x10 es {t10 / t2:.1f}x más lenta que la 2x2")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
