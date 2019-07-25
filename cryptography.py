from collections import Counter

cipherText_dic = {"Affine": 1, "Multiplicative": 2, "Additive": 3, "Hill": 4, "Vigenere": 5,
                  "Rivest-Shamir-Alderman": 6}

# Reference functions:

# Blocks Text
def block(text):
      blockedText = ' '.join([cipherText[i:i+6] for i in range(0,len(cipherText), 6)])
      return blockedText
    
cipherText = input("")
a = block(cipherText)
print(a)

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
 
# Hill Encryption
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

#Viginere decryption
  def decrypt(cipher_text, key):
    keylength = len(key)
    # print(keylength)
    key_int = [ord(i) for i in key]
    # print(key_int)
    cipher_text_int = [ord(i) for i in cipher_text]
    # print(cipher_text_int)
    plain_text = ''
    for i in range(len(cipher_text_int)):
        value = ((cipher_text_int[i] - key_int[i % keylength]) - 20) % 26
        plain_text += chr(value + 65)
    return plain_text


def find_repeats(text):
    repeats = []
    for length in range(5, 100):
        for start in range(0, len(text) - length + 1):
            word = text[start:start + length]
            if word in text[start + length::]:
                repeats.append((word, text[start + length::].find(word) + length))
    return repeats


def file_format():
    file = open("no_swears_medium.txt", "r")
    words_medium = file.readlines()

    for i in range(len(words_medium)):
        words_medium[i] = words_medium[i][:-1]

    return words_medium

def brute_force(keylength, words, message_ciphertext):
    plain_texts = []
    for i in range(len(words)):
        if len(words[i]) == keylength:
            plain_texts.append(decrypt(message_ciphertext, words[i]))
            # print(plain_texts)

    top_ic = []
    top_keywords = []
    index = 0
    best_ic = 0
    while len(top_ic) < 20:
        min_score = abs(calc_ic(plain_texts[0]) - .067)
        best_keyword = plain_texts[0]
        for j in range(len(plain_texts)):
            if abs(calc_ic(plain_texts[j]) - .067) < min_score:
                min_score = abs(calc_ic(plain_texts[j]) - .067)
                best_keyword = plain_texts[j]
                index = j
                best_ic = min_score
        top_ic.append(best_ic)
        top_keywords.append(best_keyword)
        plain_texts.remove(plain_texts[index])
    lists = [top_ic, top_keywords]
    return lists


def pretty_print(ic_s, plaintexts):
    for i in range(len(ic_s)):
        # for j in range(len(ls[0])):
        print("IC: " + str(ic_s[i])[:10] + "\t" + " Decoded Possibility: " + plaintexts[i])


# message_input = input("Viginere ciphertext: ")
message = message_input.replace(" ", "").strip()
repeated_strings = find_repeats(message)
key_length = len(repeated_strings[0][0])
check_words = file_format()
lists = brute_force(key_length, check_words, message)
pretty_print(lists[0], lists[1])

  
  
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
  
  
# Hill Decryption
 def decrypt_hill(cipher):
    possible_dets = [1,3,5,7,9,11,15,17,19,21,23,25]
    best_score = 10000
    best_string = ''
    best_matrix = []
    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    matrix = [[a,b],[c,d]]
                    if get_det(matrix) in possible_dets:
                        plain = encrypt_with_hill(cipher, matrix)
                        score = fa_test_if_english(plain)
                        if score<best_score:
                            best_score=score
                            best_string=plain
                            best_matrix = matrix
    a=best_matrix[0][0]
    b=best_matrix[0][1]
    c=best_matrix[1][0]
    d=best_matrix[1][1]
    results = []
    for num1 in [a,b,c,d]:
        for num2 in [x for x in [a,b,c,d] if x!=num1]:
            for num3 in [x for x in [a,b,c,d] if x!=num1 and x!=num2]:
                for num4 in [x for x in [a,b,c,d] if x!=num1 and x!=num2 and x!=num3]:
                    matrix1 = [[num1,num2],[num3,num4]]
                    results.append(encrypt_with_hill(cipher, matrix1))
    return results

def get_det(arr):
    return ((arr[0][0]*arr[1][1])-(arr[0][1]*arr[1][0]))%26
