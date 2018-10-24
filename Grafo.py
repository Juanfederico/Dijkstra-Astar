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
		verticesRecorridos = {}
		verticesRestantes = self.listaVertices.copy() #Creo una copia del diccionario sobre el que voy a quitar elementos
		#del verticesRestantes[verticeInicial.obtenerEtiqueta()] #Elimino el nodo que se toma como inicial de la lista de pendientes
		primerVecinoIterado = None #Por defecto
		iterado = False #Por defecto

		while len(verticesRestantes)!=0:
			for vecino in verticeIndice.obtenerConexiones(): #El diccionario auxiliar (sin el nodo inicial)
				#print(vecino)
				#print(verticesRecorridos.keys())
				if ((not iterado) and (vecino.obtenerEtiqueta() not in verticesRecorridos)):
					primerVecinoIterado = vecino
					iterado = True
				distanciaActual = verticeIndice.obtenerDistancia()+verticeIndice.obtenerPeso(vecino) #Suma del total del recorrido (los pesos)
				if distanciaActual < vecino.obtenerDistancia():
					vecino.setearDistancia(distanciaActual)
					vecino.setearVerticeAnterior(verticeIndice) #Dejando una referencia del min/max anterior para saber el camino
			if(iterado==True):
				verticesRecorridos[verticeIndice.obtenerEtiqueta()] = verticeIndice
				del verticesRestantes[verticeIndice.obtenerEtiqueta()]
				verticeIndice = primerVecinoIterado
			else: break
			iterado = False
			#print(verticeIndice.obtenerEtiqueta())
			#print(len(verticesRestantes))
		print("mostrando-----------------------------------------------------------------------------------")
		for vertice in self.obtenerVertices():
			print("Etiqueta: " + str(self.listaVertices[vertice].obtenerEtiqueta()))
			print("Distancia: " + str(self.listaVertices[vertice].obtenerDistancia()))

		verticeFinal = self.obtenerVertice(6)
		self.obtenerMejorCamino(verticeInicial, verticeFinal)
		print("camino-------------------------------------------------------------------------------------")
		self.mostrarMejorCamino()

		#FUNCIONA BIENNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN HAY QUE ARREGLARLO UN POCO




	"""def dijkstra(self, verticeInicial):
		verticesRecorridos = []
		verticesRecorridos.append(verticeInicial)
		verticesRestantes = self.listaVertices.copy() #Creo una copia del diccionario sobre el que voy a quitar elementos
		del verticesRestantes[verticeInicial.obtenerEtiqueta()] #Elimino el nodo que se toma como inicial de la lista de pendientes
		while len(verticesRestantes)!=0:
			for vertice in verticesRecorridos.values(): #El diccionario auxiliar (sin el nodo inicial)
				for vecino in vertice.obtenerConexiones():
					verticesRecorridosAux = verticesRecorridos.copy()
					distanciaActual = vertice.obtenerDistancia()+vertice.obtenerPeso(vecino) #Suma del total del recorrido (los pesos)
					if distanciaActual < vecino.obtenerDistancia():
						vecino.setearDistancia(distanciaActual)
					verticesRecorridos.update(vecino)
					#verticesRecorridos[vecino.obtenerEtiqueta()] = vecino
					print(len(verticesRecorridos))

		print("Vertices recorridos: " + str(len(verticesRecorridos)))
		for vertice in verticesRecorridos.values():
			print (vertice.obtenerDistancia())"""
				





#for vecino in verticesRestantes.values():
#print(str(verticesRestantes.items()))
#print(self.listaVertices.keys())
#print(verticesRestantes[vertice].conectadoA[vecino])