#Ejercicio 4: Determinación del tipo de triángulo
#Escribe un programa que determine el tipo de triángulo en función de sus lados usando if .
#Enunciado:
#Solicita al usuario que ingrese las longitudes de los tres lados de un triángulo. Determina si el
#triángulo es equilátero, isósceles o escaleno.

#ingresamos los numeros de los triangulos para saber sus medidas y poder identificar si son equilatero(tres lados de la misma medida )
#sis on dos lados iguaoles seria (isoseles) y si ninguno tiene coincidencia seria escaleno 
lado1= int (input("ingrese numero del triangulo: "))
lado2= int (input("ingrese numero del triangulo: "))
lado3= int (input("ingrese numero del triangulo: "))
#AHORA CON EL IF LO QUE HAREMOS ES DEFINIR QUE TIPOS SON 

if (lado1==lado2==lado3):
    print("el triangulo es equilatero")

else:
    print("es escaleno")

if (lado1==lado2 and lado3):
    print("el triangulo es isoceles: ")

