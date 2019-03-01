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
    ##less to
    def __lt__(self, other):
        return self.origen < other.origen
    #__gt__ greater to

    def to_dict(self):
        return {'id': self.id,
                'origen': self.origen,
                'destino':  self.destino,
                'distancia': self.destino,
                'peso': self.peso}