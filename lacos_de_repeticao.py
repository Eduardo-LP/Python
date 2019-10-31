#-*- coding: utf-8 -*-
#usando o comando while(enquanto)
linhas = 1
asteriscos = 1
ast = "*" 

while linhas <= 4:
	while asteriscos < 5:
		print(ast)
		asteriscos += 1

	print("\n")
	asteriscos = 1
	linhas += 1

#usando o comando for(para)
lista = [1,2,3,4,5] #listas são arrays(vetores)

for i in lista:
	print(i)

#for usando o comando range
for i in range(10,50,2): #criei uma lista de 10 a 50 onde a contagem é feita de 2 em 2
	print(i)