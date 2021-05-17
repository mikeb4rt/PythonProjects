class ca():
    #Constructor
    def __init__(self, energia, fam, estat):
        self.energia = energia
        self.fam = fam
        self.estat = estat

    #Getter todos los atributos
    def getAll(self):
        print(f"Energia: {self.energia} Fam: {self.fam} Estat: {self.estat}")

    #Metode menjar si el ca te gana subira el seu medidor de fam en conseqüencia a la quantitat especificada
    def menjar(self, cantidad):
        if self.estat == "famolenc":
            if self.fam + cantidad >= 3:
                self.fam = 3
            else:
                self.fam = self.fam + cantidad
        else:
            print("Es ca no esta famolenc")

    #Cambia l'estat a content y mostra l'estat actual des ca
    def acariciar(self):
        self.estat = "content"
        print(self.estat)

    #Si el ca no esta famolenc y te energia y gana suficients jugara y subira el seu estat de gana en 1 y la seva energia es reduira en 1
    def jugar(self):
        if self.energia <= 2 or self.fam >= 2 or self.estat == "famolenc":
            print("Es ca no vol jugar")
        else:
            self.energia = self.energia - 1
            self.fam = self.fam + 1
            self.estat = "famolenc"

    #Si es ca esta lo suficienment cansat dormirá y aumentara la seva energia el nombre d'hores que s'an especificat
    def dormir(self, hores):
        if self.energia < 2:
            if self.energia + hores >= 5:
                self.energia = 5
            else:
                self.energia = self.energia + hores
            self.estat = "famolenc"
        else:
            print("Es ca no esta cansat no s'en va a dormir")

