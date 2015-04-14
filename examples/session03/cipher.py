import random

alphabet = "abcdefghijklmnopqrstuvwxyz "

alphabet_list = [alphabet[i] for i in range(len(alphabet))]
#alphabet_list = list(alphabet)

#print(alphabet_list)

message_text = "hello"

<<<<<<< HEAD
cipher_list =['v', 'y', 'h', 'l', 'a', 'n', 'i', 'g', 'e', 'd', 'k', 'c', 'w', ' ', 'f', 's', 'm', 'p', 'r', 't', 'o', 'u', 'z', 'b', 'j', 'x', 'q']
=======
cipher_list = ['v', 'y', 'h', 'l', 'a', 'n', 'i', 'g', 'e', 'd', 'k', 'c', 'w', ' ', 'f', 's', 'm', 'p', 'r', 't', 'o', 'u', 'z', 'b', 'j', 'x', 'q']
>>>>>>> 6d22b5c1ca727e30378ed07ffb7a9fc067aa46d3

cipher_text = ""

for x in message_text:
    index = alphabet_list.index(x)
    cipher_char = cipher_list[index]
    cipher_text += cipher_char

print cipher_text
<<<<<<< HEAD
=======

new_cipher_text = "eqzergqtgvtqeqgvlqrfwaqa hgecvlvrqpeigtq fz"
decrypt_text = ""

for y in new_cipher_text:
    index = cipher_list.index(y)
    decrypt_char = alphabet_list[index]
    decrypt_text += decrypt_char

print decrypt_text












>>>>>>> 6d22b5c1ca727e30378ed07ffb7a9fc067aa46d3
