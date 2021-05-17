from Auction.Bargain.Bargain import bargain
from Auction.Bid.Bid import bid
from Auction.Users.User import user

Toni = user("Toni", 100)
Pep = user("Pep", 150)
Enric = user("Enric", 300)

mobil = bargain("Teléfono mobil", Toni, "true")
mobil.userBid(Pep, 100)

for x in range(len(mobil.getBids())):
    print(mobil.getBids()[x].toString())

mobil.userBid(Enric, 50)

for x in range(len(mobil.getBids())):
    print(mobil.getBids()[x].toString())

mobil.finishBid()
mobil.userBid(Enric, 200)

impresora = bargain("impresora", Pep, "true")
impresora.bidDog(Enric)
impresora.finishBid()

users = [Toni, Pep, Enric]
for u in range(len(users)):
    print(users[u].toString())
