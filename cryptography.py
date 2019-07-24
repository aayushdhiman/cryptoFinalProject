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
