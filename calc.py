import matplotlib.pyplot as graph

#CALCUL DE LA FONCTION
def calcGraph(degre, start, fin, pas):	
	function = []
	listePoints = []
	listeX = []
	
	for i in range(degre+1):
		value = float(input("x^" + str(i) + " pour x = "))
		function.append(value)

	while(start <= fin):
		resultat = 0
		for i in range(len(function)):
			if i == 0:
				resultat += function[i]
			else:
				resultat += function[i]*start**i
		if resultat == int(resultat):
			resultat = int(resultat)
		listePoints.append(round(resultat, 3))
		listeX.append(round(start, 4))
		start += pas

	return [listeX, listePoints]

#VARIABLES
mode = 0
debut = -1000
fin = 1000
pas = 1

#MENU
while mode != 1 and mode != 2:
	mode = int(input("Mode :\n1.Tableau de Valeur\n2.Graphique\n3.Options\n>"))
	if mode == 3:
		debut = float(input("Début : "))
		fin = float(input("Fin : "))
		pas = float(input("Pas : "))
	if mode < 1 and mode > 3:
		print("Erreur, veuillez recommencez")


deg = int(input("Degré de l'équation : "))
values = calcGraph(deg, debut, fin, pas)
x = values[0]
y = values[1] 


#TABLEAU DE VALEURS
if(mode == 1):
	for i in range(len(x)):
		print("f(" + str(round(values[0][i], 4)) + ")       \t=\t" + str(y[i]))

	while True:
		searchValue = round(float(input("\nChercher une l'image d'un x : ")), 4)
		valueIndex = x.index(searchValue)
		print("f(" + str(round(searchValue, 4)) + ") = " + str(y[valueIndex]))


#GRAPHIQUE
else:
	graph.title("Graphic Calculator")
	graph.plot(x, y)
	graph.xlabel('abscisses')
	graph.ylabel('ordonnées')
	graph.show()

