l1 = []
l2 = []

for j in range(2):
  s = input("")
  for i in (s.split(" ")):
    if j == 0:
      l1 += [int(i)]
    else:
      l2 += [int(i)]

l = []
for i in l1:
  for j in l2:
    cross = i * j
    l += [cross]

print(l)