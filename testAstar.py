from Grafo import Grafo
from Vertice import Vertice

archivo  = open("recorridolaberinto2.txt", "r")
grafo = Grafo()

print("-------------------------------------------------------------------------------------")
print("Leyendo el laberinto del archivo y agregandolo al grafo")

numeroVertice = 1 #El inicial va a ser 1 por defecto
verticePacman = 0 #Por defecto tiene un valor incorrecto. Deberia cambiar a lo largo del programa
verticeComida = 0 #Por defecto tiene un valor incorrecto. Deberia cambiar a lo largo del programa
mapa = archivo.readlines() #Paso el contenido del archivo a una lista de lineas para leerlo durante el programa
#Comenzando a iterar por sobre el mapa
for i, linea in enumerate(mapa):
	for j, caracter in enumerate(linea):
		if(caracter=='-' or caracter.lower()=='P'.lower() or caracter.lower()=='O'.lower()): #No es pared (camino, pacman o comida)
			grafo.agregarVertice(numeroVertice, 1, posX=j, posY=i) #j representa a la dimension X, i a la dimension Y, el 1 es la distancia
			vecinoBuscadoH = grafo.buscarVertice(j-1, i) #Vecino horizontal izquierdo
			if vecinoBuscadoH is not None:
				grafo.agregarArista(numeroVertice, vecinoBuscadoH.obtenerEtiqueta(), 1)
				grafo.agregarArista(vecinoBuscadoH.obtenerEtiqueta(), numeroVertice, 1)
			vecinoBuscadoV = grafo.buscarVertice(j, i-1) #Vecino horizontal superior
			if vecinoBuscadoV is not None:
				grafo.agregarArista(numeroVertice, vecinoBuscadoV.obtenerEtiqueta(), 1)
				grafo.agregarArista(vecinoBuscadoV.obtenerEtiqueta(), numeroVertice, 1)
			if(caracter.lower()=='P'.lower()):
				verticePacman = numeroVertice
			elif(caracter.lower()=='O'.lower()):
				verticeComida = numeroVertice
			numeroVertice+=1
	print("paso " +str(i+1)+ " vez por el bucle")

print("-------------------------------------------------------------------------------------")
print("Ejecutando el algoritmo de A estrella")
grafo.astar2(grafo.obtenerVertice(verticePacman), grafo.obtenerVertice(verticeComida))


print("pruebas-----------------------------------------------------------------")
for vertice in grafo.listaVertices:
	verticeIndex = grafo.listaVertices[vertice]
	for vecino in verticeIndex.obtenerConexiones():
		print("vertice: " + str(verticeIndex.obtenerEtiqueta()))
		print("vecino: " + str(vecino.obtenerEtiqueta()))
		print("-----------------------")

print("pruebas2-----------------------------------------------------------------")
for vertice in grafo.listaVertices:
	print(vertice)

print("vertices importantes--------------------------------------------------")
print("pacman:")
print(grafo.obtenerVertice(verticePacman).posX)
print(grafo.obtenerVertice(verticePacman).posY)
print("comida:")
print(grafo.obtenerVertice(verticeComida).posX)
print(grafo.obtenerVertice(verticeComida).posY)