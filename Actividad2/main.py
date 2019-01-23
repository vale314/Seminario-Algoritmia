





def menuAreas():
    opc=0
    while (opc!=4):
        print("Calculo de areas\n1 Triangulo\n2 Circulo\n3 Cuadrado\n4 Salir")
        opc=int(input());

        if(opc==1):
            print('Area de Triangulo equilatero')
            lado = input('Escribe el lado')
            lado = int(lado)
            area= (lado*lado)/2
            print('El area del Triangulo es. \n', area)
        elif(opc==2):
            print('Area de Circulo')
            lado=input('Ingrese su radio')
            lado= int(lado)
            lado= (3.14*(lado*lado))
            print('Su araea es \n', lado)
        elif(opc==3):
            print('Area de Cuadrado')
            lado= input('Ingrese su Lado')
            lado= int(lado)
            lado=lado*lado
            print('Su Area Es ', lado)
        elif(opc>4 or opc<1):
            print("Lap opcion que seleccionaste es incorrecta\n")

def signoDelZodiaco(dia,mes):
    
    if (dia >= 21 or dia <= 20) and (mes == 3 or mes == 4):
        signo = 'Aries'
        return signo
    elif (dia >= 21 or dia <= 21) and (mes == 4 or mes == 5):
        signo = 'Tauro'
        return signo
    elif (dia >= 22 or dia <= 22) and (mes == 6 or mes == 7):
        signo = 'Cancer'
        return signo
    elif (dia >= 22 or dia <= 21) and (mes == 5 or mes == 6):
        signo = 'Geminis'
        return signo
    elif (dia >= 24 or dia <= 23) and (mes == 9 or mes == 10):
        signo = 'Libra'
        return signo
    elif (dia >= 23 or dia <= 23) and (mes == 7 or mes == 8):
        signo = 'Leo'
        return signo
    elif (dia >= 24 or dia <= 23) and (mes == 8 or mes == 9):
        signo = 'Virgo'
        return signo
    elif (dia >= 24 or dia <= 22) and (mes == 10 or mes == 11):
        signo = 'Escorpio'
        return signo
    elif (dia >= 21 or dia <= 18) and (mes == 1 or mes == 2):
        signo = 'Acuario'
        return signo
    elif (dia >= 23 or dia <= 21) and (mes == 11 or mes == 12):
        signo = 'Sagitario'
        return signo
    elif (dia >= 22 or dia <= 20) and (mes == 1 or mes == 12):
        signo = 'Capricornio'
        return signo
    elif (dia >= 19 or dia <= 20) and (mes == 2 or mes == 3):
        signo = 'Piscis'
        return signo

def menuZodiacal():
    opc=0
    while(opc!=2):
        print("Ingrese su Dia")
        dia=int(input())
        print("Ingrese su Mes")
        mes=int(input())
        print("Tu Eres: "+ signoDelZodiaco(dia,mes))

        print("Deseas Salir 2\n")
        opc=int(input())

def menu():
    opc=0;
    while(opc !=3):

        print("Ingrese Su Opcion\n\n\n")
        print("1 Areas\n2 Signo\n3 Salir\n")
        opc=int(input())
        if(opc==1):
          menuAreas()
        elif(opc==2):
            menuZodiacal()
        elif(opc<1 or opc>3):
            print("Incorrecto\n")
menu()