
def sum (num1, num2, mod=26):
  return ((num1+num2) % mod)

def mult (num1, num2, mod=26):
  return ((num1*num2) % mod)

def power (num1, num2, mod=26):

def phi (num):
  list2 = factor(num, list1)
  result = (list2[0]-1) * (list2[1]-1)
  return result

def gcd(num1, num2):
  if (num1 == 0):
    return(num2)
  return(gcd(num2 % num1, num1))
 
def factor(num1, list1):
 for i in range (2, int(num1 ** 0.5))
   if(gcd(i,num1) !== 1):
      list1.append(i)
      factor((num1 / i), list1)    
 return list1
