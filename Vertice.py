class Vertice:
	def __init__(self, etiqueta, distancia=0, heuristica=0, verticeAnterior=None, posX=0, posY=0):
		self.etiqueta = etiqueta
		self.posX = posX
		self.posY = posY
		self.distancia = distancia #Utilizada para medir caminos minimos o maximos con Dijkstra
		self.heuristica = heuristica #Utilizada para medir caminos minimos o maximos con A* o A estrella
		self.conectadoA = {}
		self.valorFuncion = 0 #Para persistir en a* (contiene la suma del peso con la heuristica determinada, default 0)
		#Variables para recorridos como dijkstra o a*
		self.verticeAnterior = verticeAnterior #El anterior en el recorrido minimo/maximo con dijkstra o a*

	def agregarVecino(self, vecino, ponderacion=0):
		self.conectadoA[vecino] = ponderacion

	def __str__(self):
		return "Nodo " + str(self.etiqueta) + " conectado A: " + str([x.etiqueta for x in self.conectadoA])

	def obtenerConexiones(self): #Devuelve los vertices vecinos
		return self.conectadoA.keys()

	def obtenerVecinos(self): #Devuelve los pesos de vertices vecinos
		return self.conectadoA.values()

	def obtenerEtiqueta(self):
		return self.etiqueta

	def obtenerX(self):
		return self.posX

	def obtenerY(self):
		return self.posY

	def obtenerDistancia(self):
		return self.distancia

	def setearDistancia(self, distancia):
		self.distancia = distancia

	def obtenerVerticeAnterior(self):
		return self.verticeAnterior

	def setearVerticeAnterior(self, verticeAnterior):
		self.verticeAnterior = verticeAnterior

	def setearHeuristica(self, verticeDestino=0):
		self.heuristica = abs(verticeDestino.obtenerX()-self.obtenerX()) + abs(verticeDestino.obtenerY()-self.obtenerY())

	def obtenerHeuristica(self):
		return self.heuristica

	def obtenerPeso(self,vecino):
		return self.conectadoA[vecino]

	def setearValorFuncion(self, verticeDestino): #verticeAnterior es del cual viene en el recorrido; verticeDestino es con el que finaliza el algoritmo
		self.setearHeuristica(verticeDestino) #Generamos la heuristica segun el criterio que hayamos definido en el problema
		if self.obtenerVerticeAnterior() is not None:
			self.valorFuncion = self.obtenerPeso(self.obtenerVerticeAnterior())+self.obtenerHeuristica() #La sumamos al peso de verticeAnterior a verticeActual(self)
			return self.valorFuncion
		else:
			self.valorFuncion = self.obtenerHeuristica()
			return self.valorFuncion
