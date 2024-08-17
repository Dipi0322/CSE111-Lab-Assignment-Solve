class Cakes:
    order_list = {}
    feedbacks = {}
    def __init__(self,flavor,w):
        self.flavor = flavor
        self.w = w
        self.sweetness = "Moderate"
        self.cream = "Whipped Cream"
        self.price = 1.2
        if f"{self.flavor} Cake {self.w}gm" not in Cakes.order_list:
            Cakes.order_list[f"{self.flavor} Cake {self.w}gm"] = 1
        else:
            Cakes.order_list[f"{self.flavor} Cake {self.w}gm"] += 1

    def add_customization(self,sweetness=None,cream=None):
        self.sweetness = sweetness
        self.cream = cream

    @classmethod
    def give_feedbacks(cls,flavor,comment):
        if flavor not in cls.feedbacks:
            cls.feedbacks[flavor] = [comment]
        else:
            cls.feedbacks[flavor].append(comment)
        print("Thanks for your valuable feedback!")

    @classmethod
    def show_feedbacks(cls):
        print(cls.feedbacks)

    def cake_details(self):
        print(f"Flavor: {self.flavor} Cake, Weight: {self.w} gm\nSweetness: {self.sweetness} sugar, Cream Type: {self.cream}\nPrice: {self.w * self.price} Taka")

class Cheese_Cakes(Cakes):
    def __init__(self, flavor, w, type="baked"):
        flavor = flavor + " Cheese"
        super().__init__(flavor, w)
        self.cream = "Cream Cheese"
        self.type = type
        self.price = 1.5
        
    def add_customization(self, sweetness=None, cream=None):
        print(f"Sorry! No customization available for cheese cakes.")
    
    def cake_details(self):
        print(f"Flavor: {self.flavor} Cake, Weight: {self.w} gm\nSweetness: {self.sweetness} sugar, Cream Type: {self.cream}\nCake Type: {self.type}, Price: {self.w * self.price} Taka")

    @classmethod
    def give_feedbacks(cls, flavor, comment):
        super().give_feedbacks(flavor, comment)
        print(f"You will get 10% discount for your next purchase!")
    
order_1=Cakes("Chocolate",500)
order_2=Cakes("Vanilla",800)
print("(1)**********************************")
order_1.cake_details()
print("(1.1)**********************************")
print(Cakes.order_list)
print("(2)**********************************")
order_2.add_customization("Zero","Butter Cream")
order_2.cake_details()
print("(3)**********************************")
Cakes.give_feedbacks("Chocolate Cake","Very Delicious")
Cakes.give_feedbacks("Chocolate Cake","Yummy")
print("(4)**********************************")
Cakes.show_feedbacks()
print("(5)**********************************")
ch_order1=Cheese_Cakes("Red velvet",700)
ch_order1.cake_details()
print("(6)**********************************")
ch_order1.add_customization()
print("(7)**********************************")
ch_order2=Cheese_Cakes("Blue Berry",900,"No Bake")
ch_order2.cake_details()
print("(8)**********************************")
print(Cakes.order_list)
print("(9)**********************************")
Cheese_Cakes.give_feedbacks("Red velvet Cheese Cake","Average")
Cheese_Cakes.give_feedbacks("Blue Berry Cheese Cake","Liked it")
print("(10)**********************************")
Cakes.show_feedbacks()

