#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt

#abrira e lerá os dados do arquivo e retorna uma lista
dados = open("populacao-brasileira.csv").readlines()

x = []#anos
y = []#população

#navegação entre os dados
for i in range(len(dados)):
	if i != 0:#iginora a segunda linha
		linha = dados[i].split(";")
		#a função split separa pelo tipo de caracter selecionado dentro dos parenteses
		x.append(int(linha[0]))#add em "x" o valor da lista na posição 0
		y.append(int(linha[1]))#int converte para um numero inteiro

#legendas
plt.title("Crescimento da população brasileira")
plt.xlabel("ano")
plt.ylabel("população x100.000.000")

#construindo o grafico
plt.plot(x, y, linestyle= "--", color="k")
plt.bar(x, y, color= "#D3D3D3")

#mostrando o grafico
plt.show()