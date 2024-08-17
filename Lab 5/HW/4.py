class Shopidify:
    def __init__(self,n=None):
        self.n = n
        self.cart = {}
        if self.n == None:
            self.n = "Guest"
            print("Welcome to Shopidify")
        else:
            print(f"Welcome {self.n} to Shopidify")

    def add_to_cart(self,*item):
        if len(item) == 1:
            if type(item[0]) == str:
                if item[0] not in self.cart:
                    self.cart[item[0]] = 1
                else:
                    self.cart[item[0]] += 1

            elif type(item[0]) == list:
                for i in range(0,len(item[0]),2):
                    if item[0][i] not in self.cart:
                        self.cart[item[0][i]] = item[0][i+1]
                    else:
                        self.cart[item[0][i]] += item[0][i+1]

        else:
            for i in range(0,len(item),2):
                if item[i] not in self.cart:
                    self.cart[item[i]] = item[i+1]
                else:
                    self.cart[item[i]] += item[i+1]

    def display_cart(self):
        print(f"Items in the cart for {self.n}:")
        for k,v in self.cart.items():
            print(f"- {k}: {v}x")

    def checkout(self):
        print(f"Checkout completed for {self.n}")

    def display_history(self):
        print(f"Purchase history for {self.n}:\nTransaction 1:")
        for k,v in self.cart.items():
            print(f"- {k}: {v}x")

guest_account = Shopidify()
print("1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account = Shopidify("John")
print("2xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan", 2)
guest_account.add_to_cart("Luffy Action Figure")
guest_account.display_cart()
print("3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.add_to_cart(["Chocolate Chip Cookies", 3,"Goku Action Figure",2,"Dumbbells-5kg",2])
john_account.display_cart()
print("4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan")
guest_account.display_cart()
print("5xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.checkout()
print("6xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.display_history()
print("7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.checkout()
print("8xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.display_history()
print("9xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")