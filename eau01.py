# Afficher toutes les différentes combinaisons de 2 nombres

def combination():

    combi_lst = []
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    frst_part = f"{a}{b}"
                    scnd_part = f"{c}{d}"
                    if frst_part < scnd_part:
                        combi = f"{a}{b} {c}{d}"
                        combi_lst.append(combi)
    return combi_lst

print(" , ".join(combination()))