
import random


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = 5

vies = NB_VIES
def demander_nombre(nb_min, nb_max):
    
    nombre_int = 0
    
    while nombre_int == 0:
        
        nombre_str = input(f'entrer un nombre entre {nb_min} et {nb_max}? ')
        
        try:
            nombre_int = int(nombre_str)
            
        except:
            print('veuillez entrer une valeur correcte')
        
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f'vous devez rentrer une valeur entre {nb_min} et {nb_max}. Réessayez.')
                nombre_int = 0
                
    return nombre_int

nombre = 0

#le nombre magique est plus petit
while not nombre == NOMBRE_MAGIQUE and vies > 0:
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    print(f'il vous reste {vies} vies.')
    if nombre < NOMBRE_MAGIQUE:
        print('le nombre est plus petit que le nombre magique')
        vies -= 1
    elif nombre > NOMBRE_MAGIQUE:
        
        print('le nombre est plus grand que le nombre magique')
        vies -= 1
        
    else:
            print('BRAVO!!')
if vies == 0:           
    print(f'Vous avez perdu. le nombre magique était: {NOMBRE_MAGIQUE}')
    
#le nombre magique est plus grand
#le nombre est trouvé


