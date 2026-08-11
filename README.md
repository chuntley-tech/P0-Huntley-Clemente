# MCOC — Proyecto del curso

## Propósito general

Proyecto del curso basado en **desarrollo asistido por agentes de IA**.
Establece un entorno de trabajo reutilizable con opencode, agentes
especializados y buenas prácticas de código, como base para el resto del curso.

## Entorno de desarrollo

- Sistema operativo: **Windows**
- Python: **3.14.7** (se requiere 3.14+)
- Shell: PowerShell

## Requisitos

- Python 3.14+
- Git

## Clonar o descargar el repositorio

**Con git** (recomendado):

```powershell
git clone https://github.com/chuntley-tech/P0-Huntley-Clemente.git
cd P0-Huntley-Clemente
```

**Descargar manualmente**: botón verde "Code" → "Download ZIP" en el
repositorio, y extraer el contenido.

## Crear el ambiente virtual

Se crea una sola vez, igual en ambas terminales:

```
py -m venv .venv
```

## Activar el ambiente virtual

**PowerShell**
```powershell
.\.venv\Scripts\Activate.ps1
```

**CMD**
```cmd
.venv\Scripts\activate.bat
```

Verás `(.venv)` al inicio de la línea cuando esté activo. Para desactivarlo:
`deactivate`.

## Instalar dependencias

```powershell
pip install -r requirements.txt
```

## Ejecutar las pruebas

```powershell
pytest
```

## Ejecutar el benchmark

Mide el tiempo de `mimatmul` para matrices 2x2 y 10x10:

```powershell
py src/benchmark.py
```

## Información del sistema

Genera un reporte del sistema en `data/system_info.json` (SO, arquitectura,
versión de Python, procesador, núcleos y RAM):

```powershell
py src/system_info.py
```

## Estado actual del proyecto

- Estructura base creada: `src/mcoc/`, `tests/`, `pyproject.toml`.
- Configuración de agentes de IA lista: `.opencode/agent/` y `AGENTS.md`.
- CLI mínima funcional (`mcoc`) y tests iniciales pasando.
- Script de información del sistema (`src/system_info.py`) con salida en
  `data/system_info.json`.
- Multiplicación de matrices propia (`src/mimatmul.py`) con benchmark
  (`src/benchmark.py`).
- Repositorio público en GitHub con el código pusheado.

## Estructura

```
MCOC/
├── .opencode/       # Agentes y comandos de IA (opencode)
├── data/            # Salidas generadas (información del sistema)
├── src/mcoc/        # Código del proyecto
├── src/system_info.py    # Script de información del sistema
├── src/mimatmul.py       # Multiplicación de matrices propia
├── src/benchmark.py      # Benchmark de mimatmul
├── tests/           # Tests (pytest)
├── requirements.txt       # Dependencias del proyecto
└── pyproject.toml
```

## Agentes de IA

Consulta [AGENTS.md](AGENTS.md) para conocer los agentes disponibles y cómo
usarlos con opencode.
