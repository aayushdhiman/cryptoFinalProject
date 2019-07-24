from collections import Counter 

def calcIC(text):
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


# message_input = input("Enter message: ")
message_input = "JNFEP DNBLZ BCDLL RYVNN MZCNA GLIGN EYNAR NMZRW HRRAA EENGG ANYAA CHUEG MISOM RGZZA AMTVF AFETP " \
                "DYAGA SJRZY BXZEE ESQTH AHRQI AGKFA ARANL LMOEM SFSXY TYNSK OZNVH YEQRQ RCKLA ZCCCP XKWVC VJHBW " \
                "PRMQE ETTWV UZOEI YESNB GEWAO GQSTU XZTFJ HGHXL NQXTG HXTEN UHUEX SECQO ATLDO ACDNY XLER"

# message_input = "DDESOEOSDDHOQQHKMDHXJBBSQDTRYNBMHOPHGJEUHOQQOTDDGWHOQQWDNZYIJGHXWBBIEFAUOFVMWOKYANKCWBDDOFESCCDDGEGZYQXY"

message_input = message_input.replace(" ", "").strip()
print(get_every_nth(message_input, 8))
print(find_repeats(message_input))
