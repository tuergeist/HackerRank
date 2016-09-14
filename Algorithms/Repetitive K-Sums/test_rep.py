'''
Created on 09.09.2016

@author: cb
'''
import unittest
from repetitive_k_sums import calc, calc_seq


class Test(unittest.TestCase):
    def testCalcSeq(self):
        N=1
        K=3
        SUMS=[3]
        self.assertEqual(calc_seq(N, K, SUMS), [1])
    
    def testCalc2ndSeq(self):
        self.assertEqual(calc_seq(2, 2, [12,34,56]), [6,28])
    
    def xtestSimpleExample(self):
        inp = '1\n1 3\n3'
        out = '3'
        self.assertEqual(calc(inp), out)

    def xtestSampleInput(self):
        inp = '''3
1 3
3
2 2
12 34 56
3 2
2 3 4 4 5 6'''
        out = '''1
6 28
1 2 3'''
        self.assertEqual(calc(inp), out)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['Test.testCalc2ndSeq', 'Test.testCalcSeq']
    unittest.main()