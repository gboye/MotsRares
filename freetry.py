import codecs
import sys

#from urllib import urlencode
import re
import urllib.request
from urllib.parse   import quote
lig=[]
fichier=codecs.open(sys.argv[1],"r","utf-8")
#lig=set()
for line in fichier:
	line=line.strip()
	p=line.split("\t")
	formes=p[0]#.translate(neutralisations)
	cats=p[1]
	lig.append(formes)
	#print (lig)
	#~ lig.add(formes)
mots=lig
 
#print ("<!DOCTYPE html><html><body>")
 
mots=["avancer","oxymore","lance-grenade","mi-machine"]
for mot in mots:
	 
	url="http://www.larousse.fr/dictionnaires/francais/%s" % mot
	 
	urlContent = urllib.request.urlopen(url)
	htmlPage=urlContent.readlines()
	lignes=[]
	definitions=[]
	debut=False
	fin=False
	for element in htmlPage:
		line=element.decode('utf-8').replace("\n"," ").replace("\r"," ")
		if '<ul class="Definitions">' in line:
			debut=True
		elif debut and '</ul>' in ligne:
			debut=False
		elif debut:
			lignes.append(line)
		else:
#			print ("autre",line)
			pass
	definition=" ".join(lignes)
	print(mot+"\t"+definition)
#~ print ("</body></html>")
		#definitions=definition
	#for mot in mots:
	#if mot in definition:
			
		#print(mot+"\t"+definition+"\n")
		##else:
		    #print(mot+"\t"+"no definition available"+ "\t"+"x"+"\n")	
	sys.stderr.write(".")
	sys.stderr.flush()		
