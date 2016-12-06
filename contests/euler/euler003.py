'''
https://www.hackerrank.com/contests/projecteuler/challenges/euler003

Project Euler #3: Largest Prime Factor

'''

import unittest
from math import floor, sqrt

def main():
    # read input
    data = readFromStdin()

    for n in data:
        print(int(solve(n)))
        
def readFromStdin():
        data = []
        n = int(input())
        for _ in range(n):
            data.append( int(input().strip()) )
        return data
    
def solve(N):
    i = N
    if N % 2 ==0 :
        while i > 1: 
            i /= 2
            if i == 1:
                return i
    return loop(N)
        
def loop(N):
    end = floor(sqrt(N))
    for i in range(2, end+1):
        if N % i == 0:
            return loop(N/i)
    return N

if __name__ == "__main__":
    main()
    
    
class Test(unittest.TestCase):
        
    def testSmall(self):
        self.assertEqual(5, solve(10))
        self.assertEqual(3, solve(9))
        self.assertEqual(3, solve(18))  
        self.assertEqual(17,solve(17))
        self.assertEqual(29,solve(13195))

