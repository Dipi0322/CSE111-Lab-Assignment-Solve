s = input("")
upper = ""
lower = ""
digit = ""

for i in s:
  x = ord(i)
  if 48 <= x <= 57:
    digit += i
  elif 65 <= x <= 90:
    upper += i
  elif 97 <= x <= 122:
    lower += i

new = ""
for j in sorted(lower):
  new += j
for k in sorted(upper):
  new += k
for n in sorted(digit):
  if int(n) % 2 != 0:
    new += n
for l in sorted(digit):
  if int(l) % 2 == 0:
    new += l

print(new)