# Créez un programme qui affiche le N-ème élément de la célèbre suite de Fibonacci. (0, 1, 1, 2) étant le début de la suite et le premier élément étant à l’index 0

import sys

def fibo(elmnt):
    suite = []
    suite.append(0)
    suite.append(1)
    while len(suite) != elmnt:
        x = suite[-1] + suite[-2]
        suite.append(x)
    else:
        print(suite[elmnt - 1])

try:

    i = int(sys.argv[1])
    if i < 0:
        print("-1")
    else:
        fibo(i)

except:
    print("-1")