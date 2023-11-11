# Tri par sélection

import sys

def my_selec_sort(nb_list):
    n = len(nb_list)
    for i in range(n):
        min = i
        for x in range(i + 1, n):
            if int(nb_list[x]) < int(nb_list[min]):
                nb_list[min], nb_list[x] = nb_list[x], nb_list[min]
    return " ".join(nb_list)

try:
    if len(sys.argv) < 3:
        sys.exit()
    else:
        arg_lst = sys.argv[1:]
        print(my_selec_sort(arg_lst))

except:
    print("error")
    sys.exit()