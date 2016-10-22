'''
Created on 22.10.2016

@author: cb
'''
import unittest
import re
def main():
    s = input().strip()
    n = int(input().strip())
    print(count_a(s, n))
    
def count_a(s, n):
    l = len(s)
    m =  n//l
    #print(l,m,n, n%l, s[:n%l])
    total = len(re.findall('a',s)) * m
    total += len(re.findall('a',s[:n%l]))
    return total


if __name__ == "__main__":
    main()
    


class Test(unittest.TestCase):
    def testABC(self):
        self.assertEqual(7, count_a('aba', 10))
        self.assertEqual(1000000000000, count_a('a',1000000000000))