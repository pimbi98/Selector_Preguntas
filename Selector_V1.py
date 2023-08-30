#dado un rango de numeros, se genera un control para las preguntas dadas,
import random
import time
preguntas = list()
preguntasRealizadas = list()
def addPreguntasRealizadas(p): #Añade a lista de preguntas ya realizadas.
    preguntasRealizadas.append(p)

def printPreguntasRealizadas():
    print("Se hicieron " + str(len(preguntasRealizadas)) + " Preguntas")
    print("Preguntas realizadas en orden realizado: " + str(preguntasRealizadas))


def printPreguntasRestantes(l):
    print("Quedan " + str(len(l)) + " Preguntas")
    print("Lista actual: " + str(l))

def Manual(preguntas):
    while 1==1:
        printPreguntasRestantes(preguntas)
        nro = int(input("Ingrese numero a quitar de la lista o ingrese 0 para salir: "))
        if nro > 0:
            addPreguntasRealizadas(nro)
            preguntas.remove(nro)        
        elif nro == 0:
            return
        else: 
            print("Valor incorrecto, ingrese nuevamente.")


def Aleatorio(preguntas):
    r = random.randint(1, len(preguntas))
    nro = preguntas[r]
    print("Numero a quitar aleatoriamente es: " + str(nro))
    addPreguntasRealizadas(nro)
    preguntas.pop(r)
    time.sleep(1)
##---------------------- 0 ------------------------------##
NErrores = 0
NDesde = int(input("Ingrese numero desde: "))
NHasta = int(input("Ingrese numero hasta: "))

for i in range(NDesde, NHasta):
    preguntas.append(i)


while 1==1:
    printPreguntasRestantes(preguntas)
    print("Acciones que se pueden realizar: ")
    print("M: Quitar numeros Manualmente. ")
    print("A: Quitar numeros Aleatoriamente. ")
    print("P: Imprimir lista actual. ")
    print("R: Mostrar preguntas realizadas. ")
    print("X: Salir del programa. ")
    Accion = input("Ingrese Acción: ")
    if Accion == "M": #Saco preguntas de lista manualmente.
        Manual(preguntas)
    elif Accion == 'A': #Aleatorios
        Aleatorio(preguntas)
    elif Accion == 'P':
        printPreguntasRestantes(preguntas)
    elif Accion == 'X':
        break
    elif Accion == 'R':
        printPreguntasRealizadas()
    else:
        NErrores = NErrores + 1
        print("Valor incorrecto.")
        if NErrores >= 3:
            print("Se equivocó demasiadas veces. Finalizando programa... ")
            time.sleep(3)
            break

print("Programa finalizado.")

