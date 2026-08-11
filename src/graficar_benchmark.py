"""Genera el gráfico figures/benchmark.png a partir del CSV de resultados."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_ENTRADA = PROJECT_ROOT / "data" / "benchmark_results.csv"
FIGURA_SALIDA = PROJECT_ROOT / "figures" / "benchmark.png"


def formatear_tiempo(seg: float) -> str:
    """Formatea un tiempo en segundos a µs o ms según su magnitud."""
    if seg >= 1e-3:
        return f"{seg * 1e3:.1f} ms"
    return f"{seg * 1e6:.1f} µs"


def leer_resultados() -> dict[str, dict[str, list[float]]]:
    """Lee el CSV y agrupa tiempos por método y tamaño."""
    tiempos: dict[str, dict[str, list[float]]] = defaultdict(
        lambda: defaultdict(list)
    )
    with CSV_ENTRADA.open(encoding="utf-8") as archivo:
        for fila in csv.DictReader(archivo):
            metodo = fila["método"]
            tamano = int(fila["tamaño"].split("x")[0])
            tiempos[metodo][tamano].append(float(fila["tiempo (s)"]))
    return tiempos


def main() -> int:
    tiempos = leer_resultados()
    tamanos = sorted(next(iter(tiempos.values())))
    orden = [("mimatmul", "mimatmul (propio)"), ("numpy", "NumPy (A @ B)")]

    plt.figure(figsize=(8, 5))
    for metodo, etiqueta in orden:
        medias = [
            sum(tiempos[metodo][n]) / len(tiempos[metodo][n]) for n in tamanos
        ]
        plt.plot(tamanos, medias, marker="o", label=etiqueta)
        for n, media in zip(tamanos, medias):
            plt.annotate(
                formatear_tiempo(media),
                (n, media),
                textcoords="offset points",
                xytext=(0, 8),
                ha="center",
                fontsize=8,
            )

    plt.xticks(tamanos, [str(n) for n in tamanos])
    plt.xlim(min(tamanos) * 0.5, max(tamanos) * 1.5)
    plt.gca().yaxis.set_major_formatter(
        mticker.FuncFormatter(lambda valor, _: f"{valor:.1e}")
    )
    plt.xlabel("Tamaño de matriz (n×n)")
    plt.ylabel("Tiempo medio de ejecución (s)")
    plt.title("Comparación de tiempo: mimatmul vs NumPy")
    plt.yscale("log")
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()

    FIGURA_SALIDA.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(FIGURA_SALIDA, dpi=150)
    print(f"Gráfico guardado en: {FIGURA_SALIDA}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
