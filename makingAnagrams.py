def makingAnagrams(s1, s2):
    delete = 0
    for char in s1:
        if char in s2:
            s2 = s2.replace(char, '', 1)
        else:
            delete += 1
    delete += len(s2)
    return delete
print(makingAnagrams("cde", "abc"))