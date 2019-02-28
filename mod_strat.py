from enum import Enum

# définit une classe stratégie
class Strategie(Enum):
    idem = 1 # ne pas changer de choix
    alter = 2 # changer de choix
    alea = 3 # adopter aléatoirement une des deux stratégies ci-dessus