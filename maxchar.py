def getmaxchar(string):
    max = -1
    count = [0] * ASCII_SIZE
    print(count)
    maxvar = ''
    for i in string:
        count[ord(i)]+= 1
        if (max < count[ord(i)] or (max == count[ord(i)]) and ord(i) < ord(maxvar)):
            max = count[ord(i)]
            maxvar = i
    return maxvar
ASCII_SIZE = 180
noofinputs = input()
stringarr = []
count = 0
while(count < int(noofinputs)):
    x = input()
    x.upper()
    stringarr.append(x)
    count = count + 1
for string in stringarr:
    c = getmaxchar(string)
    print(c)


#1st input - integer of no of inputs
#2nd input - string/strings for which max character is to be found