dic = {}

while True:
  s = input("")
  if s != "STOP":
    if s not in dic:
      dic[s] = 1
    elif s in dic:
      dic[s] = dic[s] + 1
  elif s == "STOP":
    break

for k,v in dic.items():
  print(f"{k} - {v} times")