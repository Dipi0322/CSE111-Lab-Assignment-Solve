def meal(item,place="Mohakhali"):
  dic = {"BBQ Chicken Cheese Burger":250,"Beef Burger":170,"Naga Drums":200}

  if item in dic.keys():
    meal_cost = dic[item]
    if place == "Mohakhali":
      delivery = 40
    else:
      delivery = 60
    tax = meal_cost * (8/100)

    total = meal_cost + delivery + tax
    return total

  else:
    return "Item not in menu"

item = input("")
place = input("")
print(meal(item,place))