
def demander_nombre(min, max):
    reponse_str = input("Entrez une valeur entre " + str(min) + " et " + str(max) + ": ")
    try:
        reponse_int = int(reponse_str)
        if not min <= reponse_int <= max:
            print("vous devez rentrer un nombre entre", min, "et", max)
            return demander_nombre(min, max)
        return reponse_int
    except:
        print("Vous devez rentrer un nombre")
        return demander_nombre(min, max)
        
        
choix = demander_nombre(1, 5)
print("choix de l'utilisateur", choix)
            
    
    