# Afficher en majuscule une lettre sur 2

import sys

def upper_one_on_two(string):
    letters = []
    i = 2
    for x in string:
        if not x.isdigit():
            if ord(x[0:]) in range(32, 48):
                letters.append(x)
            elif i % 2 == 0:
                letters.append(x.upper())
                i += 1
            else:
                letters.append(x.lower())
                i += 1
        else:
            sys.exit()
    sentence = "".join(letters)
    return sentence


try:

    arg1 = sys.argv[1]

    if len(sys.argv) != 2:
        sys.exit()
    else:
        if upper_one_on_two(arg1):
            print(upper_one_on_two(arg1))
        else:
            sys.exit()

except:
    print("error")
    sys.exit