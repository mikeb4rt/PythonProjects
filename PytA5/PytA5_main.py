from carta import carta
from sobre import sobre
from caja import caja

Charizard = carta("Charizard", "Fuego", "super super rara", 190, 80, 100, "50% de quemar al contacto")
Pickachu = carta("Pickachu", "Electrico", "rara", 90, 45, 75, "55% de paralizar al oponente cuando ataca")
Eevee = carta("Eevee", "normal", "normal", 40, 40, 60, "Sus ataques del mismo tipo tienen un 100% mas de efectividad")
Dialga = carta("Dialga","Dragon", "legendaria", 220, 290, 300, "Tiene resistencia a todos los tipos")
Muk = carta("Muk", "Veneno", "super rara", 80, 150, 165, "Los ataques fisicos tienen un 50% menos de efectividad")

carts = [Charizard, Pickachu, Eevee, Dialga, Muk]

sobre1 = sobre("29/03/2021", "Poke1", "Cartas desde la 1 a la 4 gen", 2.99)
sobre2 = sobre("29/03/2021", "Poke2", "Cartas desde la 1 a la 4 gen", 2.99)
sobre3 = sobre("29/03/2021", "Poke3", "Cartas desde la 1 a la 4 gen", 2.99)
sobre4 = sobre("29/03/2021", "Poke4", "Cartas desde la 1 a la 4 gen", 2.99)
sobre5 = sobre("29/03/2021", "Poke5", "Cartas desde la 1 a la 4 gen", 2.99)

caja1 = caja("30/03/2021", "Primera caja")

sobre1.añadirCarta(Charizard)
sobre3.añadirCarta(Pickachu)
sobre5.añadirCarta(Eevee)
sobre2.añadirCarta(Dialga)
sobre4.añadirCarta(Muk)

caja1.añadirSobres(sobre1)
caja1.añadirSobres(sobre2)
caja1.añadirSobres(sobre3)
caja1.añadirSobres(sobre4)
caja1.añadirSobres(sobre5)

caja1.veureSobres()