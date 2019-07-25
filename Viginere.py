from collections import Counter

# Blocks Text
def block(text):
      blockedText = ' '.join([cipherText[i:i+6] for i in range(0,len(cipherText), 6)])
      return blockedText
    
cipherText = input("")
a = block(cipherText)
print(a)
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


# Viginere Encrypter and Decrypter

def encrypt_with_viginere(message, key):
    key_length = len(key)
    int_key = [ord(i) for i in key]
    int_message = [ord(i) for i in message]
    cipher_text = ''

    for i in range(len(int_message)):
        value = (int_message[i] + int_key[i % key_length]) % 26
        cipher_text += chr(value + 65)

    return cipher_text
