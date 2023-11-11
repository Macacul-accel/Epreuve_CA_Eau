# Afficher toutes les combinaisons possibles de 3 chiffres différents dans l'ordre croissant

def combination():
    combi_lst = []
    for a in range(10):
        for b in range(a + 1, 10):
            for c in range(b + 1, 10):
                combination = f"{a}{b}{c}"
                combi_lst.append(combination)
    return combi_lst

print(", ".join(combination()))