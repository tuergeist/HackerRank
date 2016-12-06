# URL
# https://www.hackerrank.com/challenges/mini-max-sum
import unittest

def main():
    test = readFromStdin()
    print(minimax(test))

def readFromStdin():
    return [int(c_temp) for c_temp in input().strip().split(' ')]

def minimax(ais):
    ais.sort()
    return "%s %s" % (ais[0]+ais[1]+ais[2]+ais[3], ais[4]+ais[1]+ais[2]+ais[3])
    
    
if __name__ == "__main__":
#     unittest.main()
    main()
    
    
class Test(unittest.TestCase):
    def testABC(self):
        self.assertEqual('10 14', minimax([1,2,3,4,5]))
