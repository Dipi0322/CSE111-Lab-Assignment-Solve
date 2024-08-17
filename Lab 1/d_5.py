s1 = input("")
s2 = input("")

if len(s1) == len(s2):
    dic1 = {}
    dic2 = {}

    for i in range(len(s1)):
        dic1[s1[i]] = i

    for j in range(len(s2)-1,-1,-1):
        dic2[s2[j]]= j

    anagram = False
    for key1 in dic1.keys():
        for key2 in dic2.keys():
            if key1 == key2:
                v1 = dic1[key1]
                v2 = dic2[key2]
                sum = v1 + v2
                if sum == len(s1) - 1:
                    anagram = True
                else:
                    break
            elif key1 != key2:
                break

else:
    anagram = False
            
if anagram:
    print("Those strings are anagrams.")
else:
    print("Those strings are not anagrams.")

