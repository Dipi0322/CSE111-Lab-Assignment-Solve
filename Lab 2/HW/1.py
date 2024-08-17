def hospital_fee(**kwargs):
    max_amount = None
    max_payer = []

    for k,v in kwargs.items():
        if max_amount == None or v > max_amount:
            max_amount = v
            max_payer = [k]
        elif v == max_amount:
            max_payer += [k]

    return max_amount,max_payer

max_amount, max_payer = hospital_fee(Neymar =1000, Dembele = 600, Reus = 500, Bale = 1000)
new_s = f"Highest fee was {max_amount} tk which was paid by "
for i in range(len(max_payer)):
    if i == 0:
        new_s += max_payer[i]
    else:
        new_s += ", " + max_payer[i]

print(new_s)