class Cancion:
    #Todos los atributos son publicos

    artista = ''
    duracion = 0
    album = ''

    # tanto artista, duarcion, album como el titulo son iguales


    #Este es el contructor
    def __init__(self):

        #self solo hace la propiedad titulo como publica
        self.titulo = ''

    #_str_ es nuestro sobre carga de oparadores de cout <<c
    def __str__(self):
        return "Artista: " + self.artista + "\n" \
                "Album: " + self.album + "\n" \
                "Titulo: "+ self.titulo + "\n" \
                "Duracion: "+ str(self.duracion) + "sec"