import math
class Particula:
    def __init__(self):
        self.id=0
        self.origenX= 0
        self.origenY=0
        self.destinoX= 0
        self.destinoY=0
        self.distancia=0
        self.velocidad=0
        self.red=0
        self.green=0
        self.blue=0

    def __str__(self):#Sobrecarga

        return "id: " + str(self.id) + '\n' + \
            'origenX: ' + str(self.origenX) + '\n' + \
            'origenY: ' + str(self.origenY) + '\n' + \
            'destinoX: ' + str(self.destinoX) + '\n' + \
            'destinoY: ' + str(self.destinoY) + '\n' + \
            'distancia: ' + str(self.distancia) + '\n' + \
            'velocidad: ' + str(self.velocidad) + '\n' + \
            'RED: '+ str(self.red) +'\n' + \
            'GREEN: ' + str(self.green) + '\n' + \
            'BLUE: ' + str(self.blue) + '\n'

    def to_dicc(self):#diccionario
        return {'id': self.id,
                'origen':{
                    "x":self.origenX,
                    "y": self.origenY
                },
                "destino":{
                    'x': self.destinoX,
                    'y': self.destinoY,
                },
                'distancia': self.distancia,
                'velocidad': self.velocidad,
                "color":{
                    'red': self.red,
                    'green': self.green,
                    'blue': self.blue
                }
               }