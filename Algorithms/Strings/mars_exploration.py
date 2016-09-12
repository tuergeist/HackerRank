# https://www.hackerrank.com/challenges/mars-exploration
# 
import unittest

def main():
    ins = input().strip()
    print(calc(ins))

def calc(ins):
    count = 0
    assert len(ins) % 3 == 0
    for i in range(0, len(ins) - 2, 3):
        sub = ins[i:i+3]
        if sub != 'SOS':
            if sub[0] != 'S':
                count = count + 1
            if sub[1] != 'O':
                count = count + 1
            if sub[2] != 'S':
                count = count + 1            
    return count

           
if __name__ == "__main__":
    #unittest.main()
    main()

class Test(unittest.TestCase):
    def testSimple(self):
        self.assertEquals(1, calc('SPS'))
    def testSimple2(self):        
        self.assertEquals(1, calc('SPSSOS'))
    def testZero(self):        
        self.assertEquals(1, calc('S0SSOS'))
    def testMultibit(self):        
        self.assertEquals(3, calc('SOSTTT'))     