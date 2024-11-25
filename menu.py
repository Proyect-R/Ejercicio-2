from operaciones import sumar
from operaciones import restar
from operaciones import multiplicar
from operaciones import dividir
from operaciones import factorial_iterativo
from operaciones import factorial_recursivo
from operaciones import fibonacci

def mostrar_Menu():
 print ("1- sumar")   
 print ("2- restar")   
 print ("3- multiplicar")   
 print ("4- dividir")  
 print ("5- salir")   
 print ("6-Calcular el factorial de un número (iterativo)")  
 print ("7-Calcular el factorial de un número (recursivo)")
 print ("8- Calcular el fibonacci de un número (iterativo)")

        
mostrar_Menu()
numero = int (input("Ingresa un número"))


if numero == 1:
        num1 = input("Ingresa el primer número: ")
        num2 = input("Ingresa el segundo número: ")

        # Verificamos si son int o float
        num1 = float(num1) if '.' in num1 else int(num1)
        num2 = float(num2) if '.' in num2 else int(num2)

        # Llamamos a la función sumar y mostramos el resultado
        print(sumar(num1, num2))
        mostrar_Menu()

elif numero == 2:
        num1 = input("Ingresa el primer número: ")
        num2 = input("Ingresa el segundo número: ")

        # Verificamos si son int o float
        num1 = float(num1) if '.' in num1 else int(num1)
        num2 = float(num2) if '.' in num2 else int(num2)

        # Llamamos a la función restar y mostramos el resultado
        print(restar(num1, num2))
        mostrar_Menu()

elif numero == 3:
        num1 = input("Ingresa el primer número: ")
        num2 = input("Ingresa el segundo número: ")

        # Verificamos si son int o float
        num1 = float(num1) if '.' in num1 else int(num1)
        num2 = float(num2) if '.' in num2 else int(num2)

        # Llamamos a la función multiplicar y mostramos el resultado
        print(multiplicar(num1, num2))
        mostrar_Menu()

elif numero == 4:

        num1 = input("Ingresa el primer número: ")
        num2 = input("Ingresa el segundo número: ")

        num1 = float(num1) if '.' in num1 else int(num1)
        num2 = float(num2) if '.' in num2 else int(num2) 

        print(dividir(num1, num2))
        mostrar_Menu()    

elif numero == 5:
       print("Saliendo...")    


elif numero == 6:
        num = int(input("Ingresa un número entero para calcular su factorial: "))
        
        print(factorial_iterativo(num))

elif numero == 7:
        num = int(input("Ingresa un número entero para calcular su factorial: "))
        factorial_recursivo(num)
        print(factorial_recursivo(num))

elif numero == 8:
    num = int(input("Ingresa un número para calcular su Fibonacci: "))
    print(fibonacci(num))

else:
        print("Opción no válida")