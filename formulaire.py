#implémenter fonction recuperer_et_afficher_infos_de_la_personne
# paramètre : numero_personne
#rien retourner
#input / print
#variables nom / age

nombre_personnes = input('Entrez le nombre de personne : ')

def recuperer_infos_personnes(numero_personne):
    
    nom_personne = input('nom de la personne '+ str(numero_personne) + ' : ')
    age_personne = input('age de la personne ' + str(numero_personne) + ': ')
    return nom_personne, int(age_personne)
    

def afficher_infos_personne(numero, nom, age=0):
    
    print(f'le nom de la personne', numero, ' est :', nom, '')
    print(f'l age de la personne', numero, ' est: ', age,'')
    print('le nom comporte ' + str(len(nom)) +' caractères')
    
def recuperer_et_afficher_infos_de_la_personne(numero_personne):
    
    nom_personne, age_personne = recuperer_infos_personnes(numero_personne)
    
    afficher_infos_personne(numero_personne, nom_personne, age_personne)



for i in range(int(nombre_personnes)):
    recuperer_et_afficher_infos_de_la_personne(i+1)



###nom1 = input('nom de la personne: ')
#age1 = input ('age de la personne: ')
#print('le nom de la personne est : nom1')
#print('l age de la personne est: age1')
#print('le nom comporte, len(nom1), caractères')###