"""
Esta es la expresion regular para el ejercicio 0, que se facilita
a modo de ejemplo:
Hola esto es un cambio
"""
RE0 = "[a-zA-Z]+"

"""
Completa a continuacion las expresiones regulares para los
ejercicios 1-5:
"""
RE1 = "[a-zA-Z0-9_]+.py"
RE2 = "-?(([1-9][0-9]*)|0)?(\.[0-9]*)?"
RE3 = "[a-z]+\.[a-z]+@(estudiante.)?uam.es"
RE4 = "([^\(\)]*\([^\(\)]*\)[^\(\)]*)+"
RE5 = "([^\(\)]*\((([^\(\)]*\([^\(\)]*\)[^\(\)]*)*|[^\(\)]*)\)[^\(\)]*)+"

"""
Recuerda que puedes usar el fichero prueba.py para probar tus
expresiones regulares.
"""

""" 
EJERCICIO 6:
Incluye a continuacion, dentro de esta cadena, tu respuesta 
al ejercicio 6.

Porque para crear una expresión regular que reconozca la profundidad infinita
deberíamos poder contabilizar infinitas aperturas y cierres de una cadena dada, 
lo cual es imposible con una cadena de longitud y caracteres finitos. 
Una manera posible de hacer esto sería generando una pila de elementos, 
en la cual metiésemos (push) tantos paréntesis abiertos cómo encontrásemos y 
sacásemos (pop) tantos paréntesis como paréntesis cerrados encontrásemos, 
de manera que al finalizar, si la pila se encuentra vacía, la cadena ha sido aceptada,
y si aún quedan paréntesis o si en el proceso se ha requerido de extraer un 
paréntesis cuando la pila se encontraba vacía, la cadena no sería aceptada.

"""
