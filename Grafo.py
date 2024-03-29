import math
from Vertice import Vertice

class Grafo:
	def __init__(self):
		self.listaVertices = {}
		self.numVertices = 0
		self.mejorCaminoActual = []

	def agregarVertice(self, etiqueta, distancia=0, heuristica=0, posX=0, posY=0):
		self.numVertices += 1
		nuevoVertice = Vertice(etiqueta, distancia, heuristica, posX=posX, posY=posY)
		self.listaVertices[etiqueta] = nuevoVertice
		return nuevoVertice

	def obtenerVertice(self, etiqueta):
		if etiqueta in self.listaVertices:
			return self.listaVertices[etiqueta]
		else:
			return None

	def buscarVertice(self, posX, posY):
		verticeEncontrado = None
		for etiqueta in self.listaVertices:
			if((self.listaVertices[etiqueta].posX == posX) and (self.listaVertices[etiqueta].posY == posY)):
				verticeEncontrado = self.listaVertices[etiqueta]
		return verticeEncontrado

	def __contains__(self, etiqueta):
		return etiqueta in self.listaVertices

	def agregarArista(self, desde, hasta, peso):
		if desde not in self.listaVertices:
			nv = self.agregarVertice(desde)
		if hasta not in self.listaVertices:
			nv = self.agregarVertice(hasta)
		self.listaVertices[desde].agregarVecino(self.listaVertices[hasta], peso)

	def obtenerVertices(self):
		return self.listaVertices.keys()

	def limpiarMejorCamino(self):
		self.mejorCaminoActual = []

	#recursivo
	def obtenerMejorCamino(self, verticeOrigen, verticeDestino): #Primero se debe ejecutar dijkstra o A*
		#Se podria tambien hacer todo en este metodo (calcular el dijkstra y ver el mejor camino de un nodo a otro)
		if(verticeDestino.obtenerVerticeAnterior() is not None):
			self.obtenerMejorCamino(verticeOrigen, verticeDestino.obtenerVerticeAnterior())
			self.mejorCaminoActual.append(verticeDestino)
		else:
			self.mejorCaminoActual.insert(0, verticeOrigen)

	def mostrarMejorCamino(self):
		for i, vertice in enumerate(self.mejorCaminoActual):
			print("--------------- Paso: " + str(i) + " ---------------")
			print("Etiqueta: " + str(vertice.obtenerEtiqueta()))
			print("Distancia hasta el momento: " + str(vertice.obtenerDistancia()))
			if(i==len(self.mejorCaminoActual)-1): 
				print("--------------- Final (distancia total=" + str(vertice.obtenerDistancia()) + ") ---------------")


	def __iter__(self):
		return iter(self.listaVertices.values())

	def dijkstra(self, verticeInicial):
		verticeIndice = verticeInicial
		listaPrioridad = [] #Se agregan por prioridad los vecinos de los nodos analizados; es una pila (FIFO)
		verticesRestantes = self.listaVertices.copy() #Creo una copia del diccionario sobre el que voy a quitar elementos
		#del verticesRestantes[verticeInicial.obtenerEtiqueta()] #Elimino el nodo que se toma como inicial de la lista de pendientes
		primerVecinoIterado = None #Por defecto
		while len(verticesRestantes)!=0:
			for vecino in verticeIndice.obtenerConexiones(): #El diccionario auxiliar (sin el nodo inicial)
				if (vecino.obtenerEtiqueta() in verticesRestantes):
					listaPrioridad.insert(0, vecino)
				distanciaActual = verticeIndice.obtenerDistancia()+verticeIndice.obtenerPeso(vecino) #Suma del total del recorrido (los pesos)
				if distanciaActual < vecino.obtenerDistancia():
					vecino.setearDistancia(distanciaActual)
					vecino.setearVerticeAnterior(verticeIndice) #Dejando una referencia del min/max anterior para saber el camino
			if(verticeIndice.obtenerEtiqueta() in verticesRestantes): del verticesRestantes[verticeIndice.obtenerEtiqueta()]
			if(len(listaPrioridad)!=0): 
				verticeIndice = listaPrioridad[0]
				del listaPrioridad[0]
		print("Fin de la ejecucion")
		#print("mostrando-----------------------------------------------------------------------------------")
		#for vertice in self.obtenerVertices():
		#	print("Etiqueta: " + str(self.listaVertices[vertice].obtenerEtiqueta()))
		#	print("Distancia: " + str(self.listaVertices[vertice].obtenerDistancia()))

	def astar(self, verticeComienzo, verticeDestino):
		listaAbierta = [verticeComienzo]
		listaCerrada = []
		verticeIndice = verticeComienzo
		#Comienza algoritmo
		#while(verticeIndice.obtenerEtiqueta()!=verticeDestino.obtenerEtiqueta()):
		while(verticeDestino not in listaCerrada):
			listaAbierta.remove(verticeIndice)
			listaCerrada.append(verticeIndice)
			if verticeDestino not in listaCerrada:
				for vecino in verticeIndice.obtenerConexiones():
					#vecino.setearVerticeAnterior(verticeIndice) #Lo apunto como nodo padre
					for item in listaAbierta:
						if(vecino.obtenerEtiqueta()==item.obtenerEtiqueta()):
							#verticeIndice.valorFuncion(verticeDestino)
							coste = verticeIndice.setearValorFuncion(verticeDestino) + vecino.setearValorFuncion(verticeDestino)
							if(item.setearValorFuncion(verticeDestino)>coste):
								item.setearVerticeAnterior(verticeIndice)
					if vecino not in listaAbierta and vecino not in listaCerrada:
						vecino.setearVerticeAnterior(verticeIndice) #Agrego el padre del vertice
						vecino.setearValorFuncion(verticeDestino) #Calculo el valor de la funcion
						listaAbierta.append(vecino)
				verticeIndice = self.obtenerMinimoVertice(listaAbierta, listaCerrada)
		print("Fin de la ejecucion")

	def mostrarMejorCaminoAstar(self, verticeOrigen, verticeDestino):
		listaCamino = [] #Lista ordenada del camino hacia el destino
		verticeIndice = verticeDestino
		contadorCamino = 0
		while(verticeOrigen.obtenerEtiqueta() not in listaCamino):
			listaCamino.insert(0, verticeIndice.obtenerEtiqueta())
			contadorCamino += 1
			verticeIndice = verticeIndice.obtenerVerticeAnterior()
		print("Distancia total: " + str(len(listaCamino)-1)) #-1 Porque no se cuenta desde donde arranca (la lista incluye al elemento inicial)
		return listaCamino

	def obtenerMinimoVertice(self, listaVertices, listaRestriccion):
		verticeMin = None
		funcionMin = float('inf')
		contadorVeces = 0
		for vertice in listaVertices:
			if(vertice.valorFuncion<funcionMin and vertice not in listaRestriccion):
				funcionMin = vertice.valorFuncion
				verticeMin = vertice
			if contadorVeces>0: 
				None
				#print("Entro mas de 1 vez, valor funcion: " + str(vertice.valorFuncion))
				#print("Valor de funcion minima: " + str(verticeMin.valorFuncion))
			contadorVeces+=1
		#if verticeMin is not None: print("valor: " + str(verticeMin.obtenerEtiqueta()))
		#print("end for--------------")
		return verticeMin



