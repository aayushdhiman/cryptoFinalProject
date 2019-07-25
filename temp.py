def findRepeats(text):
    repeats = []
    for length in range(5, 100):
        for start in range(0, len(text) - length + 1):
            word = text[start:start + length]
            if word in text[start + length::]:
                repeats.append((word, text[start + length::].find(word) + length))
    return repeats


message_input = "KQOWE FVJPU JUUNU KGLME KJINM WUXFQ MKJBG WRLFN FGHUD WUUMB SVLPS NCMUE KQCTE SWREE KOYSS IWCTU \
                AXYOT APXPL WPNTC GOJBG FQHTD WXIZA YGFFN SXCSE YNCTS SPNTU JNYTG GWZGR WUUNE JUUQE APYME KQHUI DUXFP \
                GUYTS MTFFS HNUOC ZGMRU WEYTR GKMEE DCTVR ECFBD JQCUS WVBPN LGOYL SKMTE FVJJT WWMFM WPNME MTMHR SPXFS \
                SKFFS TNUOC ZGMDO EOYEE KCPJR GPMUR SKHFR SEIUE VGOYC WXIZA YGOSA ANYDO EOYJL WUNHA MEBFE LXYVL WNOJN \
                SIOFR WUCCE SWKVI DGMUC GOCRU WGNMA AFFVN SIUDE KQHCE UCPFC MPVSU DGAVE MNYMA MVLFM AOYFN TQCUA FVFJN \
                XKLNE IWCWO DCCUL WRIFT WGMUS WOVMA TNYBU HTCOC WFYTN MGYTQ MKBBN LGFBT WOJFT WGNTE JKNEE DCLDH WTVBU \
                VGFBI JGYYI DGMVR DGMPL SWGJL AGOEE KJOFE KNYNO LRIVR WVUHE IWUUR WGMUT JCDBN KGMBI DGMEE YGUOT DGGQE \
                UJYOT VGGBR UJYS"
repeated_strings = findRepeats(message_input.replace(" ", "").strip())
key_length = len(repeated_strings[0])


def attempt_decode(message, key_length):
    messages = []
    # for 

def enc_with_zeroes(letter):
    output = str(ord(letter)-96)
    if len(output) == 1:
        output = '0'+output
    return output








https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears-medium.txt
    
    
def file_format():
    file = open("no_swears_medium.txt", "r")
    words_medium = file.readlines()

    for i in range(len(words_medium)):
        words_medium[i] = words_medium[i][:-1]

    return words_medium

def block_text(text, length):
    output = ' '.join(text[i:i+length] for i in range(0,len(text),length))
    return output
