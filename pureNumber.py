def pureNumber(n):
    i = 1
    while n > 0 and i > 0:
        nstr = str(i)
        count = 0
        for x in nstr:
            if x == '4' or x == '5':
                count += 1
        if count == len(nstr) and count%2 == 0:
            m = nstr[::-1]
            if m == nstr:
                n -= 1
                if n == 0:
                    return i
        i += 1
x = int(input("no of inputs"))
for i in range(x):
    y = int(input("nth pure number"))
    print(pureNumber(y))
