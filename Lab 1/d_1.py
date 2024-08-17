dic1 = {}
dic2 = {}

for a in range(2):
    s = input("")

    for i in s.split(", "):
        k,v = i.split(":")
        if a == 0:
            dic1[k] = int(v)
        elif a == 1:
            dic2[k] = int(v)

new_dic= {}
for key1,val1 in dic1.items():
    new_dic[key1] = val1

for key2,val2 in dic2.items():
    if key2 in new_dic:
        new_dic[key2] = new_dic[key2] + val2
    else:
        new_dic[key2] = val2

l = []
for key,val in new_dic.items():
    l += [val]

new_l = []
for j in l:
    if j in new_l:
        continue
    else:
        new_l += [j]

sorted_l = sorted(new_l)

print(new_dic)
print(f"Values: {tuple(sorted_l)}")
