from collections import Counter 

cipherText_dic = {"Affine":1,"Multiplicative":2,"Additive":3,"Hill":4,"Vigenere":5,"Rivest-Shamir-Alderman":6}

def calc_ic(text):
    counts = Counter(text)
    num = 0.0
    den = 0.0
    for val in counts.values():
        i = val
        num += i * (i - 1)
        den += i
    if (den == 0.0):
        return 0.0
    else:
        return num / ( den * (den - 1))
    
def enc_letter(letter):
    return ord(letter.lower())-96

def dec_letter(letter):
    if letter==0:
        letter=26
    return chr(letter+96)

def get_every_nth(text, key_length):

    for i in range(key_length):
        print(get_frequency(text[i::key_length]))


def get_frequency(text):
    return Counter(text)


def find_repeats(text):
    repeats = []
    for length in range(2, 20):
        for j in range(len(text)-length+1):
            test = text[j:j+length]
            if test in text[j+length+1:]:
                diff = text[j+length+1:].find(test)+1+length
                repeats.append((test, diff))
    return repeats

def determine_IC_type(ic):
    
    

message_input = input("Enter message: ")
# message_input = "JNFEP DNBLZ BCDLL RYVNN MZCNA GLIGN EYNAR NMZRW HRRAA EENGG ANYAA CHUEG MISOM RGZZA AMTVF AFETP " \
                "DYAGA SJRZY BXZEE ESQTH AHRQI AGKFA ARANL LMOEM SFSXY TYNSK OZNVH YEQRQ RCKLA ZCCCP XKWVC VJHBW " \
                "PRMQE ETTWV UZOEI YESNB GEWAO GQSTU XZTFJ HGHXL NQXTG HXTEN UHUEX SECQO ATLDO ACDNY XLER"

# message_input = "DDESOEOSDDHOQQHKMDHXJBBSQDTRYNBMHOPHGJEUHOQQOTDDGWHOQQWDNZYIJGHXWBBIEFAUOFVMWOKYANKCWBDDOFESCCDDGEGZYQXY"

message_input = message_input.replace(" ", "").strip()
print(get_every_nth(message_input, 8))
print(find_repeats(message_input))

def cipherText(cipherText):
    Switcher = {
        1: "Affine"
        2: "Multiplicative"
        3: "Additive"
        4: "Vigenere"
        5: "Hill"
        6: "Rivest-Shamir-Alderman"
    }
    #test if this is affine
    if():
        elif():
            elif():
                elif():
                    elif():
                        elif():
def sum (num1, num2, mod=26):
  return ((num1+num2) % mod)

def mult (num1, num2, mod=26):
  return ((num1*num2) % mod)
