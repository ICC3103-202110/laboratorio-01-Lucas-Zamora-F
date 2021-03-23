# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:56:49 2021

@author: lucaz
"""
#-----------------------------Notas para el Corrector-------------------------
'''
El codigo para funcionar bien, las cordenadas deben de ser ingresadas como 'x,x'
por ejemplo: Seleccione una carta! 9,9

bugs: Al no ingresar las coordenadas como son solicitadas el programa crashea

Programa v3: Standars PEP-8

Programa v4: todas las variables y definiciones ahora estan en inlges.

Cualquier feedback es bien agradecido.
'''
#-----------------------------imports-----------------------------------------
import numpy as np
from numpy import *

#-----------------------------Definiciones------------------------------------
def show(x):
    
    print ('Tablero:')
    
    print()
    
    a = ''
    
    for i in range(2):
        
        for j in range(len(x[0])):
            
            a += str(x[i][j]) +'\t'
            
        print (a)
        
        print('')
        
        a = ''
        

def generate_board_p(x):
    
    t = np.zeros((2, x), dtype= object)
    
    for i in range(2):
        
        n = str(i)
        
        for j in range(x):
            
            m = str(j)
            
            p = '('+n+','+ m+')'
            
            t[i][j]= str(p)
            
    return t


def generate_board_c(x):
    
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


def modify_board(board_p, board_c, coord):
    
    tc = board_p.copy()
    
    a = int(coord[0])
    
    b = int(coord[1])
    
    n = int(board_c[a][b])
    
    tc[a][b] = n
    
    return tc


def play(player, ce):
    
    while True:
        
            print('')
            
            z = 0
            
            show(board_p)
            
            print(player,'es tu turno!')
            
            c1 = input('Selecciona una carta!: ')
            
            coordinate1 = c1.split(',')
            
            a1 = int(coordinate1[0])
            
            b1 = int(coordinate1[1])
            
            if a1+1 <= 2 and b1+1 <= amount_cards:
                
                if chosen_cards.count(c1) == 0 :
                    
                    chosen_cards.append(c1)
                    
                    n1 = int(board_c[a1][b1])
                    
                    tm = modify_board(board_p, board_c, coordinate1)
                    
                    show(tm) 
                    
                    while True:
                        
                        if z == 1:   
                            
                            #esto es para que no quede atrapado en el while de 
                            #arriba y vuelva al estado inicial
                            
                            break
                        
                        c2 = input('Selecciona otra carta!: ')
                        
                        coordinate2 = c2.split(',')
                        
                        a2 = int(coordinate2[0])
                        
                        b2 = int(coordinate2[1])
                        
                        if a2+1 <= 2 and b2+1 <= amount_cards:
                            
                            if chosen_cards.count(c2) == 0 :
                                
                                chosen_cards.append(c2)
                                
                                tm = modify_board(tm, 
                                                  board_c, coordinate2)
                                
                                n2 = int(board_c[a2][b2])
                                
                                show(tm)
                            
                                if n1 == n2:
                                    
                                    print('Le diste!,',player,'sigue jugando')
                                    
                                    board_p[a1][b1]= ''
                                    
                                    board_p[a2][b2]= ''
                                    
                                    ce += 1
                                    
                                    z=1
                                    
                                    found_cards = ce
                                    
                                    print('Cartas encontradas:', 
                                          found_cards)
                                    
                                    if found_cards == amount_cards:
                                        
                                        return ce
                          
                                else:
                                    
                                    print('No le diste :c')
                                    
                                    chosen_cards.remove(c1)
                                    
                                    chosen_cards.remove(c2)
                                    
                                    return ce 
                                
                            else:
                                
                                print('Esa carta ya fue elegida!')
                                
                                show(tm)
                                
                        else:
                            
                             print('Esa carta no es valida!')
                             
                             show(board_p)
                             
                else:
                    
                    print('Esa carta ya fue elegida!')
                    
            else:
                
                print('Esa carta no es valida!')

    
#-----------------------------Codigo------------------------------------------
n_player1 =str(input('ingrese el nombre del jugador 1: '))
n_player2 =str(input('ingrese el nombre del jugador 2: '))
found_cards = 0
chosen_cards = []
player1_points = 0
player2_points = 0


while True:
    chosen_a_cards = (input('Con cuantas Cartas Desea jugar?: '))
    try:
        if int(chosen_a_cards):
            break
    except ValueError:
        print('Ingrese un numero valido')
amount_cards = int(chosen_a_cards)
    
    
print('')
board_p = generate_board_p(amount_cards)
board_c = generate_board_c(amount_cards)


while True:
    ce = play(n_player1, found_cards)
    player1_points += (ce - found_cards)
    found_cards = ce
    if found_cards == amount_cards:
        break
    ce = play(n_player2, found_cards)
    player2_points += (ce - found_cards)
    found_cards = ce
    if found_cards == amount_cards:
        break
    

print()
print('----------------------------------------------------------------------')
print('Se acabo el juego!')
print()
print('puntajes')
print(n_player1, ':', player1_points)   
print(n_player2,':',player2_points)
print()    
if player1_points < player2_points:
    print('Gana', n_player2)
elif player2_points < player1_points:
    print('Gana', n_player1)
else:
    print('Es un empate!')
