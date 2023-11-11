# Afficher le premier nombre premier supérieur au nombre donné

import sys

def nbprem(x):
    i = 2
    while x % i != 0:
        i += 1
        if x == i:
            return True
    else:
        return False

def next_nb_prem(x):
    if x == 1:
        print(f"{x + 1} est le prochain nombre premier")
    else:    
        if nbprem(x) or not nbprem(x):
            x += 1
            while nbprem(x) == False:
                x += 1
            else:
                print(f"{x} est le prochain nombre premier")


try:
    if len(sys.argv) >= 3:
        sys.exit()
    else:
        arg1 = sys.argv[1]
        if not arg1.isdigit():
            sys.exit()
        elif int(arg1) <= 0:
            sys.exit()
        else:
            next_nb_prem(int(arg1))

except:
    print("-1")
    sys.exit()
