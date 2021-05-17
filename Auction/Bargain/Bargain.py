from Auction.Bid.Bid import bid


class bargain:

    def __init__(self, name, user, status):
        self.name = name
        self.user = user
        self.status = status
        self.bids = []
        user.object = name

    def getName(self):
        return self.name

    def getUser(self):
        return self.user

    def getStatus(self):
        return self.status

    def getBids(self):
        return self.bids

    def getTopBid(self):
        topbid = 0
        for x in range(len(self.bids)):
            if self.bids[x].getMoney() > topbid:
                topbid = self.bids[x].getMoney()
        return topbid

    def getWinner(self):
        winner = 0
        for x in range(len(self.bids)):
            if self.bids[x].getMoney() > winner:
                winner = self.bids[x].getUser()
        return winner

    def addBid(self, user, money):
        newBid = bid(user, money)
        self.getBids().append(newBid)

    def userBid(self, user, money):
        if self.getStatus() == "true":
            if user.getMoney() >= money:
                if self.getUser() != user:
                    if len(self.getBids()) == 0:
                        self.addBid(user, money)
                    elif self.getWinner().getMoney() > user.getMoney():
                        self.addBid(user, money)
                    else:
                        print("La puja actual es mas alta")
                else:
                    print("El propietario no puede pujar")
            else:
                print("El usuario no tiene suficiente dinero")
        else:
            print("La subasta esta cerrada")

    def bidDog(self, user):
        if self.getStatus() == "true":
            if user.getMoney() >= self.getTopBid():
                if self.getUser != user:
                    if len(self.getBids()) > 0:
                        self.addBid(user, 1)
                    else:
                        dog = self.getTopBid() + 1
                        self.addBid(user, dog)
                else:
                    print("El propietario no puede pujar")
            else:
                print("La puja actual es mas alta")
        else:
            print("La subasta esta cerrada")

    def finishBid(self):
        if self.getStatus() == "true":
            if len(self.bids) > 0:
                self.status = "false"
                winner = self.getWinner()
                winner.pay(self.getTopBid())
                print(f"El ganador es: {self.getWinner().getName()}")
            else:
                print("No hay pujas")
        else:
            print("La subasta ya esta cerrada")