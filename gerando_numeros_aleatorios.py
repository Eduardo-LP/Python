# -*- coding:utf-8 -*-
#importação da biblioteca para gerar os numeros aleatorios
import random

#gera um numero inteiro de 0 a 10 e armazena na variavel 'numero'
numero = random.randint(0,10)
print(numero)

#selecionar um numero de uma lista
lista = [34,22,99,46,48,71,20,3,20,10]
numero = random.choice(lista)
print(numero)