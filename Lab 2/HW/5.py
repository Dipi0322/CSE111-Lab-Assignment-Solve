def key_generator(*employees):
    keys = []
    key = ""
    temp = ""

    for employee in employees:
        length = len(employee)
        x = ord(employee[0])
        if 65 <= x <= 90:
            x += 32
            temp += chr(x)
        else:
            temp += employee[0]

        for i in range(-2,-length,-1):
            z = ord(employee[i])
            temp += str(z)

        y = ord(employee[length-1])
        if 97 <= x <= 122:
            y -= 32
            temp += chr(y)
        else:
            temp += employee[length-1]

        keys.append(temp)
        temp = ""
        
    return keys
    
key_list = key_generator ("Alex","Bob", "Trudy")
print(f"Encrypted Keys: {key_list}")