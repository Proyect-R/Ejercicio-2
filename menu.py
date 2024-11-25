from operaciones import sumar
from operaciones import restar
from operaciones import multiplicar

def mostrar_Menu():
 print ("1- sumar")   
 print ("2- restar")   
 print ("3- multiplicar")   
 print ("4- dividir")   
 print ("5- salir")   

numero = input("Ingresa un número")

if numero == 1:
        num1 = input("Ingresa el primer número: ")
        num2 = input("Ingresa el segundo número: ")

        # Verificamos si son int o float
        num1 = float(num1) if '.' in num1 else int(num1)
        num2 = float(num2) if '.' in num2 else int(num2)

        # Llamamos a la función sumar y mostramos el resultado
        print(sumar(num1, num2))

elif numero == 2:
        num1 = input("Ingresa el primer número: ")
        num2 = input("Ingresa el segundo número: ")

        # Verificamos si son int o float
        num1 = float(num1) if '.' in num1 else int(num1)
        num2 = float(num2) if '.' in num2 else int(num2)

        # Llamamos a la función restar y mostramos el resultado
        print(restar(num1, num2))

elif numero == 3:
        num1 = input("Ingresa el primer número: ")
        num2 = input("Ingresa el segundo número: ")

        # Verificamos si son int o float
        num1 = float(num1) if '.' in num1 else int(num1)
        num2 = float(num2) if '.' in num2 else int(num2)

        # Llamamos a la función multiplicar y mostramos el resultado
        print(multiplicar(num1, num2))

elif numero == 4:
        print("Hasta luego")
        
else:
        print("Opción no válida")