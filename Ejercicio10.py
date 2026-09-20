#Alumno: RAU QUISPE JOSUE ISAIAS
#Salario con comisión - Ejercicio 10:

salario_fijo = float(input("Ingrese el salario fijo: "))
total_mes = float(input("Ingrese el monto total vendido durante el mes: "))

comisión = total_mes * 0.04
salario_total = salario_fijo + comisión

print(f"La comisión es {comisión:.2f} soles")
print(f"El salario total es {salario_total:.2f} soles")