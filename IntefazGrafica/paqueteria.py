class Paqueteria:
    def __init__(self):
        self.lista=[]

    def agregar(self, paquete):
        self.lista.append(paquete)

    def mostrar(self):
        for paquete in self.lista:
            print(paquete)