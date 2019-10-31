# visualização de dados em python
#o atributo "as" faz com q a palavra seguinte seja usada
#como um apelido para aquela biblioteca sempre que quisermos usala
import matplotlib.pyplot as plt 

#função usada para fazer um grafico de linhas
x = [1,2]#numero minimo ate o maximo
y = [2,3]#numero minimo ate o maximo

#-------------add uma legenda--------
plt.title("meu primeiro grafico")#add um titulo ao grafico
plt.xlabel("eixo x")#cria uma legenda para o eixo x
plt.ylabel("eixo y")#cria uma legenda para o eixo y 

plt.plot(x,y)#lista de valores que indicaram as posições no "x" e no "y"
plt.show()#exibe o grafico