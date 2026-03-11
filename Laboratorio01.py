"""
Nombre: calculadora
Entradas: operacion, op1, op2
Salidas: Retornar las operaciones soportadas
Restricciones: Los parametros deben de ser de tipo entero
        Los operadores deben de ser de tipo Entero
"""

def calculadora(operacion, op1, op2):
    if not isinstance(operacion, int):
        return "Error: operación debe ser un valor Entero"
    elif operacion <= 0:
        operacion = operacion *- 1

    if not isinstance(op1, int):
        return "Error: op1 debe ser un valor Entero"
    elif op1 <= 0:
        op1 = op1 *- 1

    if not isinstance(op2, int):
        return "Error: op2 debe ser un valor Entero"
    elif op2 <= 0:
        op2 = op2 *- 1

    
    




"""
Nombre: contadorDigitos(num, digito)
Entradas: num, digito
Salidas: retornar el numero de veces que el digito aparece en el numero
Restriciones: Ambos parametros deben ser de tipo entero
        El parametro de digito debe ser menor a 10 y mayor o igual 0
"""

def contadorDigitos(num, digito):
    if not isinstance(num, int):
        return "Error: num debe ser Entero"
    elif num <= 0:
        num = num *- 1

    if not (isinstance(digito, int)):
        return "Error: num debe ser Entero"
    elif (digito >= 10) and (digito <= -10):
        return "Error el parametro digito debe ser un valor menor a 10"
    elif (num == 0) and (digito == 0):
        return 1
    elif (digito < 0):
        digito = digito *- 1

    i = 0

    while num != 0:
        if num % 10 == digito:
            i = i + 1
        num = num // 10

    return i


"""
Nombre: sumatoria_V2
Entradas: inicio, fin, distancia,  excepcion
Salidas: retornar la suma total de los numeros desde el parametro inicio hasta el final
Restricciones: Todos los parametros deben ser de tipo entero
        Los párametros distancia y excepcion debe ser menor a 10 y mayor a 0.
    Los valores de inicio y fin deben ser positivos
    Si la distancia es un número negativo, el valor de fin debe ser menor a inicio
    Si la distancia es un número positivo, el valor de fin debe ser mayor a inicio
    Si excepcion es igual a cero, se debe ignorar este valor, lo contrario,
    todo número dentro de la secuencia entre inicio y ** final** sea divisible por esta excepcion debe omitirse en la suma
"""
    
def sumatoria_V2(inicio, fin, distancia, excepcion):
    if not (isinstance(inicio, int)) or not (isinstance( fin, int)) or not (isinstance(distancia, int)) or not (isinstance(excepcion, int)):
        return "Error: Los parametros deben ser enteros"
    elif(inicio < 0) or(fin < 0):
        return "Error: los valores de inicio y fin deben ser positivos"
    elif(distancia >= 10)
    
