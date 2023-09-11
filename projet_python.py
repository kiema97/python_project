############################################################################################
##############              PROJET PYTHON                       ############################
##############          GESTION DES NOTES D'UNE CLASSE          ############################
"""
MEMBRES DU GROUPE
- SAVADOGO Idrissa 
- SIRIMA Constant
- NANA Jerémie
- KIEMA Wend-denda Arsène (E-mail: arsenekiema@statplus.net 
                           Téléphone : (+226) 64 66 62 63 / 72 10 03 95)
"""    
# 1- Fonction pour calculer la moyenne d'un élève
def calculer_moyenne(notes, coefficients):
    somme = sum(notes[i] * coefficients[i] for i in range(len(notes)))
    total_coefficients = sum(coefficients)
    moyenne = somme / total_coefficients
    return moyenne

# 2- Fonction pour déterminer si un élève passe en classe supérieure
def passe_en_classe_superieure(moyenne, seuil_passage):
    return moyenne >= seuil_passage

# 3- Demander à l'utilisateur de saisir les matières et leurs coefficients
matieres = []
coefficients = []
nombre_matiere = int(input("Entrez le nombre de matières : "))

for i in range(nombre_matiere):
    matiere = input(f"Entrez le nom de la matière {i+1}: ")
    coefficient = float(input(f"Entrez le coefficient de {matiere}: "))
    matieres.append(matiere)
    coefficients.append(coefficient)

# 4- Demander à l'utilisateur de saisir la liste des élèves et leurs notes
eleves = {}
seuil_passage = float(input("Entrez le seuil de passage en classe supérieure : "))

nombre_eleves = int(input("Entrez le nombre d'élèves : "))

for i in range(nombre_eleves):
    nom_eleve = input(f"Entrez le nom de l'élève {i+1}: ")
    notes_eleve = []
    for j in range(nombre_matiere):tf
        note = float(input(f"Entrez la note de {matieres[j]} pour {nom_eleve}: "))
        notes_eleve.append(note)
    
    moyenne_eleve = calculer_moyenne(notes_eleve, coefficients)
    eleves[nom_eleve] = moyenne_eleve

# 5-Afficher la liste des élèves classée par ordre de mérite
eleves_tries = sorted(eleves.items(), key=lambda x: x[1], reverse=True)

print("\nListe des élèves classés par ordre de mérite :")
for nom, moyenne in eleves_tries:
    resultat = "Admis" if passe_en_classe_superieure(moyenne, seuil_passage) else "Non admis"
    print(f"{nom}: Moyenne {moyenne:.2f} - Statut: {resultat}")
        