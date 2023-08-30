#dado un rango de numeros, se genera un control para las preguntas dadas,
import random
numeros = list()
def Manual(numeros):
    while 1==1:
        NQuitar = int(input("Ingrese numero a quitar de la lista o ingrese 0 para salir: "))
        if NQuitar > 0:
            numeros.remove(NQuitar)        
        elif NQuitar == 0:
            return
        else: 
            print("Valor incorrecto, ingrese nuevamente.")


def Aleatorio(numeros):
    r = random.randint(1, len(numeros))
    print("Numero a quitar aleatoriamente es: " + str(numeros[r]))
    numeros.pop(r)     

NDesde = int(input("Ingrese numero desde: "))
NHasta = int(input("Ingrese numero hasta: "))

for i in range(NDesde, NHasta):
    numeros.append(i)


while 1==1:
    print("Lista actual: " + str(numeros))
    print("Acciones que se pueden realizar: ")
    print("M: Quitar numeros Manualmente. ")
    print("A: Quitar numeros Aleatoriamente. ")
    print("P: Imprimir lista actual. ")
    print("X: Salir del programa. ")
    Accion = input("Ingrese Acción: ")
    if Accion == "M": #Saco numeros de lista manualmente.
        Manual(numeros)
    elif Accion == 'A': #Aleatorios
        Aleatorio(numeros)
    elif Accion == 'P': #Aleatorios
        print(numeros)
    elif Accion == 'X':
        break

print("Programa finalizado.")