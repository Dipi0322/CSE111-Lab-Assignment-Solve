class KK_tea:
    sales = {"KK Regular Tea": 0}

    def __init__(self,price,bag=50):
        self.name = "Regular"
        self.price = price
        self.bag = bag
        self.weight = self.bag * 2
        self.status = False

    def product_detail(self):
        print(f"Name: KK {self.name} Tea, Weight: {self.weight}\nTea Bags: {self.bag}, Price: {self.price}\nStatus: {self.status}")

    @classmethod
    def total_sales(cls):
        print(f"Total sales: {cls.sales}")

    @classmethod
    def update_sold_status_regular(cls,*obj):
        for i in obj:
            i.status = True
            if f"KK {i.name} Tea" not in cls.sales:
                cls.sales[f"KK {i.name} Tea"] = 1
            else:
                cls.sales[f"KK {i.name} Tea"] += 1

class KK_flavoured_tea(KK_tea):
    def __init__(self, name, price, bag=50):
        super().__init__(price, bag)
        self.name = name

    def product_detail(self):
        super().product_detail()

    @classmethod
    def update_sold_status_flavoured(cls,*obj):
        super().update_sold_status_regular(*obj)

t1 = KK_tea(250)
print("-----------------1-----------------")
t1.product_detail()
print("-----------------2-----------------")
KK_tea.total_sales()
print("-----------------3-----------------")
t2 = KK_tea(470, 100)
t3 = KK_tea(360, 75)
KK_tea.update_sold_status_regular(t1, t2, t3)
print("-----------------4-----------------")
t3.product_detail()
print("-----------------5-----------------")
KK_tea.total_sales()
print("-----------------6-----------------")
t4 = KK_flavoured_tea("Jasmine", 260, 50)
t5 = KK_flavoured_tea("Honey Lemon", 270, 45)
t6 = KK_flavoured_tea("Honey Lemon", 270, 45)
print("-----------------7-----------------")
t4.product_detail()
print("-----------------8-----------------")
t6.product_detail()
print("-----------------9-----------------")
KK_flavoured_tea.update_sold_status_flavoured(t4, t5, t6)
print("-----------------10-----------------")
KK_tea.total_sales()

