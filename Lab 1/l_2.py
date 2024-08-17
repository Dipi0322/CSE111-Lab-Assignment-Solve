n = int(input(""))
k = 1
sum = None
max_l = None
while k <= n:
  s = input("")
  summation = 0
  l = []
  for i in (s.split(" ")):
    summation += int(i)
    l += [int(i)]
  if sum == None or summation > sum:
    sum = summation
    max_l = l
  else:
    l = []
  k += 1

print(sum)
print(max_l)
