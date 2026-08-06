"""CLI mínima del proyecto."""

from __future__ import annotations

import sys


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if args and args[0] in ("-h", "--help"):
        print("Uso: mcoc [opciones]")
        return 0
    print("MCOC funcionando.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
