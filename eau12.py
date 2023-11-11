# Tri à bulle

import sys

def bubble_sort(nb_list):
    for x in range(len(nb_list)-1, 0, -1):
        for r in range(x):
            if int(nb_list[r]) > int(nb_list[r + 1]):
                nb_list[r], nb_list[r + 1] = nb_list[r + 1], nb_list[r]
    return " ".join(nb_list)

try:
    if len(sys.argv) < 2:
        sys.exit()
    else:
        arg_list = sys.argv[1:]
        print(bubble_sort(arg_list))

except:
    print("error")
    sys.exit() 