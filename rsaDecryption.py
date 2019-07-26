import math

#User Inputs
inputCipherText = input("Enter Cipher Text: ")
N = input("Enter Modded Key: ")
e = input("Enter Encryption Key: ")

#Mathematical Calculation
def gcd(a, b): 
  
    if (a == 0): 
        return b 
    return gcd(b % a, a) 


def phi(n): 
  
    result = 1
    for i in range(2, n): 
        if (gcd(i, n) == 1): 
            result+=1
    return result 


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def raisePower(cipherTextList, decryptingKey):
  outputList = []
  for cipherTextNumber in cipherTextList:
    test = cipherTextNumber**decryptingKey
    outputList.append(test)
  return outputList


def modularArithmetic(decryptedCipherTextList, modularNumber):
  finalOutputList = []
  for finalCipherTextNumber in decryptedCipherTextList:
    workingValue = finalCipherTextNumber % modularNumber
    finalOutputList.append(workingValue)
  return finalOutputList

  
def parseCipherInputTextToInteger(inputCipherTextAsString):
  parsedOutputList = []
  splittedCipherText = inputCipherTextAsString.split(",")
  for specificCipherText in splittedCipherText:
    parsedOutputList.append(int(specificCipherText))
  return parsedOutputList

#Temporary Variables


#New Variables
parsedCipherInputText = parseCipherInputTextToInteger(inputCipherText)
print(parsedCipherInputText)
phiOfN = phi(int(N))
d = modinv(phiOfN, int(e))
convertedText = raisePower(parsedCipherInputText, d)
decryptedText = modularArithmetic(convertedText, phiOfN)

#Print Decrypted Text
print(decryptedText, phiOfN, d, convertedText)

#print(inputCipherText, N, e)
