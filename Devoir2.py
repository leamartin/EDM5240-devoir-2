#coding: utf-8

import csv

fichier = "grants.csv"

f1 = open(fichier, encoding='utf-8')
lignes = csv.reader(f1)
next(lignes)

n = 0
objectif= 0
valeur = 0

#for ligne in lignes:
	#n+=1
	#print(n,ligne)

#for l in ligne:
	#print (n,l)

#if n != "aide aux éditeurs":
	#print ("erreur")

#dict = {int(lignes):int(ligne) for lignes,ligne in (x.split(':') for x in list) }

#for ligne in lignes:
	#n+=1
	#print("FCP - Aide aux éditeurs de périodiques", ligne)

#for ligne in lignes:
	#print(ligne [16]) 

#for ligne in lignes: 
	#n+=1

	#if ligne[16] == "CPF - Aid to publishers":
		#print (n,ligne)
	#if ligne [16] == "CPF - Business Innovation":
		#print(n,ligne) 
	#if ligne [16] == "Collective Initiatives":
		#print(n,ligne) 



#for ligne in lignes: 
	#n+=1

	#if ligne[16] == "CPF - Aid to publishers":
		#print (n,ligne)
	#elif ligne [16] == "CPF - Business Innovation":
		#print (n,ligne)
	#elif ligne [16] == "Collective Initiatives":
		#print(n,ligne) 
	#else print(ligne[13])


for ligne in lignes: 
	n+=1

	if ligne[16] == "CPF - Aid to publishers":
		print (n,ligne, ligne[13])
	elif ligne [16] == "CPF - Business Innovation":
		print (n,ligne, ligne [13])
	elif ligne [16] == "Collective Initiatives":
		print(n,ligne, ligne [13]) 
