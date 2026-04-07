[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/X4xiTEDQ)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23462307)
# TP 2 · Introducción a Python y Patrones de Prompting (GitHub Classroom)

**Stack**: Python 3.13+, `pytest`, Git/GitHub Classroom (autograding)  
**Entrega**: código en el repositorio asignado (push a `main`). Los tests se ejecutan automáticamente.

---

## 1) Objetivo

Resolver 7 ejercicios introductorios de Python (variables, condicionales, listas, funciones, diccionarios, loops y excepciones) aplicados a problemas simples en consola, y **registrar un ejemplo de prompt** (uno por ejercicio) siguiendo el patrón indicado.

**Importante**: el autograding evalúa **solo** el código (funciones). El uso de LLM se evalúa de forma **manual** leyendo tus prompts documentados.

---

## 2) Instalación de Python y pip (guía rápida)

### Opción A (recomendada): Instalación oficial de Python

#### Windows (10/11)
1. Descargá Python 3.13.x desde la web oficial (Python Downloads).
2. Durante la instalación:
   - Marcá **“Add Python to PATH”**.
   - Elegí **Install Now**.
3. Verificá en PowerShell o CMD:
   ```bash
   python --version
   pip --version
   ```

Si `python` no se reconoce, reiniciá la terminal o reinstalá asegurando “Add Python to PATH”.

#### macOS
1. Recomendado: instalar Python con Homebrew.
   - Instalá Homebrew (si no lo tenés) y luego:
     ```bash
     brew install python@3.13
     ```
2. Verificá:
   ```bash
   python3 --version
   pip3 --version
   ```

> En macOS, a veces el comando es `python3` y `pip3`.

#### Linux (Ubuntu/Debian)
1. Instalación (según repositorios disponibles):
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```
2. Verificá:
   ```bash
   python3 --version
   pip3 --version
   ```

> Si tu distro no trae 3.13, podés usar 3.11+ localmente para trabajar, pero el autograding corre en la versión configurada por la cátedra.

---

## 3) Setup del proyecto (tu repo de Classroom)

1. Cloná tu repo:
   ```bash
   git clone <URL-del-repo-asignado>
   cd <carpeta-del-repo>
   ```

2. (Recomendado) Crear entorno virtual:
   - Windows (PowerShell):
     ```bash
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - macOS/Linux:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. Instalá dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Corré los tests:
   ```bash
   pytest -v
   ```

---

## 4) Cómo se entrega

- Completá las funciones en `src/`.
- Corré tests localmente (`pytest -v`).
- Hacé commits significativos (mínimo 7).
- Hacé `push` a `main`.
- Revisá GitHub → **Actions** para ver si quedó ✅.

---

## 5) Registro de prompts (obligatorio)

Creá/actualizá el archivo `PROMPTS.md` en la raíz del repo con **1 prompt por ejercicio**.

Formato mínimo sugerido:

```markdown
## variables.py (Patrón: Receta)
Prompt:
> ...

## condicionales.py (Patrón: Interacción invertida)
Prompt:
> ...
```

No hace falta link si el LLM no lo permite, pero sí el texto del prompt.

---

## 6) Ejercicios + Ejemplos de prompt por patrón

### 6.1 Script 1 — Variables y tipos (`src/variables.py`)
**Patrón**: Receta  
**Qué hace**: arma el mensaje `"Soy [nombre], tengo [edad] años y vivo en [ciudad]."`

**Ejemplo de prompt (Receta)**:
> Actuá como tutor de Python 3.13. Dame una receta paso a paso para:  
> 1) pedir por consola nombre (str), edad (int) y ciudad (str),  
> 2) validar que edad sea un entero,  
> 3) devolver un string usando f-strings con el formato: "Soy {nombre}, tengo {edad} años y vivo en {ciudad}."  
> No uses librerías externas. Mostrá una función `armar_mensaje(nombre, edad, ciudad)` con docstring.

---

### 6.2 Script 2 — Condicionales (`src/condicionales.py`)
**Patrón**: Interacción invertida  
**Qué hace**: clasifica un número: negativo/cero/positivo par/positivo impar.

**Ejemplo de prompt (Interacción invertida)**:
> Quiero implementar una función `evaluar_numero(n: int) -> str` en Python.  
> Antes de escribir el código, haceme 3 preguntas para confirmar:  
> - qué mensajes exactos debo devolver,  
> - cómo tratar el 0,  
> - y cómo priorizar condiciones (por ejemplo, primero negativo o primero paridad).  
> Después de mis respuestas, recién ahí proponé el código.

---

### 6.3 Script 3 — Listas (`src/listas.py`)
**Patrón**: Verificador cognitivo  
**Qué hace**: calcula `suma(lista)` y `promedio(lista)` (promedio de lista vacía = 0.0).

**Ejemplo de prompt (Verificador cognitivo)**:
> Estoy resolviendo un ejercicio de listas en Python con estas reglas:  
> - `suma(lista)` debe devolver `sum(lista)`  
> - `promedio(lista)` debe devolver 0.0 si la lista está vacía, si no `sum(lista)/len(lista)`  
> ¿Podés revisar mi lógica como verificador cognitivo?  
> 1) enumerá casos borde que debería testear,  
> 2) decime errores típicos (por ejemplo división por cero),  
> 3) proponé 3 tests con entradas y salidas esperadas (sin escribir el código final por mí).

---

### 6.4 Script 4 — Funciones (`src/funciones.py`)
**Patrón**: Reflexión  
**Qué hace**: `contar_palabra(texto, palabra)` contando ocurrencias exactas, case-insensitive.

**Ejemplo de prompt (Reflexión)**:
> Necesito una función `contar_palabra(texto: str, palabra: str) -> int` en Python 3.13.  
> Quiero comparar enfoques y elegir uno simple y performante para un TP:  
> - split + count  
> - recorrer manualmente  
> - regex  
> Analizá pros/contras (performance + simplicidad + edge cases como puntuación).  
> Luego recomendá UNO y escribí el código con docstring, dejando claro qué casos NO cubre (por ejemplo, "hola," vs "hola").

---

### 6.5 Script 5 — Diccionarios (`src/diccionarios.py`)
**Patrón**: Generación infinita  
**Qué hace**: `mostrar_datos(dic)` devuelve `"[nombre] [apellido] ([edad]) - [mail]"`.

**Ejemplo de prompt (Generación infinita)**:
> Generá 8 ejemplos distintos de diccionarios Python que representen personas con claves:  
> `nombre`, `apellido`, `edad`, `mail`.  
> Para cada ejemplo, mostrámelo y también mostrámelo formateado como:  
> "{nombre} {apellido} ({edad}) - {mail}".  
> Luego extraé una regla general para implementar `mostrar_datos(dic)`.

---

### 6.6 Script 6 — Loops (`src/loops.py`)
**Patrón**: Refinamiento de preguntas  
**Qué hace**: `repetir_palabra(palabra, cantidad)` retorna lista con la palabra repetida N veces (si N<0 → []).

**Ejemplo de prompt (Refinamiento de preguntas)**:
> P1: ¿Cómo repito una palabra N veces en Python y obtengo una lista?  
> P2: ¿Cuál es la forma más simple si N puede ser 0?  
> P3: ¿Qué debería hacer si N es negativo? ¿Conviene lanzar error o devolver lista vacía para un TP?  
> P4: Mostrame una implementación de `repetir_palabra(palabra: str, cantidad: int) -> list[str]` que devuelva [] si cantidad < 0.

---

### 6.7 Script 7 — Excepciones (`src/operaciones.py`)
**Patrón**: Enfoques alternativos  
**Qué hace**: `operaciones(a,b)` devuelve dict con suma/resta/multiplicación/división, y si b=0 en división: `"Error: división por cero"`.

**Ejemplo de prompt (Enfoques alternativos)**:
> Tengo que implementar `operaciones(a: float, b: float) -> dict` para un TP.  
> Compará 3 enfoques:  
> A) usar `if b == 0` para evitar la división,  
> B) usar `try/except ZeroDivisionError`,  
> C) devolver `None` o lanzar excepción.  
> Elegí el más adecuado para principiantes + tests con pytest, justificá, y escribí el código final.

---

## 7) Criterios de aprobación

- [ ] Todos los tests pasan (`pytest -v`)
- [ ] Cobertura ≥ 70% (`pytest --cov=src --cov-fail-under=70`)
- [ ] Código claro: nombres descriptivos, sin duplicación innecesaria
- [ ] Mínimo 7 commits significativos (uno por script)
- [ ] `PROMPTS.md` con 7 prompts (uno por ejercicio)

---

## 8) Troubleshooting rápido

- **`pip: command not found`**: usá `python -m pip --version` (o `python3 -m pip ...`)
- **No corre pytest**: asegurate de activar el entorno virtual `.venv` y correr `pip install -r requirements.txt`
- **Falla un test**: leé el mensaje, muestra “esperado vs obtenido”
- **Actions falla pero local pasa**: revisá versión de Python configurada y dependencias
