
#Función para sumar
def sumar(numero_uno, numero_dos):
   
    #validamos que numero uno sea int o float
    if not isinstance(numero_uno, (int, float)):
        raise ValueError("El primer parámetro debe ser un int o float.")

    #validamos que numero dos sea int o float
    if not isinstance(numero_uno, (int, float)):
        raise ValueError("El segundo parámetro debe ser un int o float.")

    #realizamos la operacion 
    resultado = numero_uno + numero_dos
    return resultado

#Función para restar
def restar(numero_uno, numero_dos):
 
    #validamos que numero uno sea int o float
    if not isinstance(numero_uno, (int, float)):
        raise ValueError("El primer parámetro debe ser un int o float.")

    #validamos que numero dos sea int o float
    if not isinstance(numero_uno, (int, float)):
        raise ValueError("El segundo parámetro debe ser un int o float.")

    #realizamos la operacion 
    resultado = numero_uno -  numero_dos
    return resultado

 #funcion para multiplicacion
def multiplicar(valor1, valor2):
  
    #validamos que los valores sean int o float
    if not isinstance(valor1, (int, float)):
        raise ValueError("El primer parámetro debe ser int o float.")
    if not isinstance(valor2, (int, float)):
        raise ValueError("El segundo parámetro debe ser int o float.")

    #convertimos los valores
    #a enteros para manejar la recurrencia
    valor1 = int(valor1)
    valor2 = int(valor2)

    #manejar multiplicación por cero
    if valor1 == 0 or valor2 == 0:
        return 0

    #determinar el signo del resultado
    negativo = (valor1 < 0) ^ (valor2 < 0)  

    #usamos los valores absolutos
    #para la suma recurrente
    valor1, valor2 = abs(valor1), abs(valor2)

    #realizamos la suma recurrente
    resultado = 0
    for _ in range(valor2):
        resultado += valor1

    #ajustar el signo del resultado
    return -resultado if negativo else resultado  


def dividir(dividendo, divisor):
    # Verificar que ambos parámetros sean números (int o float)
    if not isinstance(dividendo, (int, float)) or not isinstance(divisor, (int, float)):
        return "Error: Ambos parámetros deben ser números (enteros o decimales)"
    
    # Verificar que el divisor no sea 0
    if divisor == 0:
        return "Error: El divisor no puede ser cero"
    
    # Realizar la división (restando iterativamente)
    cociente = 0
    while dividendo >= divisor:
        dividendo -= divisor

        cociente += 1
    
    return cociente, dividendo


# Función para calcular el Fibonacci de un número de forma iterativa
def fibonacci(n):
    # Verificamos si el número es un entero positivo
    if not isinstance(n, int):
        raise ValueError("El valor debe ser un entero.")
    if n < 0:
        raise ValueError("El número debe ser mayor o igual a 0.")
    
    # Caso base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Calculamos el Fibonacci de manera iterativa
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b
