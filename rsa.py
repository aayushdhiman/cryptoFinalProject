def block(text):
      blockedText = ' '.join([cipherText[i:i+3] for i in range(0,len(cipherText), 3)])
      while(len(blockedText) % 6 != 0):
          blockedText = blockedText + 'a'
      return blockedText
      
def enc_with_zeroes(letter):
    output = str(ord(letter)-96)
    if len(output) == 1:
        output = '0'+output
    return output
    
def getAllNumbersOfCipherText(text):
    lst = []
    i = 0;    
    while(i < len(text)):
        lst.append(enc_with_zeroes(text[i]))        
        i = i + 1            
    return lst
    
def concentatelist(list):
    newlst = []
    for i in range(0, int(len(list) / 4)):
        a = ''
        for j in range (0,4):
          print((i*4)+j)
          if (j != 6):
            a += str(list[(i*4)+j])            
        newlst.append(int(a))
    #    print(a)
    return newlst    
    
def power (num1, e, mod, phi):
    a = e % phi
    return (num1 ** a) % mod 
    
cipherText = input("Cyphertext: ")
p = int(input("First Prime: "))
q = int(input("Second Prime: "))
n = p*q
e = int(input("Encryption Key: "))
phi = (p-1)* (q-1)

a = block(cipherText)
b = getAllNumbersOfCipherText(a)
c = concentatelist(b)
d = []
for i in range (0, len(c)):
   d.append(power(c[i], e, n, phi))  
#print(a)
#print(b)
#print(c)
print(d)


#def block(s, size):
#o = []
#while s:
#o.append(s[:2])
#s = s[2:]
#return o
#enc_letter()
#def encode_text()
#blocked = block(a, 6)
#for i in range (0, )
#p = input("")
#q = input("")
#n = p*q
#phi = (p-1)(q-1)
