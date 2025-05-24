etudiants = ["Ali","Sara","Kaoutar","Imane"]

print("Liste des etudiants inscrits :")
for nom in etudiants:
    if nom.startswith("S"):
        print(f"{nom}(commence par S)")
    else:
        print(nom)