import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_QUESTION = 4
# opérateur choisi au hasard
OPERATOR = 4

#score de départ
nb_point = 0

    


def poser_question():
        
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, OPERATOR)

    if o == 0:
        operateur = '+'
    elif o == 1:
        operateur = '-'
    elif o == 2:
        operateur = '*'
    else:
        # les reponses en float ne sont pas acceptées, voir ligne 34
        operateur = '/'
    
    # l'opérateur généré reste constant, il faudrait installer une boucle pour qu'il change à chaque question
    question_str = input(f'calculez {a} {operateur} {b} = ')
            
    question_int = int(question_str)
    
    # la boucle ne marche pas, elle ne retourne que des FALSE, il doit y avoir une erreur dans les conditions de déclenchement    
    while not question_int == a + b or a - b or a * b or a / b:
        
        return False
            
    else:
        
        return True

# résultat question
for i in range(0, NOMBRE_QUESTION):
    
    print(f'question n°{i+1} sur {NOMBRE_QUESTION}:')
    
    if poser_question():
        nb_point += 1
        print('votre réponse est correct')
        print(f'votre note est de {nb_point} / {NOMBRE_QUESTION}')
        print()
    else:
        print('Votre réponse est incorrect')
        print(f'votre note est de {nb_point} / {NOMBRE_QUESTION}')
        print()
        
print('c\'est la fin de l\'exercice.')

