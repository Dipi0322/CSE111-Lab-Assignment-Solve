def palindrome(s):
  new_s = ""
  for i in s:
    if i != " ":
      new_s += i

  mid = len(new_s) // 2

  new1 = ""
  for j in range(mid):
    new1 += new_s[j]

  new2 = ""
  for k in range(len(new_s)-1,mid,-1):
    new2 += new_s[k]

  if new1 == new2:
    return "Palindrome"
  else:
    return "Not a palindrome"

string = input("")
print(palindrome(string))