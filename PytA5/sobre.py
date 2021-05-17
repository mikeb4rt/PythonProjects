class sobre():
    def __init__(self, identificador, nom, descripcio, preu):
        self.identidicaro = identificador
        self.nom = nom
        self.descripcio = descripcio
        self.preu = preu
        self.cartes = []

    def añadirCarta(self, cart):
        self.cartes.append(cart)

    def veureCartes(self):
        for x in self.cartes:
            print(f" Nom: {x.getNom()} Tipus: {x.getTipus()} Raresa: {x.getRaresa()}")