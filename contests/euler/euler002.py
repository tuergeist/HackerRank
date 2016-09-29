'''

'''
import unittest

def main():
    # read input
    e = Euler002()
    e.readFromStdin()
    e.printOut()
        
class Euler002():
    def __init__(self):
        self.data = []
        self.efib = [2]
        f = 1
        s = 2
        mx = 40000000000000000
        while  s < mx:
            fib = f + s
            if fib % 2 == 0: 
                self.efib.append(fib)
            f = s
            s = fib

    
    def printOut(self):
        for n in self.data:
            print(self.solve(n))
    
    def readFromStdin(self):
        n = int(input())
        for _ in range(n):
            self.data.append( int(input().strip()) )
    
    def solve(self, N):
        s = 0
        for f in self.efib:
            if f <= N:
                s += f
        return s


if __name__ == "__main__":
    main()
    
    
class Test(unittest.TestCase):
    def setUp(self):
        self.e = Euler002()
        
    def testZehnZwanzig(self):
        self.assertEqual(self.e.solve(10), 10) 

    def testTausend(self):
        self.assertEqual(self.e.solve(100), 44)
        
