
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

#llamamos a la funcion 
#y damos valor a los parametros
    print(sumar(10, 5.5))  

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

#llamamos a la funcion 
#y damos valor a los parametros
    print(restar(6, 5)) 

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

#imprimimos y damos valor
#a cada parametro
print(multiplicar(5, 3))   
