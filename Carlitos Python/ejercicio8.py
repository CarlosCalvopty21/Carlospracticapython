Nombre = input("Nombre: ")
Edad = int(input("Edad: "))
Nota1 = float(input("Ingresa nota1: "))
Nota2 = float(input("Ingresa nota2 "))
Nota3 = float(input("Ingresa nota3 "))
promedio = Nota1 + Nota2 + Nota3 
division = promedio / 3
if division >= 71:
    print("Aprobaste")
else:
    print("Reprobaste")
