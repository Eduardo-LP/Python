#-*- coding: utf-8 -*-
a = "Eduardo"
b = "Lemos"

concatenar = a + " " + b

print(concatenar)

#lendo o numero de caracteres numa string

tamanho = len(concatenar)#a função len conta a contidade de caracteres dentro de uma string
print(tamanho)

print(concatenar[9])#usamos para acessar uma posição em uma string

for i in range(0,13):
	print(concatenar[i])

#alterando a fonte
print("alterando a fonte:")
print(concatenar)#quero deixar as palavras tudo em minusculo.. como fazer?
print(concatenar.lower())#deixa as palavras em minusculo
print(concatenar.upper())#deixa as palavras em MAIUSCULO
#tem a função strip que remove caracteres especiais do final da frase como exemplo: \n
print("\n")
busca = concatenar.find("Lemos")#enconta a posição que esta o inicio da palavra
print(busca)
print(concatenar[busca:])#printa do inicio da busca ate o final
print("\n")

#tambm podemos subistituir palavras

concatenar = concatenar.replace("Eduardo", "Nós")#troca a primeira palavra por outra
print(concatenar)