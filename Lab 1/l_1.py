list = []

while True:
  s = input("")
  if s != "STOP":
    list += [s]
  elif s == "STOP":
    break

list1 = []
for j in list:
  if j not in list1:
    list1 += [j]
  else:
    continue

count = 0
list2 = []
for k in list1:
  for i in list:
    if k == i:
      count += 1
    else:
      continue
  list2 += [count]
  count = 0

for j in range(len(list1)):
  for k in range(len(list2)):
    if j == k:
      print(f"{list1[j]} - {list2[k]} times")