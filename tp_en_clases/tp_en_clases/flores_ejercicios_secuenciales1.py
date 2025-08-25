#Ejercicios complementarios unidad 1

"""1. Crea una variable llamada "numero1" y asígnale un número entero de tu elección """

numero1 = 22

"""2. No borres la variable número uno y crea una variable llamada "numero2" asignándole un número decimal de tu elección. """

numero2 = 2.22

"""3. Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2". """

suma = numero1 + numero2

"""4. Ahora crear tres variables más sin borrar lo que tienes. 
    Una para resta, otra para multiplicación y otra para división. Imprime estas variables """

resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print(f"La suma es : {suma}, La resta es: {resta}, La multiplicación es: {multiplicacion}, La división es: {division}")

"""5. Crea una variable llamada "nombre" y asígnale tu nombre como valor. """

nombre = "Braian"

"""6. Crea una variable llamada "precio" y asígnale un valor decimal que represente el precio de un artículo ficticio. """

precio = 22.2


"""7. Ahora, sin borrar la variable anterior, crea una variable llamada "descuento"
    y asígnale un valor decimal que represente el descuento aplicado al artículo. 
    Por ejemplo, si le quieres aplicar un 25% de descuento, dale un valor de 0,25. 
    El valor 1 equivaldría al 100% y el valor 0 al 0%. """

descuento = 0.35

"""8. Ahora, intenta calcular el precio final aplicando el descuento al precio original y almacena el resultado en una variable llamada "precio_final".
     Para ello vas a tener que aplicar la lógica de matemáticas. """

precio_final = precio - (precio * descuento)

"""9. Crea una variable llamada "cadena" y asignale un texto, una frase, lo que quieras de tu elección. Qué sea un string. """

cadena = "Su producto acepta el descuento semanal del 35%"

"""10. Sin borrar la variable "cadena", crea una nueva variable llamada "longitud". En ella, vas 
    a almacenar la longitud en caracteres de la cadena utilizando una de las funciones de 
    Python. """

longitud = len(cadena)
print (f"La longitud de la cadena es: {longitud} caracteres")

"""11. Crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y 
    conviértelo en número entero. Lo puedes hacer en la misma variable o en otra, da lo mismo. """

precio = 17.77
precio_entero = int(precio)
print(f"El precio entero es: {precio_entero}")

"""12. Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas 
    en una tercera variable llamada "nombre_completo", el nombre y el apellido con un 
    espacio entre medio. Puedes usar libremente la forma de concatenación que quieras. """

nombre = "chinchilla"
apellido = "pipicucu"
nombre_completo  = nombre + " " + apellido
print(f"El nombre completo es: {nombre_completo}")

"""13. Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10. """

edad = 22
edad_incrementada = edad + 5
edad_disminuida = edad_incrementada - 10
print (f"Edad original: {edad}, Edad incrementada en 5: {edad_incrementada}, Edad disminuida en 10: {edad_disminuida}")

"""14. Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y 
    centímetros. Por ejemplo: 1.83. Multiplícala por 4 y luego divídela en 3. """

altura = 1.75
altura_en_metros = altura * 4
altura_en_centimetros = altura_en_metros / 3
print(f"Altura original: {altura}, Altura multiplicada en metros: {altura_en_metros}, Altura dividida en centimetros: {altura_en_centimetros}")

"""15. Crea una variable que contenga tu nombre completamente en mayúsculas. Después 
    transfórmalo todo en minúsculas con algún método o función de Python. """

nombre_mayusculas = "BRAIAN"
nombre_minusculas = nombre_mayusculas.lower() #LOWER() convierte a minúsculas cualquier texto / palabra UPPER() convierte a mayúsculas
print(f"Nombre en mayúsculas: {nombre_mayusculas}, Nombre en minúsculas: {nombre_minusculas}")

"""16. Por último, con la variable con el nombre en mayúsculas, aplica un método parecido 
    para que se transforme todo en minúsculas excepto la primera letra. """

nombre_mayusculas_inicial =  nombre_mayusculas.capitalize() #CAPITALIZE() convierte la primera letra en mayúscula y el resto en minúsculas
print(f"Nombre con primera letra en mayúscula: {nombre_mayusculas_inicial}")