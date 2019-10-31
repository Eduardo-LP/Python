import matplotlib.pyplot as plt

#add valores ao grafico
x = [1,2,3,4,5]#valores no eixo x
y = [2,5,3,8,6]#valores de altura para cada item do eixo x

#add legendas
plt.title("Meu grafico de barras")
plt.xlabel("eixo X")
plt.ylabel("eixo Y")

#construção do grafico
plt.bar(x,y)#tipo grafico de barras
plt.show()#para gerar o grafico