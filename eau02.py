# Afficher les arguments reçus à l'envers

import sys

try:
    if len(sys.argv) < 3:
        sys.exit()
    else:
        for x in sys.argv[:0:-1]:
            print(x)

except:
    print("Error")
    sys.exit()
