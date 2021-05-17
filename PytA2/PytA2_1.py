def raim(tipus, grandaria):
        if tipus == "A":
            if grandaria == "1":
                return 20
            else:
                return 30
        if tipus == "B":
            if grandaria == "1":
                return 30
            else:
                return 50
tipus = input("Quin tipus de raim A o B?")
gradaria = input("Quin tipues de grandaria 1 o 2?")
cantitat = int(input("Quants quilos vols"))
print(f"Total a pagar {cantitat * raim(tipus,gradaria)}€")