# URL
# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers
# https://docs.python.org/3/reference/datamodel.html#object.__mul__
# http://www.tf.uni-kiel.de/matwis/amat/mw1_ge/kap_2/basics/b2_1_5.html
# max 45min
import unittest
import math

def main():
    c, d = readFromStdin()
    print(c+d)
    print(c-d)
    print(c*d)
    print(c/d)
    print(c.mod())
    print(d.mod())
    

def readFromStdin():
    xin = [float(c_temp) for c_temp in input().strip().split(' ')]
    c = Complex(xin[0], xin[1])
    xin = [float(c_temp) for c_temp in input().strip().split(' ')]
    d = Complex(xin[0], xin[1])
    return c, d

class Complex():
    def __init__(self, r, i):
        self.real = r
        self.img = i
        
    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img) 

    def __sub__(self, other):
        return Complex(self.real - other.real, self.img - other.img) 

    def __mul__(self, other):
        real = self.real*other.real - self.img*other.img
        img = self.real*other.img + other.real*self.img 
        return Complex(real, img)

    def __truediv__(self, other):
        real = (self.real*other.real + self.img*other.img) / \
                (other.real*other.real + other.img*other.img)
        
        img = (other.real*self.img - self.real*other.img) / \
                (other.real*other.real + other.img*other.img)  
        return Complex(real, img)
    
    def mod(self): # aka Betrag
        return Complex(math.sqrt(math.pow(self.real, 2) + math.pow(self.img, 2)), 0)
    
    def __eq__(self, other):
        return prec2(self.img) == prec2(other.img) and \
            prec2(self.real) == prec2(other.real)
    
    def __str__(self):
        sign=''
        if self.img >= 0:
            sign = '+'
        return "%.2f%s%.2fi" % (self.real, sign, self.img)
        
   
def prec2(x):
    return int(x * 100) / 100
    
if __name__ == "__main__":
    main()
    
    
class Test(unittest.TestCase):
    def testAdd(self):
        c = Complex(1,2)
        d = Complex(3,4)
        self.assertEquals(Complex(4,6), c+d)
        self.assertEquals(Complex(4,-6), c + Complex(3,-8))

    def testSub(self):
        self.assertEquals(Complex(2,1), Complex(3,3) - Complex(1,2))
        
    def testMul(self):
        self.assertEquals(Complex(4,17), Complex(2,1) * Complex(5,6))
        
    def testDiv(self):
        res = Complex(2,1) / Complex(5,6)
        self.assertEquals(Complex(0.26, -0.11), res, res)
        
    def testMod(self):
        self.assertEquals(Complex(7.81, 0), Complex(5,6).mod())    
        
    def testStr(self):
        self.assertEqual('7.81+0.00i', str(Complex(7.81, 0)))
        self.assertEqual('7.81-1.00i', str(Complex(7.81, -1)))    