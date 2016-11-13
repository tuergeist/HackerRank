# URL
# https://www.hackerrank.com/challenges/fibonacci-modified
import unittest

def main():
    test = readFromStdin()
    print(calc_fib(test[0], test[1], test[2]))

def readFromStdin():
    return [int(c_temp) for c_temp in input().strip().split(' ')]

def calc_fib(t1, t2, n):
    t = {}
    t[1] = t1
    t[2] = t2
    for i in range(3, n+1):
        t[i] =  t[i-2] + (t[i-1]*t[i-1])
    return t[n]
    
if __name__ == "__main__":
#     unittest.main()
    main()
    
    
class Test(unittest.TestCase):
    def testABC(self):
        self.assertEqual(5, calc_fib(0,1,5))
