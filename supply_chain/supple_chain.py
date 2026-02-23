class Firm(object):
    def __init__(self, name, cash, inventory):
        self.name = name
        self.cash = cash
        self.inventory = inventory
     
    def transact(self,other,item,amount):
        price = other.inventory[item]['price']
        total_price = price * amount
        if self.cash < total_price:
            print(f"{self.name} has insufficient funds to pay ${total_price:.2f}")
        if other.inventory[item]['quantity'] < amount:
            print(f"{other.name} cannot fulfill this order")

        if self.cash >= total_price and amount <= other.inventory[item]['quantity']:
            other.cash += total_price
            self.cash -=  total_price
            other.inventory[item]['quantity'] -= amount
            if item in self.inventory:
                self.inventory[item]['quantity'] += amount
            else:
                self.inventory[item]= {'quantity': amount, 'price' : price }
            print(f"{self.name} paid ${total_price:.2f} for {amount} {item}")



        