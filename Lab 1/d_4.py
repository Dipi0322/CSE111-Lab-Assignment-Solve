s = input("")
new_s = ""

for i in s:
    x = ord(i)
    if 65 <= x <= 90:
        x += 32
        y = chr(x)
        new_s += y
    else:
        new_s += i

dic = {}
for j in new_s:
    if j == " ":
        continue
    elif j not in dic:
        dic[j] = 1
    elif j in dic:
        dic[j] = dic[j] + 1
print(dic)