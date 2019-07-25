def findRepeats(text):
    repeats = []
    for length in range(5,100):
        for start in range(0,len(text)-length+1):
            word = text[start:start+length]
            if word in text[start+length::]:
                repeats.append((word, text[start+length::].find(word)+length))
    print(repeats)
