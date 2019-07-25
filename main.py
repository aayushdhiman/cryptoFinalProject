
def sum (num1, num2, mod=26):
  return ((num1+num2) % mod)

def mult (num1, num2, mod=26):
  return ((num1*num2) % mod)

def power (num1, num2, mod=26):
  a = num2 % phi(mod)
  return (num1 ** a) % mod
def phi (num):
  list2 = prime_factors(num, list1)
  prod = product(list2)
  s = set(list2)
  for a in s
    prod = prod * ((1- (1/s)))
  return prod

def gcd(num1, num2):
  if (num1 == 0):
    return(num2)
  return(gcd(num2 % num1, num1))
 
def prime_factors(num1):
    i = 2
    factors = []
    while i * i <= num1:
        if num1 % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def product(list):
    p = 1
    for i in list:
        p *= i
    return p
def modinverse(e, mod=26):
  e = e % mod
  for i in range (1, mod):
    if (a * i) % m == 1):
      return i
  return 1  
  
