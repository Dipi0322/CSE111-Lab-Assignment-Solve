def is_james_bond(l):
    bond = "007"
    new_s = ""

    for i in l:
        if i == 0 or i == 7:
            new_s += str(i)

    if bond in new_s:
        print("True")
    else:
        print("False")
    

is_james_bond( [1, 2, 4, 0, 0, 7, 5] )