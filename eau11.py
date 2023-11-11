# Afficher la différence minimum absolue entre 2 éléments d'un tableau uniquement constituer de nombres

import sys

def absolute_min():
    nb_lst = sys.argv[1:]
    min_result = []
    for x in nb_lst:
        for i in nb_lst:
            if x != i:
                if int(x) - int(i):
                    result = int(x) - int(i)
                    if not min_result:
                        min_result.append(abs(result))
                    else:
                        if abs(result) < min_result[0]:
                            min_result.pop()
                            min_result.append(abs(result))
    return min_result[0]


try:
    if len(sys.argv) < 3:
        sys.exit()
    else:
        print(absolute_min())

except:
    print("error")
    sys.exit()