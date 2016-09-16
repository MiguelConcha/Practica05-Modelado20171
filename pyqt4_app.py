import sys
import random
from PyQt4 import QtGui, QtCore
from datetime import *

class Ventana(QtGui.QMainWindow):
	def __init__(self):
		super().__init__()
		#Diccionario que servirá para que los personajes de la lucha independentista puedan variar; se accederá con enteros generados aleatoriamente.
		self.personajes = {1:"Juan Aldama", 2:"Ignacio Allende", 3: "Doña Josefa Ortíz",
						 4: "Miguel Hidalgo y Costilla", 5: "Jośe María Morelos y Pavón", 
					 	6: "Vicente Guerrero", 7: "Nicolás Bravo", 8: "Agustín de Iturbide", 9: "Epigmnio González",
					 	10: "Hermenegildo Galeana", 11: "José Mariano Michelena", 12: "Leona Vicario", 13: "Andrés Quintana Roo",
					 	14: "Servando Teresa de Mier", 15: "Miguel Barragán"}
		self.btn_aniv = None #Botón "Apriétame"
		self.btn_salir = None #Botón para salir del programa fácilmente.
		self.btb_reload = None #Botón para generar nuevos personajes.
		self.label = None #Texto con los personajes históricos.
		self.setGeometry(400,400, 2000, 500) #Estableciendo las dimensiones de la ventana que contiene todo.
		self.setWindowTitle("¡Viva México!") #Poniéndole el título.
		self.setWindowIcon(QtGui.QIcon("flag.png")) #Y el ícono.
		#Creando los botones con sus respectivas acciones y el label.
		self.make_characters_label()
		self.makebtn_reload()
		self.makebtn_aniv()
		self.makebtn_salir()

	'''Texto con la etiqueta con los personajes históricos.'''
	def make_characters_label(self):
		#Generando tres números aleatorios en el rango [1,15]
		random_numbers = random.sample(range(1, 15), 3)
		#Poniéndole el texto al label.
		content = "Personajes de la Independencia:\n1) " + self.personajes[random_numbers[0]] + "\n" + "2) " + self.personajes[random_numbers[1]] + "\n" + "3) " + self.personajes[random_numbers[2]]
		self.label = QtGui.QLabel(content, self) 
		#Finalmente, definiendo la fuente, su tamaño, el color del texto y el fondo; moviéndolo a donde debe ir.
		self.label.setFont(QtGui.QFont('Courier', 15))
		self.label.resize(self.label.sizeHint())
		self.label.setStyleSheet("QLabel { color : #9999ff; }")
		self.label.move(650, 70)

	'''Botón para generar nuevos personajes históricos y mostrarlos.'''
	def makebtn_reload(self):
		#Fijando el texto del botón y haciendo que se muestre.
		self.btn_aniv = QtGui.QPushButton('Otros ↺', self)
		#Definiendo la acción que ocurrirá en caso de ser pulsado.
		self.btn_aniv.clicked.connect(self.generate_new_chars)
		#Definiendo su fuente, tamaño y posición.
		self.btn_aniv.setFont(QtGui.QFont('SansSerif', 20))
		self.btn_aniv.resize(self.btn_aniv.sizeHint())
		self.btn_aniv.move(1500, 100)

	def generate_new_chars(self):
		#Generando tres números aleatorios nuevamente.
		random_numbers = random.sample(range(1, 15), 3)
		content = "Personajes de la Independencia:\n1) " + self.personajes[random_numbers[0]] + "\n" + "2) " + self.personajes[random_numbers[1]] + "\n" + "3) " + self.personajes[random_numbers[2]]
		#y cambiando el texto de la etiqueta para mostrar los nuevos personajes.
		self.label.setText(content)

	'''Botón para mostrar los días que faltan para el siguiente 15 de septiembre.'''
	def makebtn_aniv(self):
		#Fijando el texto del botón y haciendo que se muestre.
		self.btn_aniv = QtGui.QPushButton('Apriétame', self)
		self.btn_aniv.clicked.connect(self.dias)
		#Definiendo su fuente, tamaño y posición.
		self.btn_aniv.setFont(QtGui.QFont('SansSerif', 20))
		self.btn_aniv.resize(self.btn_aniv.sizeHint())
		self.btn_aniv.move(850, 300)
		
	'''Calcula los días para el próximo 15 de septiembre y cambia el texto del botón.'''
	def dias(self):
		#Se obtiene la información de la fecha actual.
		fecha_actual = date.today()
		dia = fecha_actual.day
		mes = fecha_actual.month
		actual = fecha_actual.year
		#y se crea una fecha que sirve para tener la información de la fecha del siguente 15. 
		fecha_futura = date(actual,9,15)
		#Si ya es septiebre y a partir del 15, se tendrán que calcular los días restantes para el 15 de septiembre del siguiente año.
		if mes >= 9 and dia >= 15:
			actual += 1
			fecha_futura = date(actual,9,15) #Se la suma una unidad al año de la fecha del futuro.
		regreso = (fecha_futura - fecha_actual).days
		#Estableciendo el color y fondo del botón, el nuevo texto, las dimensiones y la posición.
		self.btn_aniv.setStyleSheet('QPushButton {background-color: #336600; color: red;}')
		if regreso == 365: 
			self.btn_aniv.setText("¡¡¡HOY ES EL GRITO!!!") #Anunciando cuánto falta para el 15 de septiembre más cercano (si estamos a 15, faltan 365 días para el del siguiente y eso significa que hoy es 15).
			self.btn_aniv.move(650, 300)
		else:
			self.btn_aniv.setText("¡Faltan " + str(regreso) + " días para el 15 de septiembre de " + str(actual)) #Anunciando cuánto falta para el 15 de septiembre del próximo año.
			self.btn_aniv.move(250, 300)
		self.btn_aniv.resize(self.btn_aniv.sizeHint())

	def makebtn_salir(self):
		#Se define el texto del botón y se muestra.
		self.btn_salir = QtGui.QPushButton('Salir', self)
		self.btn_salir.clicked.connect(exit) #La acción es simplemente la de salir (exit), por lo que no se tiene que definir una función adicional para lograr ésto.
		#Se define la fuente del botón y su tamaño de letra, su dimensión y posición.
		self.btn_salir.setFont(QtGui.QFont('SansSerif', 10))
		self.btn_salir.resize(self.btn_salir.sizeHint())
		self.btn_salir.move(900, 400)		

if __name__ == "__main__":
	#Se crea la aplicación para poder inicializar el Widget de la Ventana, se muestra (con todo lo que tiene ésta) y esto ocurre mientras que no termine la ejecución del programa.
    app = QtGui.QApplication(sys.argv)
    myapp = Ventana()
    myapp.show()
    sys.exit(app.exec_())