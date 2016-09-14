'''
Created on 11.09.2016

@author: cb
'''
import unittest
from maxsubarray import maxContSum, maxDiscSum


class Test(unittest.TestCase):


    def testMaxContSum(self):
        self.assertEqual(maxContSum([1,2,3,4]), 10)
    
    def testMaxContSumWNegs(self):
        self.assertEqual(maxContSum([1,2,3,4, -5]), 10)
        self.assertEqual(maxContSum([2,-1,2,3,4, -5]), 10)
        self.assertEqual(maxContSum([-1,0,-1, -10]), 0)
        self.assertEqual(maxContSum([0]),0)
    
    def testMmaxDiscSum(self):
        self.assertEqual(maxDiscSum([1,2,3,4, -5]), 10)
        self.assertEqual(maxDiscSum([2,-1,2,3,4, -5]), 11)
        self.assertEqual(maxDiscSum([-100, -1 , 1 ,0]), 1)
        self.assertEqual(maxDiscSum([-100, -1 , 0 ,-1]), 0)

    def testNegOnly(self):
        self.assertEqual(maxDiscSum([-100, -1]), -1)
        self.assertEqual(maxContSum([-100, -1]), -1)
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()