
s = input("")

temp = []
for i in s.split(", "):
    temp += [i]

keys = []
values = []
for j in temp:
    k1,v1 = j.split(":")
    keys.append(k1)
    values.append(v1)

dic = {}
for a in range(len(keys)):
    for b in range(len(values)):
        if a == b:
            dic[keys[a]] = values[b]

v = []
for ke, va in dic.items():
    if va not in v:
        v.append(va)

new_dic = {}
for key, value in dic.items():
    if value not in new_dic:
        new_dic[value] = [key]
    else:
        new_dic[value].append(key)

print(new_dic)
