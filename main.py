
class Add:
def __init__ (self, num1, num2):
  self.num1 = num1
  self.num2 = num2
  return ((self.num1+self.num2) % 26)

class Mult:
def __init__ (self, num1, num2):
  self.num1 = num1
  self.num2 = num2
  return ((self.num1*self.num2) % 26)
