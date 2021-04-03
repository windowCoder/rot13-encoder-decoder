# rot 13 encode/decode
# Populate alphabetList with upper and lowercase letters.
# 1. text <= 13 (a-m) can have 13 added to get the cipher (n-z)
# 2. text >= 12 (n-z) can have 13 subtracted to get the cipher (a-m)
alphabet, x, the_message = 'abcdefghijklmnopqrstuvwxyz', 0, ''
alphabetBoth, alphabetLow, alphabetHigh, msg = [], [], [], []

for i in alphabet:  # CREATE 3 alphabet lists; lowercase, uppercase, and both combined.
    alphabetLow.append(alphabet[x])
    alphabetHigh.append(alphabet[x].upper())
    alphabetBoth.append(alphabet[x].upper())
    alphabetBoth.append(alphabet[x].lower())
    x += 1

entry = input("[92mrot13 encode/decode \nentry: [0m")

for string in entry:    #  COMPARE each string and how it relates to the lists.
    if string not in alphabetBoth:  # non alphabet
        msg.append(string)
    elif string in alphabetLow:  # if string is LOWER case
        if alphabetLow.index(string) >= 13:  # and high
            msg.append(alphabetLow[alphabetLow.index(string) - 13])
        if alphabetLow.index(string) <= 12:  # or low
            msg.append(alphabetLow[alphabetLow.index(string) + 13])
    elif string in alphabetHigh:  # if string is UPPER case
        if alphabetHigh.index(string) >= 13:  # and high
            msg.append(alphabetHigh[alphabetHigh.index(string) - 13])
        if alphabetHigh.index(string) <= 12:  # or low
            msg.append(alphabetHigh[alphabetHigh.index(string) + 13])

for k in msg:   # COMBINE list msg to form one string
    the_message += k

print(f"[92m{the_message}[0m ")
