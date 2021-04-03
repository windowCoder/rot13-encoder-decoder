# rot 13 encode/decode
# Populate alphabetList with upper and lowercase letters.
# 1. text <= 13 (a-m) can have 13 added to get the cipher (n-z)
# 2. text >= 12 (n-z) can have 13 subtracted to get the cipher (a-m)
alphabet, x, the_message = 'abcdefghijklmnopqrstuvwxyz', 0, ''
alphabetBoth, alphaLower, alphaUpper, msg = [], [], [], []

for i in alphabet:  # CREATE 3 alphabet lists; lowercase, uppercase, and both combined.
    alphaLower.append(alphabet[x])
    alphaUpper.append(alphabet[x].upper())
    alphabetBoth.append(alphabet[x].upper())
    alphabetBoth.append(alphabet[x].lower())
    x += 1

entry = input("[92mrot13 encode/decode \nentry: [0m")

for string in entry:    #  COMPARE each string and how it relates to the lists.
    if string in alphaLower:  # if string is LOWER case
        if alphaLower.index(string) >= 13:  # and high
            msg.append(alphaLower[alphaLower.index(string) - 13])
        else:
            msg.append(alphaLower[alphaLower.index(string) + 13])
    elif string in alphaUpper:  # if string is UPPER case
        if alphaUpper.index(string) >= 13:  # and high
            msg.append(alphaUpper[alphaUpper.index(string) - 13])
        else:
            msg.append(alphaUpper[alphaUpper.index(string) + 13])
    else:
        msg.append(string)

for k in msg:   # COMBINE list msg to form one string
    the_message += k

print(f"[92m{the_message}[0m ")
