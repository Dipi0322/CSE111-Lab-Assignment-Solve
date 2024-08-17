def paragraph(s):
  char = ".!?"
  temp = ""
  new_s = ""

  for i in range(len(s)):
    if i == 0:
      x = ord(s[i])
      if 97 <= x <= 122:
        y = chr(x-32)
        new_s += y

    elif (s[i-1] == " " and s[i-2] in char) or (s[i-1] == " " and s[i+1] == " " and s[i] == "i"):
      x = ord(s[i])
      if 97 <= x <= 122:
        y = chr(x-32)
        new_s += y

    else:
      new_s += s[i]

  return new_s

print(paragraph("my fav animal is i dog. how are you? i am fine!"))