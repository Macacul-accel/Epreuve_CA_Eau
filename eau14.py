# Afficher les éléments donnés en argument par ordre ASCII

import sys

def sorted_ascii(lst_args):
    j = 0
    for x in range(len(lst_args) - 1, 0, -1):
        for i in range(x):
            while ord(lst_args[i][j]) == ord(lst_args[i + 1][j]):
                j += 1
            else:
                if ord(lst_args[i][j]) > ord(lst_args[i + 1][j]):
                    lst_args[i], lst_args[i + 1] = lst_args[i + 1], lst_args[i]
    final_lst = " ".join(lst_args)
    return final_lst


try:
    args = sys.argv[1:]

    if len(sys.argv) < 3:
        sys.exit()
    else:
        print(sorted_ascii(args))

except:
    print("error")
    sys.exit()