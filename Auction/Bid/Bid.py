class bid:

    def __init__(self, user, money):
        self.user = user
        self.money = money

    def getUser(self):
        return self.user

    def getMoney(self):
        return self.money

    def toString(self):
        return f"Usuario: {self.getUser().getName()} Puja: {self.getMoney()}"
