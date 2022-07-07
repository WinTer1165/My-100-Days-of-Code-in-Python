class Computer:

    def __init__(self):
        self.maxprice = 900

    def sell(self):
        print(f"Selling Price: {self.maxprice}")

    def setMaxPrice(self, price):
        self.maxprice = price


c = Computer()
c.sell()

# change the price
c.maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
