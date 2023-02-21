nombres = []
cont = 0
while cont < 3:
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
    cont = cont + 1
aux = 0
largo = 0
for i in range(3):
    if i == 0:
        largo = len(nombres[i])
    else:
        if largo < len(nombres[i]):
            aux = i
            largo = len(nombres[i])
print("El nombre mas largo es:", nombres[aux])