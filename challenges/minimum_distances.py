# URL
#
import unittest

def main():
    # read input
    _ = int(input().strip())
    arr = [int(A_temp) for A_temp in input().strip().split(' ')]
    print(calcMinDistance(arr))
    
def calcMinDistance(data):
    '''
    Print a single integer denoting the minimum dij in A; if no such value exists, print -1.
    '''
    result = len(data) + 1
    found = {}
    pos = 0
    for n in data:
        if n in found:
            diff = pos - found[n]
            if diff < result:
                result = diff 
        found[n] = pos
        pos +=1 
    if result == len(data) + 1:
        result = -1
    return result
        

if __name__ == "__main__":
#     unittest.main()
    main()
    
    
class Test(unittest.TestCase):
    def testABC(self):
        self.assertEquals(3, calcMinDistance([7,1,3,4,1,7]))
        
    def testNoResult(self):
        self.assertEquals(-1, calcMinDistance([7,1,3,4,2,8]))