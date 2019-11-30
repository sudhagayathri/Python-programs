secret_word = "jaisriram"
min_count = 0
your_word = ""
out_ofguesses = False
while your_word != secret_word and not(out_ofguesses):
    your_word =input("guess the secret word")
    min_count += 1
    if min_count > 5:
        out_ofguesses = True

if(not(out_ofguesses)):
    print("you win")
else:
    print("exceeded limit")

