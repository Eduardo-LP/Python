# -*- coding:utf-8 -*-
"""
em python dicionarios são arrays onde é possivel
add um "link" associado a uma palavra
como exemplo:
	a palavra "facebook" quando mensionada, estaremos
	nos refirindo ao link: "facebook.com"

"""
#dicionario de sites
dicionario_sites = {"udemy": "udemy.com", "google": "google.com", "facebook": "facebook.com"}

print(dicionario_sites['udemy'])#ele printara o site relacionado a quela "chave"(udemy)

for chave in dicionario_sites:#printara todos os sites desse dicionario
 	print(dicionario_sites[chave])