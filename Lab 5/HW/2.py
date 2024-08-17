class Foodie:
    def __init__(self,name):
        self.name = name
        self.l = []
        self.total = 0

    def order(self,*s):
        for i in s:
            self.price = 0
            item,quantity = i.split("-")
            self.l.append(item)
            for k,v in menu.items():
                if item == k:
                    self.price += v * int(quantity)
                    self.total += self.price
                    print(f"Ordered - {item}, quantity - {quantity}, \nprice (per Unit) - {v}.\nTotal price - {self.price}")

    def show_orders(self):
        return f"{self.name} has {len(self.l)} item(s) in the cart.\nItems: {self.l}\nTotal Spent: {self.total}"
    
    def pay_tips(self,n=None):
        if n != None:
            self.total += n
            print(f"Gives {n}/- tips to the waiter.")
        else:
            print("No tips to the waiter.")

menu = {'Chicken Lollipop':15,'Beef Nugget':20,'Americano':180,'Red Velvet':150,'Prawn Tempura':80,'Saute Veg':200}


f1 = Foodie('Frodo')
print(f1.show_orders())
print('1----------------------')
f1.order('Chicken Lollipop-3','Beef Nugget-6','Americano-1')
print('2----------------------')
print(f1.show_orders())
print('3----------------------')
f1.order('Red Velvet-1')
print('4----------------------')
f1.pay_tips(20)
print('5----------------------')
print(f1.show_orders())
f2 = Foodie('Bilbo')
print('6----------------------')
f2.order('Prawn Tempura-6','Saute Veg-1')
print('7----------------------')
f2.pay_tips()
print('8----------------------')
print(f2.show_orders())

