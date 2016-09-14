# URL
#
import os
import unittest

def main():
    # read input
    fname = 'sample9.input'
    debug = False
    if os.path.isfile(fname):
        N, M, edges = readFromFile(fname)
        debug = True
    else:
        N, M, edges = readFromStdin()

def readFromFile(fname):
    data = []
    lnr = -1
    with open(fname, 'r') as f:
        lines = f.readlines()
    for line in lines:
        lnr = lnr + 1
        if lnr == 0 or lnr %2 == 1:
            continue
        b = [int(a_temp) for a_temp in line.split(' ')]
        data.append( b )
    return data

def readFromStdin():
    data = []
    n = int(input())
    for _ in range(n):
        input()
        data.append( [int(a_temp) for a_temp in input().strip().split(' ')] )
    return data

if __name__ == "__main__":
#     unittest.main()
    main()
    
    
class Test(unittest.TestCase):
    def testABC(self):
        self.assertTrue(True)