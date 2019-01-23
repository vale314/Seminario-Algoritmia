# nombre = input('Escribe tu nombre: ')
# # edad es de tipo string
# edad = input('Escribe Tu Edad: ')
# # edad se realiza un cast a tipo int
# edad = int(edad)
#
# if edad>= 18:
#     print('Ya puedes votar')
# else:
#     print('Aun no puedes votar')
#
# print('Hola Mundo', nombre)
# print('vas a cumplir', edad+1 , '\n')
#
# print('Area de Triangulo equilatero')
# lado = input('Escribe el lado')
# lado = int(lado)
# area= (lado*lado)/2
#
# print('El area del Triangulo es. \n', area)
#
#
# print('Area de Circulo')
# lado=input('Ingrese su radio')
# lado= int(lado)
# lado= (3.14*(lado*lado))
# print('Su araea es \n', lado)
#
# print('Area de Cuadrado')
# lado= input('Ingrese su Lado')
# lado= int(lado)
# lado=lado*lado
# print('Su Area Es ', lado)


#Comentar varias linreeas de codigo es ctrl /


# temp = int(input('Temperatura: '))
#
# if temp > -10 and temp < 0:
#     print('Helado ')
# elif temp >= 0 and temp < 14:
#     print('Frio')
# elif temp >=14 and temp < 24:
#     print('Templado')
# elif temp >= 24:
#     print('Caluroso')


# ano= int(input('Ingresa el año'))
#
# if ano >= 3 and ano <=6:
#     if ano == 3:
#         dia = int(input('Ingresa el dia'))
#         if(dia >=21):
#             print('Primavera\n')
#         else:
#             print('Invierno\n')
#     elif ano == 4 or 5:
#         print('Primavera\n')
#     elif ano == 6:
#         dia = int(input('Ingresa el dia'))
#         if(dia <= 21):
#             print('Primavera\n')
#         else:
#             print('Verano\n')
# elif ano >=6 and ano <=9:
#     if ano == 7 or ano == 8:
#         print('Verano')
#     elif ano == 9:
#         dia = int(input('Ingresa el dia'))
#         if(dia>=21):
#             print('Otoño')
#         else:
#             print('Verano')
#


# i= 0
# while i < 10
#     print(i)
#     i = i+1

#      incia en 0 hasta el 10 e incrementa de 2 en 2
# lista = [10, 'Michael', 2, ['a',1,'abc']]
# for i in range(0,10,2):
#     print(i)

# for i in lista:
#     print(i)

# i=0
# while i <len(lista):
#     print(lista[i])
#     i=i+1


# def mostrar(s="Hello", n=2):
#     for i in range (0, n):
#         print(s)
#
# mostrar('Michael', 4)



from cancion import  Cancion
from  playlist import PlayList

l = PlayList()

while True:
    print('1 Agregar Cancion')
    print('2 Mostrar Cnaciones')
    print('0 Salir')
    op = input()

    if op == '1':
        cancion = Cancion()
        cancion.artista = input("Artista")
        cancion.album = input("Album")
        cancion.titulo = input("Titulo")
        cancion.duracion = int(input("Duaracion"))
        l.agregar(cancion)
    elif op == '2':
        l.mostrar()
        pass
    elif op =='0':
        break
