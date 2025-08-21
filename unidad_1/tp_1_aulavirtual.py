
#Práctico 1: Estructuras secuenciales
#Nombre alumno: braian flores

    # ejercicio 1

print("Hola Mundo!")

    # ejercicio 2

nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}! ")

    # ejercicio 3

nombre = input("Ingrese su nombre: ")  
apellido = input("Ingrese su apellido: ")   
edad = input("Ingrese su edad: ")   
residencia = input("Ingrese su lugar de residencia: ")      
print(f"Soy {nombre}  {apellido}, tengo {edad} años y vivo en {residencia}") 

    # ejercicio 4

radio = float(input("Ingresa el radio del círculo: "))
area = 3.14 * radio**2
perimetro = 2 * 3.14
print(f"El área del círculo es: {area:}")
print(f"El perímetro del círculo es: {perimetro:}")

    # ejercicio 5

segundos = int(input("Ingresa cantidad de segundos: "))
horas = segundos // 3600
print(f"{segundos} segundos son {horas} horas.")

    # ejercicio 6

numero = int(input("Ingresa el numero del cual desea conocer su tabla: "))
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

    # ejercicio  7

numero = int(input("Ingresa el primer número  que sea distinto a cero: "))

numero2 = int(input("Ingresa el segundo número que sea distinto a cero: "))

print(f"{numero} + {numero2} = {numero + numero2}")
print(f"{numero} - {numero2} = {numero - numero2}")
print(f"{numero} x {numero2} = {numero * numero2}")
print(f"{numero} / {numero2} = {numero // numero2}")

    # ejercicio 8

altura = int(input("Ingresa su altura en centímetros: "))
peso = int(input("Ingresa su peso en kilogramos: "))
altura_metro = altura / 100
print(f"Su altura en metros es: {altura_metro}")
imc = peso / (altura_metro ** 2)
print(f"Tu índice de masa corporal es: {imc}")

    # ejercicio 9 

temperatura = int(input("Ingrese la temperatura en grados celsius: "))
print(f"La temperatura en grados fahrenheit es: {temperatura * 9/5 + 32}")

    # ejercicio 10

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio de los tres números es: {promedio}")