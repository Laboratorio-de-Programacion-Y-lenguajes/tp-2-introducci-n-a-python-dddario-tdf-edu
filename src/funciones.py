# ============================================================
# MÓDULO 6: Funciones
# ============================================================


def aplicar_funcion(lista: list, func) -> list:
    """
    Aplica func a cada elemento de la lista y retorna la nueva lista.
    """
    return [func(elemento) for elemento in lista]


def componer(f, g):
    """
    Retorna una nueva función que aplica g y luego f.
    Ejemplo: componer(f, g)(x) == f(g(x))
    """
    def composicion(x):
        return f(g(x))
    return composicion


def memoizar(func):
    """
    Retorna una versión de func que cachea sus resultados.
    Si se llama con los mismos argumentos, retorna el resultado cacheado.
    """
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


def reducir(lista: list, func, inicial):
    """
    Aplica func acumulativamente a los elementos de lista,
    comenzando con inicial.
    Ejemplo: reducir([1,2,3], lambda a,b: a+b, 0) -> 6
    NO uses functools.reduce
    """
    acumulador = inicial
    for elemento in lista:
        acumulador = func(acumulador, elemento)
    return acumulador
