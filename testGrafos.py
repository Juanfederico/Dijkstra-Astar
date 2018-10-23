from Grafo import Grafo
from Vertice import Vertice


print("funciona")

grafo = Grafo()

print("-------------------------------------------------------------------------------------")
print("Definiendo la cantidad de vertices con sus distancias/heuristicas (0 por defecto)")

grafo.agregarVertice(1, 0) #Como utilizaremos Dijkstra para conocer los caminos minimos definimos solo distancias (en nuestro caso el nodo 1 sera el inicial)
grafo.agregarVertice(2, 99999)
grafo.agregarVertice(3, 99999)
grafo.agregarVertice(4, 99999)
grafo.agregarVertice(5, 99999)
grafo.agregarVertice(6, 99999)
grafo.agregarVertice(7, 99999)

print("-------------------------------------------------------------------------------------")
print("Agregando las conexiones entre los vertices")
#Se podria diferenciar de un grafo dirigido a un no dirigido en la clase grafo para no tener que hacer todo x2 en caso de no serlo

grafo.agregarArista(1,2,1)
grafo.agregarArista(1,3,5)
grafo.agregarArista(2,1,1)
grafo.agregarArista(2,3,4)
grafo.agregarArista(2,4,8)
grafo.agregarArista(2,5,7)
grafo.agregarArista(3,1,5)
grafo.agregarArista(3,2,4)
grafo.agregarArista(3,4,6)
grafo.agregarArista(3,6,2)
grafo.agregarArista(4,2,8)
grafo.agregarArista(4,3,6)
grafo.agregarArista(4,5,11)
grafo.agregarArista(4,6,9)
grafo.agregarArista(5,2,7)
grafo.agregarArista(5,4,11)
grafo.agregarArista(5,6,3)
grafo.agregarArista(5,7,10)
grafo.agregarArista(6,3,2)
grafo.agregarArista(6,4,9)
grafo.agregarArista(6,5,3)
grafo.agregarArista(6,7,12)
grafo.agregarArista(7,5,10)
grafo.agregarArista(7,6,12)

#for v in grafo:
#	for w in v.obtenerConexiones():
#		print("( %s , %s )" % (v.obtenerEtiqueta(), w.obtenerEtiqueta()))

print("-------------------------------------------------------------------------------------")

v = grafo.obtenerVertice(1)

grafo.dijkstra(v)

for vecino in v.obtenerConexiones():
	print(vecino) #toString del nodo vecino
	print("Peso: " + str(v.conectadoA[vecino]))