# rot 13 encode/decode
# 13 subtracted to get the cipher (a-m) >= 12 message <= 13 (a-m) + 13 to get the cipher (n-z)
message = input("[92mrot13 encode/decode \nentry: [0m")
def rot13(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    msg = ''
    for i in message:
        if i in alphabet:
            if alphabet.index(i) <= 12:
                msg += alphabet[alphabet.index(i) + 13]
            else:
                msg += alphabet[alphabet.index(i) - 13]
        elif i in alphabet.upper():
            if alphabet.upper().index(i) <= 12:
                msg += alphabet.upper()[alphabet.upper().index(i) + 13]
            else:
                msg += alphabet.upper()[alphabet.upper().index(i) - 13]
        else:
            msg += i
    return msg
print(f"[92m{rot13(message)}[0m ")
