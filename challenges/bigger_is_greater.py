# URL https://www.hackerrank.com/challenges/bigger-is-greater
#
import math
import unittest

def main():
    words  = readFromStdin()

def readFromStdin():
    data = []
    n = int(input())
    for _ in range(n):
        data.append( input().strip() )
    return data

def findBiggerLexiSolution(word):
    # find longest non-increasing suffix
    p = 0
    for c in word[::-1]:
        if lc == '':
            lc = c
            continue
        if ord(c) >= ord(lc):
           p += 1
    
            
    
def calcLexi(word):
    ls = 0
    f = 1
    for s in word[::-1]:
        ls += ord(s) * f
        f *= 10
    return ls
        

if __name__ == "__main__":
    main()
    
    
class Test(unittest.TestCase):
    def testCL(self):
        self.assertEqual(97, calcLexi('a'))
        self.assertEqual(970+97, calcLexi('aa'))
        self.assertEqual(9700+970+97, calcLexi('aaa'))
        
    def testCL2(self):
        self.assertEqual(970+98, calcLexi('ab'))
        self.assertEqual(980+97, calcLexi('ba'))
        
    def testBigger(self):
        self.assertEqual('ba', findBiggerLexiSolution('ab'))
        
    def testComplex(self):
        self.assertEqual('dhkc', findBiggerLexiSolution('dhck'))
        
    def testComplex2(self):
        self.assertEqual('hcdk', findBiggerLexiSolution('dkhc'))

        
        