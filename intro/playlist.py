class PlayList:
    def __init__(self):
        self.lista = []

    def agregar(self,cancion):
        self.lista.append(cancion)
        #append es como el push

    def mostrar(self):
        for cancion in self.lista:
            print(cancion)