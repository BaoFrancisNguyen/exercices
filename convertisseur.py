#1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"

# 1 CM = 0.393701 pouces
# 1 POUCE = 2.54 cm

#2 - Demander à l'utilisateur de rentrer la valeur à convertir (en réaffichant l’unité demandée)

  
def convertisseur(unit1, unit2, facteur):
    
    valeur_str = input(f'Conversion {unit1} vers {unit2}. Donnez la valeur à convertir ou  \'q\' pour quitter le programme: ')
    if valeur_str == 'q':
        print('Vous avez quitté le programme')
        exit()
    valeur_float = float(valeur_str)
    valeur_convertie = round(valeur_float * facteur, 2) #valeur arrondie à 2 décimals
    print(f'Le résultat est de {valeur_convertie} {unit2}')

print('convertisseur')
print('a - pouce vers CM')
print('b - CM vers pouce') 

valeur = input(f'Veuiller choisir une valeur: a ou b (ou taper \'q\' pour quitter le programme): ') 

while True:
    
    if valeur == 'q':
        print('Vous avez quitté le programme')
        exit() 
        
    if valeur == "a":
        # a : cm --> pouces
            convertisseur('cm', 'pouces', 0.393701)
            
    if valeur == 'b':
        # b : pouces --> cm
            convertisseur('pouces', 'cm', 2.54)



  

    

#3 - Afficher la valeur convertie (et l'unité : cm ou pouces)

#- fin du programme.