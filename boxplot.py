#-*- coding:utf-8 -*-
#criando um boxplot: diagrama de caixas
import matplotlib.pyplot as plt
import random as rd

vetor = []

for i in range(100):
	numero_aleatorio = rd.randint(0, 50)
	vetor.append(numero_aleatorio)

plt.boxplot(vetor)
plt.show()