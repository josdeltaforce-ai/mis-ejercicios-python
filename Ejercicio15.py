#Alumno: RAU QUISPE JOSUE ISAIAS
#Costo final de la compra - Ejercicio 15:

precio_unitario = float(input("Ingrese el precio unitario del producto: "))
cantidad_comprada = int(input("Ingrese la cantidad de compra: "))
valor_envío = float(input("Ingrese el valor del envío: "))

subtotal = precio_unitario * cantidad_comprada
total = subtotal + valor_envío

print(f"El subtotal es {subtotal:.2f}")
print(f"El costo total es de {total:.2f} soles")

