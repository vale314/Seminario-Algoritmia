import json
from particula import Particula
import math

class Capturador:
    def __init__(self):
        self.lista=[]

    def agregar(self, particula):
        self.lista.append(particula)

    def mostrar(self):

        for particula in self.lista:
            print(particula)

    def guardar(self, file,pen,scene):
        scene.addLine(0, 0, 499, 0, pen)
        lista_dicc = []
        for particula in self.lista:
            lista_dicc.append(particula.to_dicc())

        with open(file, 'w') as archivo:
           json.dump(lista_dicc, archivo, indent=5)


    def recuperar(self, file):
        with open(file, 'r') as archivo:
            particulas= json.load(archivo)

            for particula in particulas:
                p = Particula()
                p.id = particula['id']
                p.origenX = particula['origen']['x']
                p.origenY = particula['origen']['y']
                p.destinoX = particula['destino']['x']
                p.destinoY = particula['destino']['y']
                p.distancia = math.sqrt(pow((int(p.destinoX)-int(p.origenX)),2)+pow((int(p.destinoY)-int(p.origenY)),2))
                p.velocidad = particula['velocidad']
                p.red = particula['color']['red']
                p.green = particula['color']['green']
                p.blue = particula['color']['blue']
                self.lista.append(p)

    def ordenar_velocidad(self):
        self.lista.sort()

    def ordenarDistancia(self,particula):
        return int(particula.distancia)

    def ordenar_distancia(self):
        #,reverse=TRUE
        self.lista.sort(key=self.ordenarDistancia,reverse=True)