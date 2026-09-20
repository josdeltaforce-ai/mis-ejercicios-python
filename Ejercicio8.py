#Descuento en un producto:

precio_producto = float(input("Ingrese el precio del producto: "))
descuento = precio_producto * 0.1
precio_final = precio_producto - descuento
print(f"El descuento del 10% es de {descuento:.2f}")
print(f"El precio final es de {precio_final:.2f} soles")