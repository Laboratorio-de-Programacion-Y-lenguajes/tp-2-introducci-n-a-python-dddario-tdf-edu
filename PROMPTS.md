# Registro de Prompts

En este archivo se documentan los prompts utilizados con herramientas de IA
(Claude Code) durante el desarrollo del TP.

---

## Mis prompts

### 1 - variables.py (Patrón: Receta)

**Herramienta**: Claude Code

**Prompt usado**:
> Actuá como tutor de Python 3.13. Dame una receta paso a paso para implementar
> las siguientes funciones en variables.py:
> 1) `crear_saludo(nombre)` que retorne "Hola, {nombre}!" usando f-strings,
> 2) `suma_enteros(a, b)` que retorne la suma de dos enteros,
> 3) `es_mayor_de_edad(edad)` que retorne True si edad >= 18,
> 4) `tipo_de_dato(valor)` que retorne el nombre del tipo usando type().__name__,
> 5) `convertir_a_float(valor)` que convierta un string a float.
> No uses librerías externas. Cada función debe tener docstring.

**Resultado obtenido**:
Claude generó implementaciones simples y directas para las 5 funciones, usando
f-strings, operadores de comparación y funciones built-in de Python.

**¿Lo usaste tal cual o lo modificaste?**
Se usó tal cual. Las implementaciones son directas y corresponden exactamente
con lo esperado por los tests.

---

### 2 - condicionales.py (Patrón: Interacción invertida)

**Herramienta**: Claude Code

**Prompt usado**:
> Quiero implementar las funciones de condicionales.py en Python.
> Antes de escribir el código, confirmame:
> - Para `clasificar_numero(n)`: ¿qué strings exactos debo retornar y cómo trato el 0?
> - Para `clasificar_nota(nota)`: ¿los rangos son con >= o con >?
> - Para `es_bisiesto(anio)`: ¿cuál es la regla exacta para años divisibles por 100 y 400?
> Después de mis respuestas, proponé el código final.

**Resultado obtenido**:
Claude aclaró que el 0 retorna "cero" (no "positivo"), que los rangos usan >=,
y explicó la regla del año bisiesto (div. por 4 excepto 100, salvo 400).
Luego generó el código con if/elif/else anidados.

**¿Lo usaste tal cual o lo modificaste?**
Se usó tal cual. La interacción previa ayudó a confirmar los casos borde
antes de escribir el código.

---

### 3 - listas.py (Patrón: Verificador cognitivo)

**Herramienta**: Claude Code

**Prompt usado**:
> Estoy resolviendo ejercicios de listas en Python con estas reglas:
> - `suma_lista([])` debe retornar 0 (sum de lista vacía)
> - `invertir_lista` NO debe modificar la lista original
> - `eliminar_duplicados` debe mantener el orden de primera aparición
> - `aplanar_lista` aplana solo un nivel de profundidad
> ¿Podés revisar mi lógica como verificador cognitivo?
> 1) Enumerá casos borde que debería testear,
> 2) Indicá errores típicos (lista vacía, mutación accidental, etc.),
> 3) Proponé implementaciones correctas con list comprehensions.

**Resultado obtenido**:
Claude identificó: lista vacía en suma_lista, mutación con reverse() en lugar
de [::-1], y duplicados con set (que pierde orden) vs set+lista. Propuso
implementaciones con list comprehensions y slicing.

**¿Lo usaste tal cual o lo modificaste?**
Se adoptaron las sugerencias. En particular, `invertir_lista` usa `lista[::-1]`
para no mutar el original, y `eliminar_duplicados` usa set para control pero
lista para mantener orden.

---

### 4 - diccionarios.py (Patrón: Generación infinita)

**Herramienta**: Claude Code

**Prompt usado**:
> Generá 5 ejemplos distintos de uso de diccionarios en Python para estas operaciones:
> 1) contar frecuencia de palabras (case-insensitive),
> 2) invertir claves y valores,
> 3) merge de dos dicts donde d2 tiene prioridad,
> 4) filtrar pares por valor mínimo.
> Para cada ejemplo mostrá el input y output esperado.
> Luego extraé una regla general para implementar cada función.

**Resultado obtenido**:
Claude generó ejemplos variados y derivó las reglas: usar `.lower().split()` y
`.get()` para contar, dict comprehension para invertir, `{**d1, **d2}` para merge,
y comprensión con condición para filtrar.

**¿Lo usaste tal cual o lo modificaste?**
Se usó la lógica propuesta. Para `merge_diccionarios` se prefirió `.copy()` +
`.update()` en lugar de `{**d1, **d2}` por legibilidad explícita.

---

### 5 - loops.py (Patrón: Refinamiento de preguntas)

**Herramienta**: Claude Code

**Prompt usado**:
> P1: ¿Cómo genero una lista de 1 a N en Python de forma idiomática?
> P2: ¿Cuál es la forma más simple de calcular los primeros 10 múltiplos de N?
> P3: ¿Cómo sumo los dígitos de un número sin convertirlo a string?
> P4: ¿Cuál es el algoritmo más simple para verificar si N es primo?
> P5: Mostrámela implementación de `fibonacci(n)` que retorne los primeros N números,
> empezando por [0, 1, 1, 2, 3, 5...].

**Resultado obtenido**:
Claude respondió cada pregunta progresivamente: `list(range(1, n+1))`,
list comprehension con `range(1,11)`, conversión a str para `suma_digitos`,
raíz cuadrada para la prueba de primalidad, y bucle while para fibonacci.

**¿Lo usaste tal cual o lo modificaste?**
Se adoptaron todas las sugerencias. Para `suma_digitos` se usó `str(n)` ya que
es más legible que la aritmética manual con módulo 10.

---

### 6 - funciones.py (Patrón: Reflexión)

**Herramienta**: Claude Code

**Prompt usado**:
> Necesito implementar funciones de orden superior en Python 3.13 para un TP:
> - `aplicar_funcion(lista, func)`: map manual,
> - `componer(f, g)`: composición f(g(x)),
> - `memoizar(func)`: caché con dict,
> - `reducir(lista, func, inicial)`: fold manual sin functools.
> Quiero comparar enfoques para cada una:
> A) usando built-ins (map, functools),
> B) usando closures y funciones anidadas,
> C) usando lambda.
> Elegí el más claro para principiantes y justificá. Luego escribí el código final.

**Resultado obtenido**:
Claude recomendó list comprehensions para `aplicar_funcion`, función anidada para
`componer` y `memoizar` (más legible que lambda), y bucle for para `reducir`.
Justificó que las closures son más explícitas para aprender.

**¿Lo usaste tal cual o lo modificaste?**
Se usó la recomendación de funciones anidadas (closures). Es el enfoque más
didáctico y queda claro cómo funciona el caché en `memoizar`.

---

### 7 - operaciones.py (Patrón: Enfoques alternativos)

**Herramienta**: Claude Code

**Prompt usado**:
> Tengo que implementar operaciones con strings para un TP en Python 3.13.
> Compará 3 enfoques para `es_palindromo`:
> A) limpiar con replace + comparar con [::-1],
> B) usar regex para limpiar,
> C) comparar caracter por caracter con dos punteros.
> Para `caesar_cipher`, compará:
> A) usar ord/chr con módulo 26,
> B) usar str.maketrans/str.translate,
> C) construir manualmente el alfabeto como string.
> Elegí el más adecuado para principiantes, justificá, y escribí el código final.

**Resultado obtenido**:
Claude recomendó el enfoque A para ambos casos: más legible, sin imports extra
y cubre los casos del test. Para caesar_cipher, ord/chr con % 26 maneja
correctamente el wrap-around (xyz → yza).

**¿Lo usaste tal cual o lo modificaste?**
Se usó tal cual. El enfoque con ord/chr es el más claro para entender cómo
funciona el cifrado César a nivel de código ASCII.

---

## Reflexión final

Aprendí que la calidad del prompt impacta directamente en la calidad de la respuesta: ser específico sobre los casos borde (lista vacía, N negativo, wrap-around en Caesar) evita tener que corregir el código después. La IA fue muy útil para comparar enfoques y elegir el más claro para principiantes, ahorrando tiempo en investigación. En cambio, fue menos útil cuando el prompt era vago: si solo preguntaba "cómo hago X", la respuesta era genérica. La próxima vez usaría el patrón de "enfoques alternativos" desde el inicio para todos los ejercicios, ya que obliga a entender el problema antes de escribir el código.
