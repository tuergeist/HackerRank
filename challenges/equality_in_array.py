# URL
# https://www.hackerrank.com/challenges/equality-in-a-array
import unittest

def main():
    test = readFromStdin()
    print(equalize(test))

def readFromStdin():
    n = input()
    return [int(c_temp) for c_temp in input().strip().split(' ')]

def equalize(ais):
    t = {}
    for ai in ais:
        if ai not in t:
            t[ai] = 1
        else:
            t[ai] += 1
    if len(t.keys()) != 1:
        for item in sorted(t.items(), key=lambda x: x[1], reverse=True):
            return len(ais) - item[1]
    return 0
    
    
if __name__ == "__main__":
#     unittest.main()
    main()
    
    
class Test(unittest.TestCase):
    def testABC(self):
        self.assertEqual(2, equalize([3,3,2,1,3]))
