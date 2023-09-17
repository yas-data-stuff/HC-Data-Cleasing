#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
   MAC0122 Principios de Desenvolvimento de Algoritmos
 
   Problema da fatia de soma maxima: 

       dado:      uma lista v de números inteiros;
       encontrar: uma fatia v[e:d] de soma máxima.
'''
# importa todas as funções do módulo fatiamax
from fatiamax import *

# para o cronômetro
import time

# para o gerador de numeros aleatórios
import random

#------------------------------------------------------
# CONSTANTES

# numero de elementos
NMIN = 0x0100      # = 4096  
NMAX = 0x80000#00  # = 134217728 ~ 135 milhões

# semente default para o gerador de no. aleatorios
SEMENTE = 1234567

# no. de experimentos default.
NO_EXPERIMENTOS = 1

# para testes
MOSTRE = False

#
MIN = -4096
MAX =  4096

#------------------------------------------------------
def main(argv=None):
    #------------------------------------------------
    # valores default para os parâmetros
    semente = SEMENTE   # para o gerador de numeros aleatorios 
    no_experimentos = 1 # número de repeticoes de uma função
    max = NMAX   # numero maximo de elementos da lista 
    min = NMIN   # numero mínimo de elementos na lista
    
    # inicialize a semente do gerador de numeros aleatorios 
    random.seed(semente)

    # crie uma vetor com lista de max ints
    print("Criando lista com %d ints" %max)
    v = lista_int_rand(max)
    print("Lista criada.\n")

    # para teste
    if MOSTRE:
        print("semente = %d" %(semente))
        mostre_lista(v)

    # imprima cabeçalho 
    print("         n ", end="")
    print("    div_conq ", end="")
    print("   fatia_max \n", end="")

    n = min
    while n <= max:
        # cronometre algoritmo por divisão e conquista
        inicio = time.time()
        soma_max1, e1, d1 = fatia_max_div_conq(0, n, v)
        fim = time.time()
        t1 = fim-inicio
            
        # cronometre algoritmo quadrático
        inicio = time.time()
        soma_max2, e2, d2 = fatia_max(0, n, v)
        fim = time.time()
        t2 = fim-inicio

        print(f"{n:10}"     , end="")
        print(f"{t1:11.2f}s", end="")
        print(f"{t2:11.2f}s")

        if soma_max1 != soma_max2:
            print(f"SOCORRO! soma_max1 = {soma_max1} != {soma_max2} = soma_max2")
            
        # proximo valor de n
        n *= 2

#------------------------------------------------------------
#  F U N C O E S    A U X I L I A R E S 
#------------------------------------------------------------
def lista_int_rand(n):
    '''(int) -> list
    REXECE um inteiro não negativo n.
    CRIA e RETORNA uma lista com n número inteiros gerados aleatoriamente no
        intervalo [MIN,MAX[.
    '''
    lista = []
    for i in range(n):
        valor = random.randrange(MIN,MAX)
        lista.append(valor)
    return lista

#------------------------------------------------------------
def mostre_lista(v):
    '''(list) -> None
    RECEBE uma lista v de números inteiros.
    EXIBE o seu conteudo de uma maneira conveniente.
    '''
    print("Lista:")
    n = len(v)
    for i in range(n):
        print(f"{i:8}: {v[i]}")


#-----------------------------------------------------------    
if __name__ == "__main__":
    main()
    
