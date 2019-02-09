class Capturador:
    def __init__(self):
        self.lista=[]

    def agregar(self, particula):
        self.lista.append(particula)

    def mostrar(self):
        for particula in self.lista:
            print(particula)

    def guardar(self,file):
        with open(file,'w') as archivo:
            for particula in self.lista:
                archivo.write(str(particula))