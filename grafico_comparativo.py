# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt

#objetivo: criar um grafico comparativo
x1 = [1,3,5,7,9]
x2 = [2,4,6,8,10]

y1 = [4,2,6,2,8]
y2 = [1,4,7,8,5]

#Titulos
plt.title("Meu grafico comparativo")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

#construindo o grafico
plt.bar(x1, y1, label = "grupo 1")
plt.bar(x2, y2, label = "grupo 2")
plt.legend()#add as legendas a cima ao grafico

#visualização do grafico
plt.show()