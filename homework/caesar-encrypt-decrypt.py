# Week2 Day2 Homework

dict = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def ch_encrypt(input_ch, n):
    index_count = dict.index(input_ch)+n
    if(index_count >= len(dict)):
        index_count -= len(dict)
    return dict[index_count]

def caesar_encrypt(input_str, n):
    newStr = ""
    for ch in input_str:
        if(ch.isalpha()): 
            newStr += ch_encrypt(ch.upper(), n)
        else:
            newStr += ch
    return newStr

def ch_decrypt(input_ch, n):
    index_count = dict.index(input_ch)-n
    if(index_count < 0):
        index_count += len(dict)
    return dict[index_count]

def caesar_decrypt(input_str, n):
    newStr = ""
    for ch in input_str:
        if(ch.isalpha()): 
            newStr += ch_decrypt(ch.upper(), n)
        else:
            newStr += ch
    return newStr

print(caesar_encrypt("abc xyz !3", 2))
print(caesar_decrypt("abc xyz !3", 2))
