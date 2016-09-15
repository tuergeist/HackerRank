# https://www.hackerrank.com/challenges/30-review-loop
import unittest

def main():
    n = int(input().strip())
    strings = []
    for _ in range(n):
        t = input().strip()
        strings.append(t)
    
    for s in strings:
        even, odd = getEvenOddSubs(s)
        print("%s %s" % (even, odd))
        
def getEvenOddSubs(s):
    even = odd = ""
    l = 0
    for x in s:
        if l == 0:
            even += x
            l = 1
        else:
            odd += x
            l = 0
    return even, odd

if __name__ == '__main__':
    main()

class Test(unittest.TestCase):
    
    def setUp(self):
        ""
        
    def testSmall(self):
        self.assertEquals(('Hce','akr'), getEvenOddSubs('Hacker'))
        
    def testLong(self):
        s = 'b'
        for _ in range(9999):
            s += 'b'
        even, odd = getEvenOddSubs(s)
        self.maxDiff = None
        self.assertEqual(even, odd)
    