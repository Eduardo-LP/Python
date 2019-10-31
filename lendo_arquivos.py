#-*- coding: utf-8 -*-
arquivo = open("arquivo_para_teste.txt")#função usada para abrir os arquivos

linhas = arquivo.readlines()#usada para ler linhas dentro desde arquivo, e transforma uma lista

for linha in linhas:
	print(linha)
print("\n")

texto_completo = arquivo.read()#le todo o arquivo e coloca em uma variavel só
