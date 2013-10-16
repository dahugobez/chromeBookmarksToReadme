# This Python file uses the following encoding: utf-8
'''
Convertit les exports de favoris Chrome au format md pour GitHub

@TODO: Niveau de titre en fonction de la profondeur de noeud

'''

import re

def extraction( ligne):
	patternDeNoeud = 'H[0-9]+ ADD.*>(.*)</H[0-9]+>'
	patternDeFeuille = '<DT><A HREF="(.*)" ADD.*>(.*)</A>'
	match = re.findall( patternDeNoeud, ligne)
	if len(match) == 0:
		match = re.findall( patternDeFeuille, ligne)
		out = '* ['+match[0][1]+']('+match[0][0].replace(')','\)')+')'
		if len(match) == 0:
			raise Exception( 'no match')
	else:
		out = '\n\n###'+match[0]+'\n'
	return out


print( 'Initialisation...')
nomFichierChrome = 'favoris.html'
listeDeSortie = list()
listeDeRejets = list()
fichierChrome = open( nomFichierChrome)
fichierDeSortie = open( 'favoris.md','w')

print( '...extraction...')
for i in fichierChrome.readlines():
	try:
		listeDeSortie.append( extraction( i))
	except Exception, a:
		listeDeRejets.append( i)
print( 'extrait', len(listeDeSortie))
print( 'rejets', len(listeDeRejets))

print( '...ecriture...')
# ecriture du fichier de sortie
for u in listeDeSortie:
	fichierDeSortie.write( u+'\n')

print( '...fin.')
