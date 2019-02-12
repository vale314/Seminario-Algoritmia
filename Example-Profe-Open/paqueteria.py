import json
from paquete import  Paquete

class Paqueteria:
    def __init__(self):
        self.lista=[]

    def agregar(self, paquete):
        self.lista.append(paquete)

    def mostrar(self):
        for paquete in self.lista:
            print(paquete)

    def guardar(self,file):
        lista_dicc =[]
        for paquete in self.lista:
            lista_dicc.append(paquete.to_dict())
        with open(file,'w') as archivo:
            json.dump(lista_dicc,archivo,indent=5)
            #for paquete in self.lista:
            #    archivo.write(str(paquete.to_dict()))


    def recuperar(self,file):
        with open(file,'r') as archivo:
            paquetes = json.load(archivo)

            for paquete in paquetes:
                p= Paquete()
                p.id = paquete['id']
                p.origen = paquete['origen']
                p.destino = paquete['destino']
                p.distancia = paquete['distancia']
                p.peso = paquete['peso']

                self.lista.append(p)