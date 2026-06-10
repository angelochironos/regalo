# Algoritmos y Estructuras de Datos TP1 2026

# Integrantes:
# Bianco Genaro
# Chirinos Angelo
# Colquicocha Daiana
# Egidi Giuliana

# Variables: 
# nombre1, nombre2, nombre4, opc, prediccion: string
# cont1, cont2, cont4, racha1, perdidas2, ganadas2, perdidas4, ganadas4, cont, numero1, numero2, aciertos, fallas, creditosTotal, dado1, dado2, suma, creditos, a: int

import random
nombre1=" "
nombre2=" "
nombre4=" "
cont1=0
cont2=0
cont4=0
racha1=0
perdidas2=0
ganadas2=0
perdidas4=0
ganadas4=0

print("\n*** Los juegos de apuesta están prohibidos para los menores y es perjudicial para la salud. ***")

def MENU():
    print("\n* MENÚ PRINCIPAL DE JUEGOS ")
    print("\nA- Menor o mayor.")
    print("B- Número Secreto.")
    print("C- BlackJack Simple.")
    print("D- Par o impar.")
    print("E- Reportes.")
    print("S- Salir del programa.")   
  
    
def menuReporte():
    print("\n** Reportes")
    print("\nA- Ver cantidad de veces que cada jugador jugó a cada juego.")
    print("B- En el juego 'Menor-mayor' ver mayor racha alcanzada.")    
    print("C- En el juego 'Número secreto' ver cantidad de veces que perdió y que ganó.")
    print("D- En el juego 'Par o impar' ver cantidad de veces que perdió y que ganó.")
    print("V- Volver al menú principal de juegos.")    
      
    
def Juego1():
    global cont1
    global racha1
    global nombre1
    nombre1=input("\nIngrese el nombre del jugador: ")
    print("\n** ¡ Hola ", nombre1, "! El juego consiste adivinar si el siguiente número será mayor o menor al actual.")
    cont=0
    numero1 = random.randint(1, 1000)
    opc="1"
    while (opc=="1"):
        cont1+=1
        prediccion=""        
        while (prediccion.lower()!="mayor" and prediccion.lower()!="menor"):
            print("\nEl número actual es: ", numero1)
            prediccion = input("¿El número siguiente será mayor o menor? Ingrese mayor o menor: ")
            numero2 = random.randint(1, 1000)

        if ((prediccion.lower()=="mayor" and numero2>numero1)or(prediccion.lower()=="menor" and numero1>numero2)):
            cont+=1
            numero1=numero2
            print("\n* ¡ACERTASTE!")
            opc = str(input("\nSi desea seguir jugando ingrese 1, si desea salir presione 0: "))
            while (opc!="0" and opc!="1"):
                opc = str(input("\nOpción inválida. Si desea seguir jugando ingrese 1, si desea salir presione 0: "))
        else:
            print("\n* NO ACERTASTE. El juego ha terminado :(")
            print ("\nEl jugador", nombre1, "acertó: ", cont, " veces\n")
            opc = "0"
        if (racha1<cont):
            racha1=cont
            
    input("\nPresione ENTER para volver al menú...")
            
        
def Juego2():
    global cont2
    global nombre2
    global perdidas2
    global ganadas2
    nombre2=input("\nIngrese el nombre del jugador: ")
    print("\n** ¡ Hola ", nombre2, "! En este juego la computadora va a pensar un número entre 1 y 100 y vos tenés seis intentos para adivinarlo.\n")
    
    opc="1"
    while (opc=="1"):
        numero1 = random.randint(1, 100)
        numero2=0        
        cont=0
        while (cont<6 and numero1!=numero2 ):
            a=0
            while(a==0):
                try:
                    numero2 = int( input("Ingrese un número entre 1 y 100: "))
                    while (numero2<1 or numero2>100):
                        numero2 = int(input("\nNúmero inválido. Ingrese un número entre 1 y 100:"))
                except ValueError:
                    print("\nNúmero inválido.")
                else:
                    a=1
                           
            cont+=1 
            if (numero1>numero2):
                print("\n:( - No le pegaste. Pista: el número secreto es mayor.")
                print("Te quedan ",6-cont," intentos.\n")
            elif (numero1<numero2):
                print("\n:( - No le pegaste. Pista: el número es menor.")
                print("Te quedan ",6-cont," intentos.\n")
    
        if (numero1==numero2):
            print("\n:D - ¡Ganaste!")
            print("Lo acertaste en el intento número: ",cont)
            ganadas2+=1
        else:
            print("\n:'( - Perdiste.")
            print("\nEl numero secreto es: ",numero1)
            perdidas2+=1

        cont2 = ganadas2 + perdidas2
        print("\nJugadas:", cont2)
        print("Perdidas:", perdidas2)
        print("Ganadas:", ganadas2)      
        
        opc = str(input("\nSi desea seguir jugando ingrese 1, si desea salir presione 0: "))
        while (opc!="0" and opc!="1"):
            opc = str(input("\nOpción inválida. Si desea seguir jugando ingrese 1, si desea salir presione 0: "))
            
    input("\nPresione ENTER para volver al menú...")

def Juego4():
    global cont4
    global nombre4
    global ganadas4
    global perdidas4
    aciertos = 0
    fallas = 0
    creditosTotal = 100    
    nombre4=input("\nIngrese el nombre del jugador: ")
    print("\n** ¡ Hola ", nombre4, "! En este juego la computadora va a lanzar dos dados y tenés que adivinar si la suma de éstos da un número par o impar.")
    print("\n* Tenes ",creditosTotal, "créditos virtuales para jugar.")
    opc = "1"
    while (opc=="1" and creditosTotal>0):
        cont4+=1
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        prediccion = ""
        creditos = 1
        while (prediccion!="par" and prediccion!="impar"):      
            prediccion = input("\n¿La suma de los dados será par o impar? Ingrese par o impar: ")
            a=0
            while(a==0):
                try:
                    creditos = int(input("Ingrese la cantidad de créditos virtuales que desea apostar: "))
                    while(creditos<=1 or creditos>creditosTotal):
                        creditos = int(input(f"Ingreso inválido. Tiene que ingresar un número entre 1 y {creditosTotal} : "))
                except ValueError:
                    print("\nNúmero inválido.")
                else:
                    a=1
        if ((suma % 2 == 0 and prediccion.lower() == "par") or (suma % 2 == 1 and prediccion.lower() == "impar")):
                creditosTotal = creditosTotal + creditos
                aciertos+=1
                print("\n:D ¡Acertaste!")
                print("\n** Tenes ", creditosTotal, "créditos virtuales acumulados.")
                print("** Llevas ", aciertos, "aciertos.")
        else:
            creditosTotal = creditosTotal - creditos
            fallas+=1
            print("\n:( Perdiste.")
            print("** Tenes ", creditosTotal, "créditos virtuales acumulados.")                             
            
        opc = str(input("\nSi desea seguir jugando ingrese 1, si desea salir presione 0: "))
        while (opc!="0" and opc!="1"):
            opc = str(input("\nOpción inválida. Si desea seguir jugando ingrese 1, si desea salir presione 0: "))
            
        if (creditosTotal==0 and opc=="1"):
            print("\n :( Lo siento, no te quedan más créditos para jugar. Perdiste la racha.")
            print("** Tuviste ", aciertos, " aciertos.")
    ganadas4 = ganadas4 + aciertos
    perdidas4 = perdidas4 + fallas
    input("\nPresione ENTER para volver al menú...")

    
def reporte():
    opc = " "
    while (opc!="V"):
        menuReporte()
        opc = str(input("\nIngrese su opción: ")).upper()
        while (opc<"A" or opc>"D" and opc!= "V"):
            opc = str(input("\nIngreso Invalido - reintente. Ingrese su opción: ")).upper()
        match opc:
            case "A": 
                print("   JUEGO         | CANT. DE VECES QUE JUGÓ |   JUGADOR/A   ")
                print("'Menor-mayor'    |           ", cont1,"           |  ", nombre1)
                print("'Número secreto' |           ", cont2,"           |  ", nombre2)
                print("'Par o impar'    |           ", cont4,"           |  ", nombre4)
            case "B": 
                print("La mayor racha alcanzada es de ", racha1, "aciertos.")
            case "C": 
                print("La cantidad de veces ganadas: ", ganadas2)
                print("La cantidad de veces perdidas: ", perdidas2)
            case "D": 
                print("La cantidad de veces ganadas: ", ganadas4)
                print("La cantidad de veces perdidas: ", perdidas4)
            case "V": input("\nVolviendo al menú principal. Presione ENTER.\n")
    
    
    
def cartel():
    print("-----------------------")
    print("....EN CONSTRUCCION...")
    print("------------------------")
    input("\nPresione ENTER para volver al menú...")

opc = " "
while (opc!="S"):
    MENU()
    opc = str(input("\nIngrese su opción: ")).upper()
    while (opc<"A" or opc>"E" and opc!= "S"):
        opc = str(input("\nIngreso Invalido - reintente. Ingrese su opción: ")).upper()
    match opc:
        case "A": Juego1()
        case "B": Juego2()
        case "C": cartel()
        case "D": Juego4()
        case "E": reporte()
        case "S": input("\nGracias por jugar. No apueste, juegue por diversión\n")
        
   
