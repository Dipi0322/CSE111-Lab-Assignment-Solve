a = input("")
b = input("")

l1 = []
l2 = []
s = "0123456789"

for i in a:
    if i in s:
        l1 += [int(i)]
    elif i == " ":
        continue

for j in b:
    if j in s:
        l2 += [int(j)]
    elif j == " ":
        continue

count = 0
for k in l2:
    sum = k + l1[1]
    if sum <= 5:
        count += 1

num_of_teams = count // 3
print(num_of_teams)

