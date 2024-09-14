#Ejercicio 5: Días de la semana
#Escribe un programa que, dado un número del 1 al 7, imprima el día correspondiente de la
#semana usando match .
#Enunciado:
#Solicita al usuario un número del 1 al 7 y muestra el día de la semana correspondiente (1 = Lunes,
#7 = Domingo).

# Solicitar al usuario que ingrese un número del 1 al 7
numero = int(input("Inserte un número del 1 al 7: "))

# Usar match para determinar el día de la semana


match numero:
    case 1:
        dia = "Lunes"
    case 2:
        dia = "Martes"
    case 3:
        dia = "Miércoles"
    case 4:
        dia = "Jueves"
    case 5:
        dia = "Viernes"
    case 6:
        dia = "Sábado"
    case 7:
        dia = "Domingo"
    case _:
        dia = "introdece un numero. Debe ser del 1 al 7."

        

if (numero>=8 or numero<=0):
    print ("el valor es invalido")
    
else:
    print(f"hoy es {dia}")



