import pprint
grafo = dict() #{}

while True:
    print('1 Crear Conexión')
    print('2 Mostrar Grafo')
    print('0 Salir')

    op = input(': ')

    if op == '1':
        origen= input('origen: ').upper()
        destino = input('Destino: ').upper()
        peso = int(input('Peso: '))

        if origen in grafo:
            grafo[origen].append((destino,peso))
        else:
            grafo[origen] = [(destino,peso)]
        if destino in grafo:
            grafo[destino].append((origen,peso))
        else:
            grafo[destino] = [(origen,peso)]
    elif op == '2':
        #pprint.pprint(grafo,width=40)
        str = pprint.pformat(grafo,width=40)
        print(str)
    elif op == '0':
        break

grafo['A'] = [('B',10),('C',2)]
grafo['B'] = [('A',10)]
grafo['C'] = [('A',2)]

pprint.pprint(grafo,width=40)