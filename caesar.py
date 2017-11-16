def alphabet_position(yertext):

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #yertext = yertext.lower()
    alphaindex = 0

    for i in range(len(alphabet)):

        if yertext == alphabet[i]:
            return i % 26
        if yertext not in alphabet:
            return None
        # print(i, alphabet[i])

def rotate_character(char,rot):
    originalPosition = 0
    newPosition = 0
    newChar = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if char not in alphabet:

        return char

    originalPosition = alphabet_position(char)
    newPosition = (originalPosition + rot) % 26

    newChar = alphabet[newPosition]

    if char.isupper(): #preserve case

        return newChar.upper()

    else:

        return newChar

def rotate_string(yourInput, rotate):

    caesarOutput = ""
    for i in yourInput:

        caesarOutput = caesarOutput + rotate_character(i,rotate)

    return caesarOutput