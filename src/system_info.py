"""Recoge información del sistema y la guarda en data/system_info.json."""

from __future__ import annotations

import ctypes
import json
import os
import platform
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_FILE = DATA_DIR / "system_info.json"


def _physical_cores() -> int:
    """Devuelve el número de núcleos físicos usando la API de Windows."""
    if sys.platform != "win32":
        return 0

    kernel32 = ctypes.windll.kernel32
    relation_processor_core = 0
    required = ctypes.c_ulong(0)

    kernel32.GetLogicalProcessorInformationEx(
        relation_processor_core, None, ctypes.byref(required)
    )

    buffer = ctypes.create_string_buffer(required.value)
    length = ctypes.c_ulong(required.value)
    if not kernel32.GetLogicalProcessorInformationEx(
        relation_processor_core, buffer, ctypes.byref(length)
    ):
        raise ctypes.WinError()

    data = buffer.raw
    cores = 0
    offset = 0
    while offset < len(data):
        relationship = int.from_bytes(data[offset : offset + 4], "little")
        size = int.from_bytes(data[offset + 4 : offset + 8], "little")
        if relationship == relation_processor_core:
            cores += 1
        offset += size
    return cores


def _ram_total_bytes() -> int:
    """Devuelve la memoria RAM total en bytes usando la API de Windows."""
    if sys.platform != "win32":
        raise OSError("La obtención de RAM solo está implementada para Windows")

    class MemoryStatusEx(ctypes.Structure):
        _fields_ = [
            ("dwLength", ctypes.c_ulong),
            ("dwMemoryLoad", ctypes.c_ulong),
            ("ullTotalPhys", ctypes.c_ulonglong),
            ("ullAvailPhys", ctypes.c_ulonglong),
            ("ullTotalPageFile", ctypes.c_ulonglong),
            ("ullAvailPageFile", ctypes.c_ulonglong),
            ("ullTotalVirtual", ctypes.c_ulonglong),
            ("ullAvailVirtual", ctypes.c_ulonglong),
            ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
        ]

    stat = MemoryStatusEx()
    stat.dwLength = ctypes.sizeof(MemoryStatusEx)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat)):
        raise OSError("No se pudo obtener la memoria RAM total")
    return int(stat.ullTotalPhys)


def collect_system_info() -> dict[str, str | int]:
    """Recoge la información del sistema en un diccionario."""
    ram_bytes = _ram_total_bytes()
    return {
        "sistema_operativo": platform.system(),
        "arquitectura": platform.machine(),
        "version_python": platform.python_version(),
        "modelo_procesador": platform.processor(),
        "nucleos_fisicos": _physical_cores(),
        "procesadores_logicos": os.cpu_count() or 0,
        "memoria_ram_total_bytes": ram_bytes,
        "memoria_ram_total_gb": round(ram_bytes / (1024**3), 2),
    }


def main() -> int:
    """Genera data/system_info.json y muestra la información en consola."""
    info = collect_system_info()
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(
        json.dumps(info, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(info, ensure_ascii=False, indent=2))
    print(f"\nGuardado en: {OUTPUT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
