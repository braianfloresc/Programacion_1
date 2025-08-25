#Calculadora de propinas en un restaurante
#se ingresa el monto
monto_total = float(input("Ingrese el monto total de la cuenta: " ))  
#se calcula propina del 15% y 10%     
propina_sugerida = monto_total * 0.15
propina = monto_total * 0.10
#se imprime las dos opciones de propina
print (f"La propina sugerida es:  {propina_sugerida} con el 15% , en total seria {monto_total + propina_sugerida } pesos")
print (f"Sino la propina es:  {propina} con el 10%, en total seria {monto_total + propina } pesos")