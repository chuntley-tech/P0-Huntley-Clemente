# AGENTS.md — Guía para los agentes de IA de este proyecto

Este archivo es la fuente de verdad que todos los agentes de opencode deben
leer antes de trabajar en este proyecto.

## Proyecto

- Proyecto de curso en **Python 3.14+**.
- Paquete en `src/mcoc/`, tests en `tests/` con **pytest**.
- Configuración del proyecto en `pyproject.toml`.

## Idiomas

- Código, nombres y comentarios: **español** cuando sea razonable, pero
  identificadores en inglés para APIs públicas.
- Documentación y respuestas al usuario: **español**.

## Convenciones de código

- Seguir PEP 8; importaciones ordenadas.
- Añadir type hints a todas las funciones públicas.
- `from __future__ import annotations` al inicio de cada módulo.
- Funciones pequeñas con un solo propósito.
- No añadir comentarios salvo que expliquen el *por qué*, no el *qué*.
- Docstrings en español para módulos y funciones públicas.

## Cómo verificar el trabajo

1. Tests: `pytest` desde la raíz (usar `py -m pytest` si el entorno no está
   activado).
2. Si no hay linter configurado, revisar manualmente que el código sea
   consistente con las convenciones.
3. Instalar en modo editable: `pip install -e ".[dev]"`.

## Agentes disponibles

Los agentes están en `.opencode/agent/`. Roles principales:

- **plan**: divide el trabajo en tareas accionables.
- **review**: revisa calidad y estilo del código.
- **test**: escribe y ejecuta tests.
- **docs**: genera y mantiene documentación.
- **debug**: diagnostica y corrige errores.

## Flujo sugerido para una tarea

1. `plan` para descomponer la tarea.
2. Implementar la funcionalidad.
3. `test` para cubrirla con tests.
4. `review` para validar antes de commit.
5. Commit con mensaje claro en español, estilo imperativo.
