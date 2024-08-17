def pressing(s):
    dic = {
        1: ".,?!:",
        2: "ABC",
        3: "DEF",
        4: "GHI",
        5: "JKL",
        6: "MNO",
        7: "PQRS",
        8: "TUV",
        9: "WXYZ",
        0: " "
        }
    
    new_s = ""
    for a in s:
        x = ord(a)
        if 97 <= x <= 122:
            x -= 32
            y = chr(x)
            new_s += y
        else:
            new_s += a
    
    press = ""

    for i in new_s:
        for k, v in dic.items():
            if i in v:
                for j in range(len(v)):
                    if v[j] == i:
                        press += str(k) * (j + 1)

    return press

text = input("")
print(pressing(text))
