#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt

#objetivo: criar um grafico de pontos
x = [1,3,5,7,9]
y = [1,4,7,8,5]

titulo = "Scatterplot: grafico de pontos"
eixoX = "Eixo X"
eixoY = "Eixo Y"

#legendas
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

#construção do grafico
plt.scatter(x, y)#cria os pontos na tela
plt.plot(x, y)#utilizada para ligar os pontos

#salvando a figura do grafico
plt.savefig("Grfico_teste.png", dpi= 300)#dpi é a qualidade da resolução. recomendado 300
#visualizando o grafico
plt.show()