class Price:
    def final_price(self, vat, discount=0):
        return (self.net_price * (100 + vat) / 100 ) - discount

price1 = Price()
price1.net_price = 100
print(Price.final_price(price1, 20, 10))
print(price1.final_price(20, 10))