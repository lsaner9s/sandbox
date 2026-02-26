class Firm(object):
    def __init__(self, name, cash, inventory, market_hub, industry):
        self.name = name
        self.cash = cash
        self.inventory = inventory
        self.industry = industry
        market_hub.register_participant(self)
     
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

class Market(object):
    def __init__(self):
        self.participants = []
    def register_participant(self, participant):
        if participant not in self.participants:
            self.participants.append(participant)

class TechFirm(Firm):
    def input_procurement(self,amount):
        sellers = []
        for firm in self.market_hub.participants:
            if firm.type == 'mining':
                if firm.inventory['silicon']['quantity'] > 0:
                    sellers.append(firm)
        sellers.sort(key=lambda firm: firm.inventory['silicon']['price'])

        for miner in sellers:
            if amount <= 0:
                print(f"Order for {amount} silicon fulfilled")
                break
            miner_inventory = miner.inventory['silicon']['quantity']
            price = miner.inventory['silicon']['price']

            order = min(amount, miner_inventory)
            cost = order * price

            if self.cash >= cost:
                self.transact(miner,'silicon',order)
                amount -= order
                print(f"Bought {amount} of silicon from {miner.name} at ${price} per unit")
            else:
                print(f"Ran out of cash while procuring materials")
                break
        if amount > 0:
            print(f"Due to a market shortage we were unable to procure necessary inputs")

    def produce(self,amount):
        silicon_stock = self.inventory['silicon']['quantity']
        silicon_needed = amount * 5

        if silicon_stock < silicon_needed:
            order = silicon_needed - silicon_stock
            initial_cash = self.cash
            self.input_procurement(order)
            procurment_cost = initial_cash - self.cash
        if self.inventory['silicon']['quantity'] < silicon_needed:
            print(f"Failed to secure necessary inputs to fulfill orders")
        else:
            self.inventory['silicon']['quantity'] -= silicon_needed
            self.inventory['chips']['quantity'] += amount
            chip_cost = (procurment_cost / amount)*0.30 + (procurment_cost / amount)
            self.inventory['chips']['price'] = chip_cost if chip_cost > self.inventory['chips']['price'] else self.inventory['chips']['price']

class Miner(Firm):
    def mine(self, amount,item):
        cost_to_mine = amount * 4
        if self.cash >= cost_to_mine:
            self.cash -= cost_to_mine
            if item in self.inventory:
                self.inventory[item]['quantity'] += amount
            else:
                price = (cost_to_mine/amount) * 0.10 + (cost_to_mine/amount)
                self.inventory[item]= {'quantity': amount, 'price' : price }
        else:
            print(f"Insufficient funds to mine")
        
