# Afficher si une chaîne de caractère contient que des chiffres

import sys

def is_number(arg):
    if int(arg):
        return True
    else:
        return False
    
try:
    
    arg1 = sys.argv[1]

    if len(sys.argv) != 2:
        sys.exit()
    else:
        print(is_number(arg1))

except:
    print("error")
    sys.exit()