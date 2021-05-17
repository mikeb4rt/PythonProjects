class caja():

    def __init__(self, id, descripcio):
        self.IdCaja = id
        self.descripcio = descripcio
        self.sobres = []

    def añadirSobres(self, sobre):
        self.sobres.append(sobre)

    def veureSobres(self):
        for x in self.sobres:
            x.veureCartes()