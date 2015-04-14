alphabet = "abcdefghijklmnopqrstuvwxyz "

alphabet_list = [alphabet[i] for i in range(len(alphabet))]
# alphabet_list = list(alphabet)

print(alphabet_list)

message_text = "hello world"

# cipher_list = list(alphabet_list)
# random.shuffle(cipher_list)

cipher_list = ['v', 'y', 'h', 'l', 'a', 'n', 'i', 'g', 'e', 'd', 'k', 'c', 'w', ' ', 'f', 's', 'm', 'p', 'r', 't', 'o', 'u', 'z', 'b', 'j', 'x', 'q']


def encrypt(message_text):
    cipher_text = ""
    for x in message_text:
        index = alphabet_list.index(x)
        cipher_char = cipher_list[index]
        cipher_text += cipher_char
    return cipher_text


def decrypt(cipher_text):
    code_message = ""
    for x in cipher_text:
        index = cipher_list.index(x)
        cipher_char = alphabet_list[index]
        code_message += cipher_char
    return code_message

cipher_text = "rawsapqsj"
print decrypt(cipher_text)
# puzzle is to decypt it, given a Key
# 1. assign a standard key
# 2. print out a cypher ???
