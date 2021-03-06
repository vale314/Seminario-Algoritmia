from PySide2.QtCore import Slot
from particula import Particula
from capturador import Capturador
from disjoint_set import DisjointSet
from PySide2.QtWidgets import QMainWindow, QMessageBox,QFileDialog,QGraphicsScene
from ui_mainwindow import Ui_MainWindow
from PySide2.QtGui import QPen, QColor,QBrush
from queue import PriorityQueue
import pprint
import time

import json
#https://www.geeksforgeeks.org/python-program-for-bubble-sort/
import math

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scene = QGraphicsScene()
        #self.scene.setSceneRect(0,500)
        self.ui.graphicsView.setScene(self.scene)

        self.pen = QPen()
        self.pen.setColor(QColor(0, 0, 0))
        self.pen.setWidth(1)


        self.lista=[];
        self.listaMenor=[];
        self.grafoG = dict()
        self.grafoN = dict()
        self.pila=[]
        self.cola=[]
        self.visitados=[]
        self.capturador=Capturador()
        self.disjointSet=[]
        self.grafoKruskal = dict()

        self.ui.pushButton.clicked.connect(self.click)
        self.ui.pushButton_2.clicked.connect(self.mostrar)

        self.ui.actionGuardar.triggered.connect(self.guardar)
        self.ui.actionAbrir_2.triggered.connect(self.abrir)
        self.ui.actionMostar.triggered.connect(self.mostarParticulasPuntos)

        self.ui.actionPuntos_Cercanos.triggered.connect(self.puntos_cercanos)

        self.ui.pushButton_3.clicked.connect(self.ordenar_velocidad)

        self.ui.pushButton_4.clicked.connect(self.ordenar_distancia)

        self.ui.pushButton_5.clicked.connect(self.grafo)

        self.ui.pushButton_6.clicked.connect(self.rProfundidad)

        self.ui.pushButton_7.clicked.connect(self.rAnchura)

        self.ui.pushButton_8.clicked.connect(self.algoritmoPrim)

        self.ui.pushButton_9.clicked.connect(self.mostrarGrafo)

        self.ui.pushButton_10.clicked.connect(self.mostrarGrafoG)

        self.ui.actionkrustal.triggered.connect(self.kruskal)

        self.ui.actionDijkstra.triggered.connect(self.disjkstra)

        self.ui.actionCamino_Dijkstra.triggered.connect(self.camino_disjktra)

    @Slot()
    def camino_disjktra(self):
        origenX = int(self.ui.lineEdit_2.text())
        origenY = int(self.ui.lineEdit_6.text())

        destino=(origenX,origenY)
        print("Camino")

        siguiente=destino

        var=True
        caminoNew=[]
        caminoNew.append(destino)

        while var:
            for item in self.camino:
                if siguiente == item[0] and siguiente ==item[1]:
                    caminoNew.append(item[1])
                    var=False
                    break
                    return
                elif item[0] == siguiente:
                    caminoNew.append(item[1])
                    siguiente=item[1]

        nuev=caminoNew.pop()

        self.pen.setColor(QColor(0, 0, 0))
        self.pen.setWidth(3)
        while len(caminoNew)>0:
            dest=caminoNew.pop()
            self.scene.addLine(nuev[0], nuev[1], dest[0], dest[1], self.pen)
            print(nuev,dest)
            nuev=dest
        self.pen.setWidth(1)

    @Slot()
    def disjkstra(self):
        origenX = int(self.ui.lineEdit_2.text())
        origenY = int(self.ui.lineEdit_6.text())

        self.pq = PriorityQueue()
        self.disjointSet = []
        self.arregloDistancias=[]

        origen=(origenX,origenY)

        self.llenarGrafo();

        # obtenemos Todos los Nodos sin repetir en una lista disjointSet
        for particula in self.capturador.lista:
            if(particula.origenX==origenX and particula.origenY==origenY):
                self.pq.put([particula.distancia,((particula.origenX,particula.origenY),(particula.destinoX,particula.destinoY))])
            else:
                self.pq.put([9999,((particula.origenX, particula.origenY), (particula.destinoX, particula.destinoY))])

        self.llenarDisjointSet()
        #Fin

        #Tenemos Todos los minimos desde el orgien los demas que no hay conexion directa es su peso 9999
        '''for particula in self.capturador.lista:
            if (particula.origenX == origenX and particula.origenY == origenY):
                if particula not in  self.arregloDistancias:
                    self.arregloDistancias.append([(particula.destinoX, particula.destinoY),particula.distancia])
        '''
        self.arregloDistancias.append([origen,0])

        for item in self.disjointSet:
            if self.buscarEnArregloDistancia(item):
                self.arregloDistancias.append([item, 9999])

        print("Arreglo De Distancias")
        for item in self.arregloDistancias:
            print(item)

        #fin#

        #se crea un Camino
        self.camino = []
        for item in self.arregloDistancias:
            if item[0]==origen:
                self.camino.append((item[0],item[0]))
            else:
                self.camino.append((item[0],0))

        print("Camino")
        for item in self.camino:
            print(item)

        #se crea una lista ordenada y se agrega el origen con una distancia 0
        listaOrdenada=PriorityQueue()
        for item in self.arregloDistancias:
            if item[0] == origen:
                listaOrdenada.put([item[1],item[0]])

        #Miestras la Lista Ordenada no este vacia extraer el nodo revisar cada conexion del nodo
        while not listaOrdenada.empty():
            actual=listaOrdenada.get()
            print("Adyacentes----de-----")
            print(actual)
            for adyacentes in self.grafoG[actual[1]]:
                print("Adyacente")
                print(adyacentes)
                if self.buscarEnArregloDistancia(adyacentes[0])==False:
                    elem=self.obtenerElemEnArregloDistancia(adyacentes[0])
                    ori=self.obtenerElemEnArregloDistancia(actual[1])
                    if adyacentes[1]+ori[1] < elem[1]:
                        idx=0
                        for item in self.arregloDistancias:
                            if item[0] == adyacentes[0]:
                                self.arregloDistancias[idx]=((elem[0],adyacentes[1]+ori[1]))
                            idx=idx+1
                        '''
                            a el nodo elem[0] en su camino[elem[0]]:actual[1]
                            es un decir a el nodo que tenemos el elemento en su   
                        '''
                        idx = 0
                        for item in self.camino:
                            if item[0] == elem[0]:
                                self.camino[idx]=((item[0],actual[1]))
                            idx=idx+1
                        listaOrdenada.put([adyacentes[1]+ori[1],elem[0]])

            print("Camino New")
            for item in self.camino:
                print(item)
            print("arreglo distancias")
            for item in self.arregloDistancias:
                print(item)

    def obtenerElemEnArregloDistancia(self, item):
        for particula in self.arregloDistancias:
            print(particula)
        for particula in self.arregloDistancias:
            if item == particula[0]:
                return particula;
        return False;

    def buscarEnArregloDistancia(self,item):
        for particula in self.arregloDistancias:
            if item == particula[0]:
                return False;
        return True;

    @Slot()
    def kruskal(self):
        self.visitados = []
        self.grafoN = dict()
        self.llenarGrafo()
        self.pq = PriorityQueue()
        self.disjointSet= []
        self.grafoKruskal = dict()

        for particula in self.capturador.lista:
            self.pq.put([particula.distancia,((particula.origenX,particula.origenY),(particula.destinoX,particula.destinoY))])

        self.llenarDisjointSet()

        for particula in self.capturador.lista:
            self.pq.put([particula.distancia,((particula.origenX,particula.origenY),(particula.destinoX,particula.destinoY))])

        conjunto = DisjointSet(self.disjointSet)
        print(conjunto.get())

        while not self.pq.empty():
            actual=self.pq.get()

            if actual[1][0] not in conjunto.find(actual[1][1]):
                self.llenarGrafoKrustal(actual[1][0],actual[1][1],actual[0]);
                print(actual[1][0],actual[1][1])
                conjunto.union(actual[1][0],actual[1][1])

        self.mostrarGrafoG()

        self.pen.setWidth(3)
        for item in self.grafoKruskal.items():
            print(item)
            for item2 in item[1]:
                self.pen.setColor(QColor(0, 0, 0))
                self.scene.addLine(item[0][0],item[0][1],item2[0][0],item2[0][1], self.pen)
                print(item[0][0],item[0][1],item2[0][0],item2[0][1])
        self.pen.setWidth(1)


    def llenarDisjointSet(self):
        pqAux=self.pq

        while not pqAux.empty():
            actual=pqAux.get()
            #print(actual[1][0],actual[1][1])
            if actual[1][0] not in self.disjointSet:
                self.disjointSet.append(actual[1][0])
            if actual[1][1] not in self.disjointSet:
                self.disjointSet.append(actual[1][1])

    @Slot()
    def mostrarGrafoG(self):
        self.scene.clear()
        self.scene = QGraphicsScene()
        # self.scene.setSceneRect(0,500)
        self.ui.graphicsView.setScene(self.scene)

        self.pen = QPen()
        self.pen.setColor(QColor(0, 0, 0))
        self.pen.setWidth(1)
        self.capturador.ordenar_velocidad()
        for particula in self.capturador.lista:
            self.lista.append({
                'x':particula.origenX,
                'y':particula.origenY,
                'color':{
                    'red':particula.red,
                    'green':particula.green,
                    'blue':particula.blue
                }
            })
            self.lista.append({
                'x':particula.destinoX,
                'y':particula.destinoY,
                'color':{
                    'red':particula.red,
                    'green':particula.green,
                    'blue':particula.blue
                }
            })
            self.ui.plainTextEdit.insertPlainText(str(particula))
            self.pen.setColor(QColor(particula.red, particula.green, particula.blue))
            self.scene.addEllipse(particula.origenX, particula.origenY, 5, 5, self.pen, QBrush(QColor(particula.red, 10,particula.green, particula.blue)))
            self.scene.addLine(particula.origenX, particula.origenY, particula.destinoX, particula.destinoY,
                               self.pen)

    @Slot()
    def mostrarGrafo(self):
        str = pprint.pformat(self.grafoN, width=40)
        self.ui.plainTextEdit.insertPlainText(str)

        self.mostrarGrafoG()

        self.pen.setWidth(3)
        for origen in self.grafoN:
            for destino in self.grafoN[origen]:
                self.pen.setColor(QColor(0, 0, 0))
                self.scene.addLine(origen[0], origen[1], destino[0][0], destino[0][1],self.pen)
        self.pen.setWidth(1)
    @Slot()
    def algoritmoPrim(self):
        self.visitados=[]
        self.grafoN=dict()
        self.llenarGrafo()
        pq=PriorityQueue()
        origenX = int(self.ui.lineEdit_2.text())
        origenY = int(self.ui.lineEdit_6.text())

        origen=(origenX,origenY)

        self.visitados.append(origen)

        for actual in self.grafoG[origen]:
            pq.put([actual[1],(origen,actual[0])])
        #distancia, origen. Destino

        while not pq.empty():
            actual=pq.get()
            print("Actual")
            print(actual[1][1])

            if self.buscarPila(actual[1][1])==False:
                self.visitados.append(actual[1][1])

                print("Adyacentes")
                for adyacentes in self.grafoG[actual[1][1]]:
                    print(adyacentes[1],actual[1][1],adyacentes[0])
                    pq.put([adyacentes[1],(actual[1][1],adyacentes[0])])
                #NodoOrigen, NodoOrigen, Peso
                self.llenarGrafoPrim(actual[1][0],actual[1][1],actual[0])

    def llenarGrafoKrustal(self,origen,destino,distancia):
        if origen in self.grafoKruskal:
            self.grafoKruskal[origen].append((destino, distancia))
        else:
            self.grafoKruskal[origen] = [(destino, distancia)]
        if destino in self.grafoKruskal:
            self.grafoKruskal[destino].append((origen, distancia))
        else:
            self.grafoKruskal[destino] = [(origen, distancia)]


    def llenarGrafoPrim(self,origen,destino,distancia):
        if origen in self.grafoN:
            self.grafoN[origen].append((destino, distancia))
        else:
            self.grafoN[origen] = [(destino, distancia)]
        if destino in self.grafoN:
            self.grafoN[destino].append((origen, distancia))
        else:
            self.grafoN[destino] = [(origen, distancia)]

    def buscarPila(self,busqueda):
        for actual in self.visitados:
            if actual==busqueda:
                return True;
        return False;


    @Slot()
    def rAnchura(self):
        self.ui.plainTextEdit.clear()
        self.llenarGrafo()
        self.visitados=[]
        self.scene.clear()
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        origenX = int(self.ui.lineEdit_2.text())
        origenY = int(self.ui.lineEdit_6.text())
        self.cola.append((origenX,origenY))

        while len(self.cola)!=0:
            actual=self.cola[0]
            print(actual)
            self.cola.pop(0)
            print(actual)
            if self.buscarPila(actual)==False:
                self.visitados.append(actual)
                print(actual)
                str = pprint.pformat(actual)
                self.ui.plainTextEdit.insertPlainText(str+'\n')
                for vecino in self.grafoG[actual]:
                    if(self.buscarPila(vecino)==False):
                        self.cola.append(vecino[0])
    def llenarGrafo(self):
        self.grafoG=dict()
        for particula in self.capturador.lista:
            origen = (particula.origenX, particula.origenY)
            destino = (particula.destinoX, particula.destinoY)
            if origen in self.grafoG:
                self.grafoG[origen].append((destino, particula.distancia))
            else:
                self.grafoG[origen] = [(destino, particula.distancia)]
            if destino in self.grafoG:
                self.grafoG[destino].append((origen, particula.distancia))
            else:
                self.grafoG[destino] = [(origen, particula.distancia)]

    @Slot()
    def rProfundidad(self):
        self.ui.plainTextEdit.clear()
        self.llenarGrafo();
        self.visitados=[]
        self.scene.clear()
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        origenX = int(self.ui.lineEdit_2.text())
        origenY = int(self.ui.lineEdit_6.text())
        self.pila.append((origenX,origenY))

        while len(self.pila)!=0:
            actual=self.pila[len(self.pila)-1]
            self.pila.pop()
            if self.buscarPila(actual)==False:
                self.visitados.append(actual)
                print(actual)
                str = pprint.pformat(actual)
                self.ui.plainTextEdit.insertPlainText(str+'\n')
                for vecino in self.grafoG[actual]:
                    if(self.buscarPila(vecino)==False):
                        self.pila.append(vecino[0])


    @Slot()
    def grafo(self):
          # {}
        self.scene.clear()
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        for particula in self.capturador.lista:
            origen=(particula.origenX,particula.origenY)
            destino=(particula.destinoX,particula.destinoY)
            if origen in self.grafoG:
                self.grafoG[origen].append((destino, particula.distancia))
            else:
                self.grafoG[origen] = [(destino, particula.distancia)]
            if destino in self.grafoG:
                self.grafoG[destino].append((origen, particula.distancia))
            else:
                self.grafoG[destino] = [(origen, particula.distancia)]
        str = pprint.pformat(self.grafoG, width=40)
        self.ui.plainTextEdit.insertPlainText(str)

    @Slot()
    def puntos_cercanos(self):
        self.listaMenor=[]
        for i in range(len(self.lista)-1):
            particulaMenor=self.lista[i+1];

            for j in range(len(self.lista)-1):
                particula2=self.lista[j]
                if(j==0):
                    auxDistancia=math.sqrt(pow((int(particula2['x']) - int(particulaMenor['x'])), 2) + pow((int(particula2['y']) - int(particulaMenor['y'])), 2))
                    aux={'origen':particulaMenor,'destino':particula2}

                if((math.sqrt(pow((int(particula2['x'])-int(particulaMenor['x'])),2)+pow((int(particula2['y'])-int(particulaMenor['y'])),2))<auxDistancia)and(particulaMenor!=particula2)):
                    auxDistancia = math.sqrt(pow((int(particula2['x']) - int(particulaMenor['x'])), 2) + pow((int(particula2['y']) - int(particulaMenor['y'])), 2))
                    aux = {'origen': particulaMenor, 'destino': particula2}
            self.listaMenor.append(aux);
            self.dibujar();

    @Slot()
    def mostarParticulasPuntos(self):
        self.scene.clear()
        self.scene = QGraphicsScene()
        # self.scene.setSceneRect(0,500)
        self.ui.graphicsView.setScene(self.scene)

        self.pen = QPen()
        self.pen.setWidth(1)

        for particula in self.capturador.lista:

            print(particula.origenX,particula.origenY)
            ## Problema
            ## Si hay un nodo que no tenga origen solo nodos que van hacia el no se dibuja
            ## Soluccion
            ## comparar en un nueva lista si el destino se encuentra en la lista de origenes
            ## si no se encuentra dibujar

            ##posible solucion
            self.scene.addEllipse(particula.destinoX, particula.destinoY, 5, 5, self.pen, QBrush(QColor(particula.red, particula.green, particula.blue)))
            self.scene.addEllipse(particula.origenX, particula.origenY, 5, 5, self.pen, QBrush(QColor(particula.red,particula.green, particula.blue)))

            self.ui.plainTextEdit.insertPlainText(str(particula))
            self.lista.append({
                'x':particula.origenX,
                'y':particula.origenY,
                'color':{
                    'red':particula.red,
                    'green':particula.green,
                    'blue':particula.blue
                }
            })
            self.lista.append({
                'x':particula.destinoX,
                'y':particula.destinoY,
                'color':{
                    'red':particula.red,
                    'green':particula.green,
                    'blue':particula.blue
                }
            })

    @Slot()
    def ordenar_velocidad(self):
        self.scene.clear()
        self.scene = QGraphicsScene()
        #self.scene.setSceneRect(0,500)
        self.ui.graphicsView.setScene(self.scene)

        self.pen = QPen()
        self.pen.setColor(QColor(0, 0, 0))
        self.pen.setWidth(1)
        self.capturador.ordenar_velocidad()
        y=0
        for particula in self.capturador.lista:
            self.ui.plainTextEdit.insertPlainText(str(particula))
            self.pen.setColor(QColor(particula.red, particula.green, particula.blue))
            self.scene.addLine(0, y, particula.distancia, y, self.pen)
            y=y+2

    def dibujar(self):
        self.scene.clear()
        self.scene = QGraphicsScene()
        # self.scene.setSceneRect(0,500)
        self.ui.graphicsView.setScene(self.scene)

        self.pen = QPen()
        self.pen.setColor(QColor(0, 0, 0))
        self.pen.setWidth(1)
        self.capturador.ordenar_distancia()

        for new in self.listaMenor:
            self.scene.addEllipse(new['origen']['x'], new['origen']['y'], 5, 5, self.pen,QBrush(QColor(new['origen']['color']['red'], 10, new['origen']['color']['green'], new['origen']['color']['blue'])))
            self.pen.setColor(QColor(new['origen']['color']['red'], new['origen']['color']['green'], new['origen']['color']['blue']))
            self.scene.addLine(new['origen']['x'], new['origen']['y'], new['destino']['x'], new['destino']['y'], self.pen)

    @Slot()
    def ordenar_distancia(self):
        self.scene.clear()
        self.scene = QGraphicsScene()
        #self.scene.setSceneRect(0,500)
        self.ui.graphicsView.setScene(self.scene)

        self.pen = QPen()
        self.pen.setColor(QColor(0, 0, 0))
        self.pen.setWidth(1)
        self.capturador.ordenar_distancia()
        y=0
        for particula in self.capturador.lista:
            self.ui.plainTextEdit.insertPlainText(str(particula))
            self.pen.setColor(QColor(particula.red, particula.green, particula.blue))
            self.scene.addLine(0, y, particula.distancia, y, self.pen)
            y=y+2


    @Slot()
    def guardar(self):
        self.scene = QGraphicsScene()
        #self.scene.setSceneRect(0,500)
        self.ui.graphicsView.setScene(self.scene)

        self.pen = QPen()
        self.pen.setColor(QColor(0, 0, 0))
        self.pen.setWidth(1)
        file= QFileDialog.getSaveFileName(self, 'Guardar archivo...', '.', 'JSON (*.json)')
        print(file)
        self.capturador.guardar(file[0],self.pen,self.scene)

    @Slot()
    def abrir(self):
        file= QFileDialog.getOpenFileName(self, 'Abrir archivo', '.', 'JSON (*.json)')
        self.capturador.recuperar(file[0])

    @Slot()
    def mostrar(self):
        self.scene.clear()
        self.scene.addLine(0, 0, 499, 0, self.pen)
        y=0
        for particula in self.capturador.lista:
            self.ui.plainTextEdit.insertPlainText(str(particula))
            self.pen.setColor(QColor(particula.red, particula.green, particula.blue))
            self.scene.addLine(0, y, particula.distancia, y, self.pen)
            y=y+2


    @Slot()
    def click(self):

        id=self.ui.lineEdit.text()
        origenX=self.ui.lineEdit_2.text()
        origenY=self.ui.lineEdit_6.text()
        destinoX=self.ui.lineEdit_3.text()
        destinoY=self.ui.lineEdit_7.text()
        velocidad=self.ui.lineEdit_4.text()
        red=self.ui.lineEdit_5.text()
        green=self.ui.lineEdit_8.text()
        blue=self.ui.lineEdit_9.text()

        print(id, origenX, origenY,destinoX, destinoY, velocidad, red, green, blue)

        partiula=Particula()
        partiula.id= id
        partiula.origenX=int(origenX)
        partiula.origenY=int(origenY)
        partiula.destinoX=int(destinoX)
        partiula.destinoY=int(destinoY)
        partiula.distancia=math.sqrt(pow((int(destinoX)-int(origenX)),2)+pow((int(destinoY)-int(origenY)),2))
        partiula.red=int(red)
        partiula.green=int(green)
        partiula.blue=int(blue)
        partiula.velocidad=int(velocidad)


        self.capturador.agregar(partiula)

        msg=QMessageBox.information(self, 'Exito', 'Se agrego paquete con exito') #Ventana de mensaje de la libreria QMessageBox

        self.ui.lineEdit.clear()   #Limpiar campos
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_8.clear()
        self.ui.lineEdit_9.clear()