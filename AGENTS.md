# AGENTS.md — Guía para los agentes de IA de este proyecto

Este archivo es la fuente de verdad que todos los agentes de opencode deben
leer antes de trabajar en este proyecto.

## Proyecto

- Proyecto de curso en **Python 3.14+**.
- **Propósito**: desarrollar un entorno de trabajo reutilizable y aplicaciones
  pequeñas usando **desarrollo asistido por agentes de IA**.
- Paquete en `src/mcoc/`, tests en `tests/` con **pytest**.
- Configuración del proyecto en `pyproject.toml` y dependencias en
  `requirements.txt`.

## Reglas obligatorias

- **Mantener el código sencillo**: priorizar la claridad sobre la complejidad;
  no sobre-ingeniería.
- **No inventar mediciones**: nunca fabricar valores, resultados o datos que
  no hayan sido obtenidos realmente.
- **No ejecutar comandos destructivos de Git**: evitar operaciones que borren
  historia (`push --force`, `reset --hard`, `filter-branch`, etc.) salvo
  petición explícita del usuario.
- **No subir credenciales**: revisar que no haya secretos, tokens ni claves
  antes de commitear.
- **Ejecutar las pruebas después de modificar código**: correr `pytest` cada
  vez que se cambie código y antes de dar por terminada una tarea.

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
3. Instalar dependencias: `pip install -r requirements.txt`.

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
