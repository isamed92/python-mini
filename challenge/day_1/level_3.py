# Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
from cmath import sqrt


def py_types():
    print("\n Listado de todos los tipos de datos de Python\n")
    print("Integer:", type(1))
    print("Float:", type(1.2))
    print("Complex:", type(1j))
    print("String:", type("Isaias"))
    print("Boolean:", type(True))
    print("Lista:", type([1,3,5,7,15]))
    print("Tupla:", type((2,4,6,8,10)))
    print("Conjunto (set):", type({123,"rojo", 23123.4, 5j}))
    print("Diccionario:", type({1: "isaias", 2: "medina", 3: "Argentina"}))

def distancia_euclidiana(x, y):
    print(f"La distancia euclidiana entre {x} y {y} es: ",sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2))

# py_types()

distancia_euclidiana((3,3.5), (-5.1,-5.2))
distancia_euclidiana((6,8), (-2.1,-4.5))
distancia_euclidiana((1,2), (-12.1,-34.5))
