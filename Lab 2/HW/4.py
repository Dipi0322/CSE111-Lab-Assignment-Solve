def username_generator(first_name,last_name,student_id,middle_name=""):
    username = ""

    if len(first_name) <= 3:
        for i in first_name:
            x = ord(i)
            if 97 <= x <= 122:
                x -= 32
                y = chr(x)
                username += y
            else:
                username += i

    else:
        for i in range(3):
            x = ord(first_name[i])
            if 97 <= x <= 122:
                x -= 32
                y = chr(x)
                username += y
            else:
                username += first_name[i]

    username += middle_name

    for j in range(-3,0,1):
        username += last_name[j]

    username += "_"
    student_id = str(student_id)
    
    for k in range(-4,0,1):
        username += str(student_id[k])

    return username

first_name, middle_name, last_name, student_id= input ("First Name:"), input("Middle Name:"), input ("Last Name:"), int (input ("Student ID:"))
print(username_generator (first_name, last_name, student_id))
print(username_generator(first_name, last_name, student_id, middle_name))