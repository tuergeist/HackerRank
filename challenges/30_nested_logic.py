# URL
#
import unittest

def main():
    # read input
    returned = [ int(a_temp) for a_temp in input().strip().split(' ') ] 
    expected = [ int(a_temp) for a_temp in input().strip().split(' ') ] 
    print(calc(returned, expected))

def calc(returned, expected):
    if returned[2] > expected[2]:
        return 10000
    if returned[2] == expected[2]:
        if returned[1] < expected[1]:
            return 0
        if returned[1] > expected[1]:
            return 500 * (returned[1] - expected[1])
        if returned[1] == expected[1]:
            if returned[0] <= expected[0]:
                # no fine
                return 0
            if returned[0] > expected[0]:
                return 15 * (returned[0] - expected[0])
    return 0

if __name__ == "__main__":
    main()
    
    
class Test(unittest.TestCase):
    def testABC(self):
        self.assertEqual(45, calc([9,6,2015], [6,6,2015]) )
        self.assertEqual(0, calc([2,6,2014], [5,7,2014]) )
        self.assertEqual(0, calc([31,12,2014], [1,1,2015]) )
