from collections import Counter

cipherText_dic = {"Affine": 1, "Multiplicative": 2, "Additive": 3, "Hill": 4, "Vigenere": 5,
                  "Rivest-Shamir-Alderman": 6}

# Reference functions:

# Calculates IC of text, returns decimal value
def calc_ic(text):
    counts = Counter(text)
    num = 0.0
    den = 0.0
    for val in counts.values():
        i = val
        num += i * (i - 1)
        den += i
    if den == 0.0:
        return 0.0
    else:
        return num / (den * (den - 1))

# Encrypts letter A = 1
def enc_letter(letter):
    return ord(letter.lower()) - 96

# Decrypts letter A = 1
def dec_letter(letter):
    if letter == 0:
        letter = 26
    return chr(letter + 96)

# Frequency Analysis
def get_frequency(text):
    return Counter(text)



# def cipher_text():
#     switcher = {
#         1: "Affine",
#         2: "Multiplicative",
#         3: "Additive",
#         4: "Vigenere",
#         5: "Hill",
#         6: "Rivest-Shamir-Alderman"
#     }


def add(num1, num2, mod=26):
    return (num1 + num2) % mod


def multiply(num1, num2, mod=26):
    return (num1 * num2) % mod


def encrypt_with_additive(plain_text, n, block_size):
    cipher_text = ''
    for index in range(len(plain_text)):
        letter = enc_letter(plain_text[index].lower())
        cipher_text += dec_letter(add(letter, n)).upper()
        if index != 0 and (index - 1) % block_size == 0:
            cipher_text += " "
    return cipher_text


def encrypt_with_multiplicative(plain_text, n, block_size):
    cipher_text = ''
    for index in range(len(plain_text)):
        letter = enc_letter(plain_text[index].lower())
        cipher_text += dec_letter(multiply(letter, n)).upper()
        if index != 0 and (index - 1) % block_size == 0:
            cipher_text += " "
    return cipher_text


def encrypt_with_affine(plain_text, n, r, block_size):
    plain_text = encrypt_with_additive(plain_text, n, block_size)
    plain_text = encrypt_with_multiplicative(plain_text.replace(" ", ''), r, block_size)
    return plain_text
 
def encrypt_with_hill(plain_text, matrix):
    cipher=''
    if len(plain_text)%2==1:
        plain_text+='z'
    for index in range(0,len(plain_text),2):
        plain_letter1 = enc_letter(plain_text[index])
        plain_letter2 = enc_letter(plain_text[index+1])
        cipher_letters = mult_matrix(matrix, [plain_letter1, plain_letter2])
        cipher_letter1 = dec_letter(cipher_letters[0])
        cipher_letter2 = dec_letter(cipher_letters[1])
        cipher+=cipher_letter1
        cipher+=cipher_letter2
    return cipher.upper()
        
def mult_matrix(matrix2x2, matrix2x1, mod=26):
    row1 = matrix2x2[0][0]*matrix2x1[0]+matrix2x2[0][1]*matrix2x1[1]
    row2 = matrix2x2[1][0]*matrix2x1[0]+matrix2x2[1][1]*matrix2x1[1]
    row1 %= mod
    row2 %= mod
    return [row1, row2]

# Finds every nth letter in a text when given the keyword length (Viginere)
def get_every_nth(text, key_length):
    for i in range(key_length):
        print(get_frequency(text[i::key_length]))

# Finds repeated strings in a text (Viginere)
def find_repeats(text):
    repeats = []
    for length in range(2, 20):
        for j in range(len(text) - length + 1):
            test = text[j:j + length]
            if test in text[j + length + 1:]:
                diff = text[j + length + 1:].find(test) + 1 + length
                repeats.append((test, diff))
    return repeats


# Viginere input and decryption -> incomplete
# message_input = input("Enter message: ")
#
# message_input = message_input.replace(" ", "").strip()
# print(get_every_nth(message_input, 8))
# print(find_repeats(message_input))

def encrypt_with_viginere(message, key):
    key_length = len(key)
    int_key = [ord(i) for i in key]
    int_message = [ord(i) for i in message]
    cipher_text = ''

    for i in range(len(int_message)):
        value = (int_message[i] + int_key[i % key_length]) % 26
        cipher_text += chr(value + 65)

    return cipher_text
