# Déterminer si une chaîne de caractère se trouve dans une autre

import sys

def str_in_str(big_str, in_str):
    for i in range(len(big_str) - len(in_str) + 1):
        if big_str[i:i+len(in_str)] == in_str:
            return True
    return False

try:
    str_prcpal = sys.argv[1]
    small_str = sys.argv[2]

    if len(sys.argv) > 3:
        sys.exit()
    elif not str_prcpal.isdigit() and not small_str.isdigit():
        print(str_in_str(str_prcpal, small_str))

except:
    print("error")
    sys.exit()
