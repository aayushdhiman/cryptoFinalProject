from collections import Counter
#Frequencey Analsys
def get_frequency(text):
    return Counter(text)
 
def fa_test_if_english(text):
    text = text.lower().replace(" ",'')
    text = ''.join(filter(str.isalpha, text))  
      
    length = len(text)
    bi = length//2
    tri = length//3
    
    frequencies = {'a':8.167, 'b':1.492, 'c':2.782, 'd':4.253, 'e':12.702,'f':2.228,
                   'g':2.015, 'h':6.094, 'i':6.966, "j":0.153, 'k':.772, 'l':4.025,
                   'm':2.406, 'n':6.749, 'o':7.507, 'p':1.929, 'q':.095, 'r':5.987,
                   's':6.327, 't':9.056, 'u':2.758, 'v':0.978, 'w':2.360, 'x':.150,
                   'y':1.974, 'z':.074}
    
    bigrams = {'th':2.71, 'he':2.33, 'in':2.03, 'er':1.78, 'an':1.61, 're':1.41,
                'es':1.32, 'on':1.32, 'st':1.25, 'nt':1.17}
    
    trigrams = {'the':1.81, 'and':.73, 'ing':.72, 'ent':.42, 'ion':.42, 'her':.36,
                'for':.34, 'tha':.33, 'nth':.33, 'int':.32}
    score=0
    for letter in frequencies.keys():
        counts = text.count(letter)
        score+=abs(frequencies[letter]-(counts/length*100))
    for letter in bigrams.keys():
        counts = text.count(letter)
        score+=abs(bigrams[letter]-(counts/bi*100))
    for letter in trigrams.keys():
        counts = text.count(letter)
        score+=abs(trigrams[letter]-(counts/tri*100))
    return score

# Encrypts letter A = 1
def enc_letter(letter):
    return ord(letter.lower()) - 96

# Decrypts letter A = 1
def dec_letter(letter):
    if letter == 0:
        letter = 26
    return chr(letter + 96)

def add(num1, num2, mod=26):
    return (num1 + num2) % mod


def multiply(num1, num2, mod=26):
    return (num1 * num2) % mod

# Additive Encryption
def encrypt_with_additive(plain_text, n, block_size):
    cipher_text = ''
    for index in range(len(plain_text)):
        letter = enc_letter(plain_text[index].lower())
        cipher_text += dec_letter(add(letter, n)).upper()
        if index != 0 and (index - 1) % block_size == 0:
            cipher_text += " "
    return cipher_text

# Multiplicative Encryption
def encrypt_with_multiplicative(plain_text, n, block_size):
    cipher_text = ''
    for index in range(len(plain_text)):
        letter = enc_letter(plain_text[index].lower())
        cipher_text += dec_letter(multiply(letter, n)).upper()
        if index != 0 and (index - 1) % block_size == 0:
            cipher_text += " "
    return cipher_text


# Affine Encryption
def encrypt_with_affine(plain_text, n, r, block_size):
    plain_text = encrypt_with_additive(plain_text, n, block_size)
    plain_text = encrypt_with_multiplicative(plain_text.replace(" ", ''), r, block_size)
    return plain_text
# Additive Decryption
def decrypt_additive(cipher):
    cipher = cipher.lower().replace(" ",'')
    best_score = 10000
    best_string = ''
    for i in range(26):
        plain = encrypt_with_additive(cipher, i, len(cipher)+1).lower().replace(" ",'')
        score = fa_test_if_english(plain)
        if score<best_score:
            best_score=score
            best_string=plain
    return best_string
  

# Multiplicative Decryption
def decrypt_multiplicative(cipher):
    cipher = cipher.lower().replace(" ",'')
    best_score = 10000
    best_string = ''
    for i in range(26):
        plain = encrypt_with_multiplicative(cipher, i, len(cipher)+1).lower().replace(" ",'')
        score = fa_test_if_english(plain)
        if score<best_score:
            best_score=score
            best_string=plain
    return best_string

def decrypt_affine(cipher):
    cipher = cipher.lower().replace(" ",'')
    best_score = 10000
    best_string = ''
    for i in range(26):
        for j in range(26):
            plain = encrypt_with_multiplicative(cipher, i, len(cipher)+1).lower().replace(" ",'')
            plain = encrypt_with_additive(plain, j, len(cipher)+1).lower().replace(" ",'')
            score = fa_test_if_english(plain)
            if score<best_score:
                best_score=score
                best_string=plain
    return best_string
