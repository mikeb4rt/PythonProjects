class user:

    def __init__(self, name, money):
        self.object = None
        self.name = name
        self.money = money

    def getName(self):
        return self.name

    def getMoney(self):
        return self.money

    def cash(self, salary):
        self.money = self.getMoney() + salary

    def pay(self, payment):
        self.money = self.getMoney() - payment

    def getObject(self):
        return self.object

    def toString(self):
        return f"Nombre: {self.getName()} Dinero: {self.getMoney()} Objeto: {self.getObject()}"
