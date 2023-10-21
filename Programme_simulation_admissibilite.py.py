import numpy as np

def moyenneCB(noms_ecoles:list, seuils_admissibilite:list,coefficients:list)->None:
    
    notes = np.array([
        float(input("note de Maths EDHEC?\n")),
        float(input("note de Maths EM Lyon?\n")),
        float(input("note de Maths Ecricome?\n")),
        float(input("note de Maths ESSEC II?\n")),
        float(input("note de philosophie HEC?\n")),
        float(input("note de philosophie EDHEC?\n")),
        float(input("note de philosophie Ecricome?\n")),
        float(input("note de anglais ELVi?\n")),
        float(input("note de Allemand ELVi?\n")),
        float(input("note de Anglais Ecricome?\n")),
        float(input("note de Allemand Ecricome?\n")),
        float(input("note de synthèse?\n")),
        float(input("note de résumé?\n")),
        float(input("note de HGG ESCP?\n")),
        float(input("note de HGG ESSEC?\n")),
        float(input("note de HGG Ecricome?\n"))
    ])

    resultats = np.dot(coefficients, notes)/30

    for i, resultat in enumerate(resultats):
        print(f"Ta note à {noms_ecoles[i]}: {resultat:.2f}")

        # Vérification des seuils d'admissibilité
        if resultat > seuils_admissibilite[i]:
            print(f"Admissible à {noms_ecoles[i]}")

# Exemple d'utilisation de la fonction
if __name__ == '__main__':
    noms_ecoles = ["EDHEC", "EM LYON", "Skema", "NEOMA", "Audencia"]
    seuils_admissibilite = [12.63, 11.8, 10.8, 10.4, 9.5]
    coefficients = np.array([
            [6, 0, 0, 2, 0, 4, 0, 5, 2, 0, 0, 3, 0, 0, 8,0],  # Coefficients pour l'EDHEC
            [0, 6, 0, 2, 6, 0, 0, 4, 2, 0, 0, 2, 0, 8, 0, 0],  # Coefficients pour l'EMLYON
            [0, 5, 0, 0, 6, 0, 0, 6, 5, 0, 0, 3, 0, 6, 0, 0],  # Coefficients pour SKEMA
            [0, 0, 6, 0, 0, 0, 5, 0, 0, 5, 3, 0, 2, 0, 0, 9],  # Coefficients pour NEOMA
            [9, 0, 0, 0, 6, 0, 0, 4, 3, 0, 0, 3, 0, 6, 0, 0]   # Coefficients pour Audencia
        ])

    moyenneCB(noms_ecoles, seuils_admissibilite,coefficients)

