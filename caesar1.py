def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter in alphabet:
       position = alphabet.find(letter)
    elif letter in ALPHABET:
       position = ALPHABET.find(letter)
    return position


def rotate_character(char,rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


    new = (alphabet_position(char) + int(rot))%26
    if char in alphabet:
        return alphabet[new]
    elif char in ALPHABET:
        return ALPHABET[new]

def encrypt(text,rot):
    cipher = ''
    for ch in text:
        if ch.isalpha():
           cipher = cipher + rotate_character(ch,rot)
        else:
           cipher = cipher + ch
    return cipher
