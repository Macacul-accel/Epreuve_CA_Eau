# Afficher les valeurs entre 2 deux nombres dans l'ordre croissant

import sys

def between_min_max(small, big):
    lst_between = []
    if small != big:
        if small < big:
            i = small
            x = big
        else:
            i = big
            x = small
        for value in range(i, x):
            lst_between.append(value)
        final_lst = " ".join(map(str, lst_between))
        return final_lst
        
                
try:

    nb1 = int(sys.argv[1])
    nb2 = int(sys.argv[2])

    if len(sys.argv) != 3:
        sys.exit()
    else:
        print(between_min_max(nb1, nb2))

except:
    print("error")
    sys.exit()