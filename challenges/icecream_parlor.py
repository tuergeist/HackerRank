# URL
# https://www.hackerrank.com/challenges/icecream-parlor
import unittest

def main():
    test = readFromStdin()
    for case in test.values():
        print(ices(case))

def readFromStdin():
    numcases = int(input())
    case = {}
    for i in range(numcases):
        case[i] = { 'money': int(input().strip()),
                    'flavors':  int(input().strip()),
                    'ice': [int(c_temp) for c_temp in input().strip().split(' ')] }
    return case

def ices(ais):
    l = len(ais['ice'])
    ice = ais['ice']
    for x in range(l-1):
        for y in range(x+1, l):
            if ice[x] + ice[y] == ais['money']:
                return '%s %s' %(x+1, y+1)
    
    
if __name__ == "__main__":
#     unittest.main()
    main()
    
    
class Test(unittest.TestCase):
    def testABC(self):
        self.assertEqual('1 4', ices({'money':4, 'ice':[1,4,5,3,2]}))