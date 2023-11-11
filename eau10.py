# Afficher l'index de l'élément recherché (dernier argument), dans tous les arguments affichés

import sys


    
def wanted_index():
    lst_arg = sys.argv[1:-1]
    the_wanted = sys.argv[-1]

    for x in range(len(lst_arg)):
        if lst_arg[x] == the_wanted:
            return x
    return sys.exit()


try:
    if len(sys.argv) < 3:
        sys.exit()
    else:
        print(wanted_index())

except:
    print("-1")
    sys.exit()