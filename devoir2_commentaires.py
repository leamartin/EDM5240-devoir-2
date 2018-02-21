### BONJOUR, ICI JHR ###
### Mes notes et corrections sont encore précédées de trois dièses ###

#coding: utf-8

import csv

### Tout d'abord, je modifie simplement le nom du fichier pour faire rouler ton code sur mon ordi

fichier = "../grants.csv"

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

### C'est bien d'avoir pensé inclure un compteur, mais il compte l'ensemble des subventions contenues dans le fichier «grants.csv»
### Je vais le mettre en commentaire
	### n+=1

	if ligne[16] == "CPF - Aid to publishers":
		### J'ajoute le compteur à l'intérieur des conditions pour qu'il dénombre seulement les subventions que ton code trouve
		n+=1
		print (n,ligne, ligne[13])
	elif ligne [16] == "CPF - Business Innovation":
		n+=1
		print (n,ligne, ligne [13])
	elif ligne [16] == "Collective Initiatives":
		n+=1
		print(n,ligne, ligne [13]) 

### Intéressante méthode, avec un «if» et deux «elif»
### Encore plus simple: un seul «if» grâce auquel on teste deux conditions séparées par un «or»:
### «if "Fonds du Canada pour les périodiques" in ligne[17] or "FCP -" in ligne[17]:»
### Cela permet d'aller chercher plus de subventions: 4608, ce qui correspond davantage à ce qu'on cherche
### Car tes «if» et «elif» ne fonctionnent que si toute la ligne[16] correspond à l'expression recherchée
### ce qui fait que ton code ne trouve que 2350 subventions.

### En outre, je demandais d'afficher l'année
### La ligne[13] est la date complète à partir de laquelle il fallait extraire l'année