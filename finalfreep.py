# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# #Extraction de définitions pour les mots rares

# <markdowncell>

# ##Importation des modules de traitement
# 
# - urllib.request pour l'extraction de contenu en ligne
# - bs4 (BeautifulSoup4) pour le traitement de structures HTML

# <codecell>
import codecs
import sys,os
import re
import urllib.request

nomLexique=sys.argv[1]

try:
	fichierLexique=codecs.open(nomLexique,"r","utf-8")
except IOError:
	sys.stderr.write('I could not open the lexicon file', nomLexique)
	sys.exit()


nomDictionnaire=nomLexique.split(".",1)[0]+"-dict.csv"

if os.path.isfile(nomDictionnaire):
	sys.stderr.write("le fichier",nomDictionnaire,"existe déjà.")
	sys.exit()
else:
	try:
		fichierDictionnaire=codecs.open(nomDictionnaire,"w","utf-8")

	except IOError:
		sys.stderr.write('I could not open the lexicon file', nomDictionnaire)
		sys.exit()


neutralisations=str.maketrans('éèêâàãçýïñüûôöî','eeeaaacyinuuooi')
lig=[]
for line in fichierLexique:
	line=line.strip()
	p=line.split("\t")
	formes=p[0].translate(neutralisations)
	cats=p[1]
	lig.append(formes)
mots=lig

#import bs4

# <markdowncell>

# ##Importation du lexique des mots rares à définir
# 
# Pour l'instant, juste une liste de mots saisie à la main.

# <codecell>


# <markdowncell>

# ##Boucle de récupération des définitions
# 
# Pour chaque *mot* dans *mots*
# 
# - on fabrique *url* qui correspond à l'adresse du *mot* sur le site du CNRTL
# - on récupère le contenu de la page dans *urlContent*
# - on stocke le contenu dans un objet *htmlPage* qui permet de manipuler le texte en HTML **bs4.BeautifulSoup**
# - on cherche la balise qui a id="lexicontent" et on extrait son contenu dans *definition*
# - on ajoute *definition* à la liste *definitions*

# <codecell>
#print ("<!DOCTYPE html><html><body>")
for mot in mots:
	
	url="http://cnrtl.fr/definition/% s" % mot
	urlContent = urllib.request.urlopen(url)
	htmlPage=urlContent.readlines()
	
		
	
	
	debut=False
	fin=False
	newline=False
	lignes=[]
	definitions=[]
	for element in htmlPage:
		line=element.decode('utf-8').replace("\n"," ").replace("\r"," ")
		if "lexicontent" in line:
			debut=True
		if "footer" in line:
			fin=True
		if debut and not fin:
			lignes.append(line)
		definition=" ".join(lignes)
	fichierDictionnaire.write(mot+"\t"+definition+"\n")
	sys.stderr.write(mot+" ")
	sys.stderr.flush()
fichierDictionnaire.close()

