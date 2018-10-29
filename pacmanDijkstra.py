import os
import time
import numpy as np
from Grafo import Grafo
from Vertice import Vertice

archivo  = open("recorridopacman.txt", "r")
grafo = Grafo()

#Definimos que va a representar cada simbolo en el mapa
simboloPacman = 'P'
simboloCamino = '-'
simboloPared = '%'
simboloComida = '.'

print("-------------------------------------------------------------------------------------")
print("Leyendo el laberinto del archivo y agregandolo al grafo:")

numeroVertice = 1 #El inicial va a ser 1 por defecto
verticePacman = 0 #Por defecto tiene un valor incorrecto. Deberia cambiar a lo largo del programa
verticeComida = 0 #Por defecto tiene un valor incorrecto. Deberia cambiar a lo largo del programa
mapa = archivo.readlines() #Paso el contenido del archivo a una lista de lineas para leerlo durante el programa
#Comenzando a iterar por sobre el mapa
for i, linea in enumerate(mapa):
	for j, caracter in enumerate(linea):
		if(caracter==simboloCamino or caracter.lower()==simboloPacman.lower() or caracter.lower()==simboloComida.lower()): #No es pared (camino, pacman o comida)
			grafo.agregarVertice(numeroVertice, distancia=99999, posX=j, posY=i) #j representa a la dimension X, i a la dimension Y, el 1 es la distancia
			vecinoBuscadoH = grafo.buscarVertice(j-1, i) #Vecino horizontal izquierdo
			if vecinoBuscadoH is not None:
				grafo.agregarArista(numeroVertice, vecinoBuscadoH.obtenerEtiqueta(), 1)
				grafo.agregarArista(vecinoBuscadoH.obtenerEtiqueta(), numeroVertice, 1)
			vecinoBuscadoV = grafo.buscarVertice(j, i-1) #Vecino horizontal superior
			if vecinoBuscadoV is not None:
				grafo.agregarArista(numeroVertice, vecinoBuscadoV.obtenerEtiqueta(), 1)
				grafo.agregarArista(vecinoBuscadoV.obtenerEtiqueta(), numeroVertice, 1)
			if(caracter.lower()==simboloPacman.lower()):
				verticePacman = numeroVertice
			elif(caracter.lower()==simboloComida.lower()):
				verticeComida = numeroVertice
			numeroVertice+=1

print("-------------------------------------------------------------------------------------")
print("Ejecutando el algoritmo de Dijkstra:")
verticeInicial = grafo.obtenerVertice(verticePacman)
verticeFinal = grafo.obtenerVertice(verticeComida)
grafo.dijkstra(verticeInicial) #Se envia el vertice inicial como parametro

print("-------------------------------------------------------------------------------------")
print("Buscando la distancia total del camino:")
print(verticeInicial.obtenerVerticeAnterior().obtenerEtiqueta())
grafo.obtenerMejorCamino(verticeInicial, verticeFinal)
grafo.mostrarMejorCamino()