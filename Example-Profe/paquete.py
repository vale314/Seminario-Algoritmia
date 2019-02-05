class Paquete:
    def __init__(self):
        self.id= ''
        self.origen= ''
        self.destino= ''
        self.distancia=0
        self.peso=0

    def __str__(self):#Sobrecarga
        return "id: " + self.id + '\n' + \
            'origen: ' + self.origen + '\n' + \
            'destino: ' + self.destino + '\n' + \
            'distancia: ' + str(self.distancia) + '\n' + \
            'peso: ' + str(self.peso) + '\n'
