import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

alphabet_list = [alphabet[i] for i in range(len(alphabet))]
#alphabet_list = list(alphabet)

print(alphabet_list)

message_text = "what is a baggins"

cipher_list = list(alphabet_list)
random.shuffle(cipher_list)

cipher_text = ""

for x in message_text:
    index = alphabet_list.index(x)
    cipher_char = cipher_list[index]
    cipher_text += cipher_char

print cipher_text

sdlk;abcdefghijklmnopqrstuvwxyz 