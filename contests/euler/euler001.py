'''
https://www.hackerrank.com/contests/projecteuler/challenges/euler001

Project Euler #1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below N.

1 <= T <= 10ˆ5 
1 <= N <= 10ˆ9 
'''

import unittest

def main():
    # read input
    data = Euler001.readFromStdin()
    e = Euler001()
    for n in data:
        print(e.solve(n))
        
class Euler001():
    @staticmethod
    def readFromStdin():
        data = []
        n = int(input())
        for _ in range(n):
            data.append( int(input().strip()) )
        return data
    
    def solve(self, N):
        s = 0
        for (f,d) in [(1,3), (1,5), (-1, 15)]:
            p = (N-1)//d
            s += f * ( (d * p * (p+1)) // 2 )
        return s


if __name__ == "__main__":
    main()
    
    
class Test(unittest.TestCase):
    def setUp(self):
        self.e = Euler001()
        
    def testZehnZwanzig(self):
        self.assertEqual(self.e.solve(10), 23) 
        self.assertEqual(self.e.solve(20), 78) # 3+6+9+12+15+18 + 5+10+15 - 15 [doppelt]

    def testTausend(self):
        self.assertEqual(self.e.solve(100), 2318)
        
        
    def testHTausend(self):
        self.assertEqual(self.e.solve(100000000), 2333333316666668)