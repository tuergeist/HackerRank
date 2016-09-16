import unittest
from math import ceil, floor
import re
import math


def main():
    s = input().strip()
    m = int(input().strip())
    
    print(solve(s, m))
    
    
def solve(s, m):
    ls = len(s)
    sub = findSmallesSub(s)
    r = int(floor(m / ls)) #  no rep
    if sub and r < m/sub:
        r = int(m/sub)
    return (r % int(math.pow(10,9) + 7))

def findSmallesSub(s):
    ls = len(s)
    res = 0
    maxd = int(ceil(ls/2))
    for i in range(1, maxd):
        if ls % i != 0:
            continue
        #print(i, end, s[:end])
        r = re.findall(s[:i], s)
        if len(r) > 1:
            # prove
            if s+r[0] == r[0]+s:
                # ok
                res = len(r[0])
                return res
        if len(r) == 1:
            break
    return res

 
    
class Test(unittest.TestCase):
    
    def testNonRepeating(self):
        self.assertEqual(2, solve('abc', 6))
        self.assertEqual(1, solve('abcde', 6))
        self.assertEqual(3, solve('abcde', 15))
        
    def testRepeating(self):
        self.assertEqual(3, solve('ababab', 6))    
        self.assertEqual(2, solve('aaab', 8))    
        
    def testRepeating2(self):
        self.assertEqual(4, solve('cdcdcd', 8))
        
    def testLong(self):
        s = 'Note that frexp and modfhave a different call/return pattern than theirfrexp and modfhave C equivalents: they take a single argument and return a pair of values, rather than returning their second return value through an output parameter there is no such thing in Python'
        s = s * 200
        s += 'a'
        print(len(s))
        print(solve(s, math.pow(10,9)))
        
    def testLong2(self):
        s = 'Notehatfrexp'
        s = s * 5000
        print(len(s))
        print(solve(s, math.pow(10,9)))
        
    def testLong3(self):
        s = 'abcdeabcdeefabcdeabcdeef'
        s = s * 5000
        print(len(s), math.pow(10,9)/len(s))
        print(solve(s, math.pow(10,9)))


if __name__ == "__main__":
    #unittest.main()
    main()        