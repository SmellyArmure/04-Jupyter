import numpy as np
from mod_strat import Strategie

def play(strat, nbe):
    # Génération des tirages alétaoires
    tir = np.random.randint(1,4, size=nbe) # tirage (numéro du gobelet gagnant)
    chx = np.random.randint(1,4, size=nbe) # choix du joueur
    # Prise en compte de la stratégie "aléatoire" 
    if strat == Strategie.alea: # si le joueur choisit aléatoirement sa stratégie
        tab_strat = np.random.randint(0,2, size=nbe) # tableau de stratégies (0:idem ou 1:alter)
        return np.multiply(tab_strat != np.array([chx == tir]),1).reshape(nbe,) # *voir note plus bas
    else:
    # Calcul du résultat selon la stratégie "garder" ou "changer"
        if strat == Strategie.idem: # si le joueur garde son choix de départ
            return np.multiply(np.array([chx == tir]),1).reshape(nbe,) # compare les éléments des tablaux chx et tir un à un
        elif strat == Strategie.alter: # si le joueur change de choix 
            return np.multiply(~np.array([chx == tir]),1).reshape(nbe,) # inverse du résultat précédent
# s'il avait choisi le gagnant...il choisit désormais forcément un perdant
# s'il avait choisi le perdant... le maître du jeu retire l'autre perdant et il reste le gagnant
        else: 
            print("Erreur de stratégie !")
# * Note : en faisant un schéma logique, on s'aperçoit que dans le cas d'un choix aléatoire de la stratégie,
# On gagne si et seulement si :
# 1) on est en stratégie "garder" et on avait gagné (config strat = 0 et resultat = 0)
# 2) on est en stratégie "changer" et on avait perdu (config strat = 1 et resultat = 1)
# ce qui correspond en logique à l'opérateur XOR, traduit ici en utilisant "!=" (différent de)
# sur les éléments des deux tableaux un à un.