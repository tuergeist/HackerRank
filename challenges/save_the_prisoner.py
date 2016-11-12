# URL
# https://www.hackerrank.com/challenges/save-the-prisoner
import unittest

def main():
    data = readFromStdin()
    for test in data.values():
        print(calc_prisoner(test))

def readFromStdin():
    data = {}
    t = int(input().strip())
    for i in range(t):
        tmp = [int(c_temp) for c_temp in input().strip().split(' ')]
        data[i] = tmp
    return data

def calc_prisoner(data):
    prisoners = data[0]
    sweets = data[1]
    start = data[2]
    return ((sweets + start - 2) % prisoners) +1
    
if __name__ == "__main__":
#     unittest.main()
    main()
    
    
class Test(unittest.TestCase):
    def testABC(self):
        self.assertEqual(2, calc_prisoner([5,2,1]))
        self.assertEqual(122129406, calc_prisoner([352926151,380324688,94730870]))
        
    def test_from_file(self):
        infile = 'save_the_prisoner_in.txt'
        resultfile = 'save_the_prisoner_result.txt'
        
        ref = open(resultfile, 'r')
        with open(infile, 'r') as inf:
            t = int(inf.readline())
            for case in range(t):
                line = inf.readline()
                res = int(ref.readline().strip())
                test = [int(c_temp) for c_temp in line.strip().split(' ')]
                self.assertEqual(res, calc_prisoner(test), test) 
            