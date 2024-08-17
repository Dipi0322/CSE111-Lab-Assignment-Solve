def assign_students_to_sections(section,*student):
    dic = {}
    for i in section:
        dic[i] = []

    length_s = len(section)
    for j in student:
        sum = 0
        for k in j:
            x = ord(k)
            sum += x

        num_of_sec = sum % length_s

        for a in range(length_s):
            if a == num_of_sec:
                for key,val in dic.items():
                    if section[a] == key:
                        val.append(j)

    print(dic)

assign_students_to_sections('ABCDE', 'Alice','Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace')