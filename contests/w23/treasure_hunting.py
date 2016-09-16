# https://www.hackerrank.com/contests/w23/challenges/treasure-hunting/
#
import unittest

def main():
    # read input
    x, y = [int(A_temp) for A_temp in input().strip().split(' ')]
    a, b = [int(A_temp) for A_temp in input().strip().split(' ')]
    k, n = calkKN(x,y,a,b)
    print(k)
    print(n)
    
def calkKN(x,y,a,b):
    M = [[a, b],[-b, a]] # (a, b) are transformed into (-b, a) 
    K = [[x, -b], [y, a]]
    N = [[a, x], [b, y]]
    k = det(K) / det(M)
    n = det(N) / det(M)
    return (k, n)


def det(matrix):
    d = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    return d

if __name__ == "__main__":
#     unittest.main()
    main()
    
    
class Test(unittest.TestCase):
    def testABC(self):
        self.assertEquals((4.0,-1.0), calkKN(5,3,1,1))
        
    