# Afficher en majuscule le début de chaque mot

import sys

def upper_first_letter(string):
    letters = []

    if len(string) > 2 and not string.isdigit():
        for x in range(len(string)):
            if x == 0:
                letters.append(string[x].upper())
            elif string[x - 1] in [" ", "/n", " "]:
                letters.append(string[x].upper())
            else:
                letters.append(string[x].lower())
    else:
        sys.exit("nombre")

    sentence = "".join(letters)
    return sentence


try:
    arg = sys.argv[1]

    if len(sys.argv) != 2:
        sys.exit("pas bon")
    else:
        print(upper_first_letter(arg))

except:
    print("error")
    sys.exit("c'est la rue")