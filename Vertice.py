class Vertice:
	def __init__(self, etiqueta, distancia=0, heuristica=0, verticeAnterior=None, posX=0, posY=0):
		self.etiqueta = etiqueta
		self.posX = posX
		self.posY = posY
		self.distancia = distancia #Utilizada para medir caminos minimos o maximos con Dijkstra
		self.heuristica = heuristica #Utilizada para medir caminos minimos o maximos con A* o A estrella
		self.conectadoA = {}
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

	def obtenerDistancia(self):
		return self.distancia

	def setearDistancia(self, distancia):
		self.distancia = distancia

	def obtenerVerticeAnterior(self):
		return self.verticeAnterior

	def setearVerticeAnterior(self, verticeAnterior):
		self.verticeAnterior = verticeAnterior

	def obtenerHeuristica(self):
		return self.heuristica

	def obtenerPeso(self,vecino):
		return self.conectadoA[vecino]