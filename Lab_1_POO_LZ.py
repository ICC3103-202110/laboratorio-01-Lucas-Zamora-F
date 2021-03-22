# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:56:49 2021

@author: lucaz
"""
#-----------------------------imports-----------------------------------------
import numpy as np
from numpy import *

#-----------------------------Definiciones------------------------------------
def mostrar(x):
    print ('Tablero:')
    print()
    a = ''
    for i in range(2):
        for j in range(len(x[0])):
            a +=  str(x[i][j]) +'\t'
        print (a)
        print('')
        a = ''

def generar_tablero_j(x):
    t = np.zeros((2, x), dtype= object)
    for i in range(2):
        n = str(i)
        for j in range(x):
            m = str(j)
            p = '('+n+','+ m+')'
            t[i][j]= str(p)
            
    return t

def generar_tablero_c(x):
    t = np.zeros((2, x))
    n = []
    for a in range(2):
        for b in range(x):
            n.append(b)
    for i in range(2):
        for j in range(x):
            nr = n[random.randint(len(n))]
            n.remove(nr)
            t[i][j] = nr
          
    
    return t

def modificar_tablero(tableroj,tableroc, coord):
    tc = tableroj.copy()
    a = int(coord[0])
    b = int(coord[1])
    n = int(tablero_c[a][b])
    tc[a][b] = n
    return tc

def jugar(jugador, pjugador, ce):
    while True:
            print('')
            mostrar(tablero_j)
            print(jugador,'es tu turno!')
            c1 = input('Selecciona una carta!: ')
            coordenada1 = c1.split(',')
            a1 = int(coordenada1[0])
            b1 = int(coordenada1[1])
            if a1+1 <= 2 and b1+1 <= n_cartas:
                if cartas_elegidas.count(c1) == 0 :
                    cartas_elegidas.append(c1)
                    n1 = int(tablero_c[a1][b1])
                    tm = modificar_tablero(tablero_j, tablero_c, coordenada1)
                    mostrar(tm) 
                    while True:
                        c2 = input('Selecciona otra carta!: ')
                        coordenada2 = c2.split(',')
                        a2 = int(coordenada2[0])
                        b2 = int(coordenada2[1])
                        if a2+1 <= 2 and b2+1 <= n_cartas:
                            if cartas_elegidas.count(c2) == 0 :
                                cartas_elegidas.append(c2)
                                tm = modificar_tablero(tm, tablero_c, coordenada2)
                                n2 = int(tablero_c[a2][b2])
                                mostrar(tm)
                            
                                if n1 == n2:
                                    print('Le diste!,',jugador,' sigue jugando')
                                    tablero_j[a1][b1]= ''
                                    tablero_j[a2][b2]= ''
                                    mostrar(tablero_j)
                                    ce += 1
                                    cartas_encontradas = ce
                                    if cartas_encontradas == n_cartas:
                                        return ce
                            
                          
                                else:
                                    print('No le diste :c')
                                    cartas_elegidas.remove(c1)
                                    cartas_elegidas.remove(c2)
                                    return ce 
                            else:
                                print('Esa carta ya fue elegida!')
                                mostrar(tablero_j)
                                
                        else:
                             print('Esa carta no es valida!')
                             mostrar(tablero_j)
                else:
                    print('Esa carta ya fue elegida!')
                    mostrar(tablero_j)
            else:
                print('Esa carta no es valida!')

    
#-----------------------------Codigo------------------------------------------
n_jugador1 =str(input('ingrese el nombre del jugador 1: '))
n_jugador2 =str(input('ingrese el nombre del jugador 2: '))
cartas_encontradas = 0
cartas_elegidas = []
p_jugador1 = 0
p_jugador2 = 0
n_cartas = int(input('Con cuantas Cartas Desea jugar?: '))

print('')
tablero_j = generar_tablero_j(n_cartas)
tablero_c = generar_tablero_c(n_cartas)


while True:
    ce = jugar(n_jugador1, p_jugador1,cartas_encontradas)
    if cartas_encontradas != ce:
        p_jugador1 += (ce - cartas_encontradas)
    cartas_encontradas = ce
    if cartas_encontradas == n_cartas:
        break
    jugar(n_jugador2, p_jugador2,cartas_encontradas)
    if cartas_encontradas != ce:
        p_jugador2 += (ce - cartas_encontradas)
    cartas_encontradas = ce
    if cartas_encontradas == n_cartas:
        break
print('Se acabo el juego!')
print('puntajes')
print(n_jugador1,':',p_jugador1)   
print(n_jugador2,':',p_jugador2)    
if p_jugador1 < p_jugador2:
    print('Gana', n_jugador2)
elif p_jugador2 < p_jugador1:
    print('Gana', n_jugador1)
else:
    print('Es un empate!')
