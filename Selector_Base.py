#dado un rango de numeros, se genera un control para las preguntas dadas,
NDesde = int(input("Ingrese numero desde: "))
NHasta = int(input("Ingrese numero hasta: "))
numeros = list()
for i in range(NDesde, NHasta):
    numeros.append(i)


while 1==1:
    print("Lista actual: " + str(numeros))
    NQuitar = int(input("Ingrese numero a quitar de la lista o ingrese 0 para salir: "))
    if NQuitar > 0:
        numeros.remove(NQuitar)        
    elif NQuitar == 0:
        break
    else: 
        print("Valor incorrecto, ingrese nuevamente.")

print("Programa finalizado.")