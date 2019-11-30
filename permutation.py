from itertools import permutations
def strpermutation(str):
    permlist = permutations(str)
    allwords = []
    for perm in list(permlist):
        x = ''.join(perm)
        if x not in allwords:
            allwords.append(x)
        else:
            continue
        counta = 3
        countb = 0
        if(x == 'saaa'):
            for y in x:
                if  y == 'a':
                    counta += 1
                    print(counta)
                else:
                    countb += 1
                    print(countb)
            print(counta)
            print(countb)
            if(counta < (3*countb)):
                allwords.remove(x)
    print(allwords)



c = "aaas"
strpermutation(c)