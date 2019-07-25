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
