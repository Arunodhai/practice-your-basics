sentence= input("Enter a string : ")
letters=digits=0
for sen in sentence:
    if sen.isdigit():
        digits=digits+1
    elif sen.isalpha():
        letters=letters+1
    else:
        pass
print("Number of Letters : ",letters)
print("Number of Digits : ",digits)