list = []

while True:
  s = input("")
  if s != "STOP":
    l = []
    for i in (s.split(" ")):
      l += [int(i)]
    l1 = []
    for j in range(len(l)):
      if j != len(l) -1:
        abs_diff = abs(l[j+1] - l[j])
        l1 += [abs_diff]
      elif j == len(l) - 1:
        continue
    for k in l1:
      if 1 <= k <= 4:
        ub_jumper = True
      else:
        ub_jumper = False
        break
    if ub_jumper:
      list += ["UB Jumper"]
    else:
      list += ["Not UB Jumper"]

  elif s == "STOP":
    break

for i in list:
  print(i)
