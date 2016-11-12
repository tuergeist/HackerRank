# URL
# https://www.hackerrank.com/challenges/bon-appetit
import unittest

def main():
    item, costs, charged = readFromStdin()
    r = calc_diff(item, costs, charged)
    if r == 0:
        print("Bon Appetit")
    else:
        print(r)

def readFromStdin():
    data = [int(c_temp) for c_temp in input().strip().split(' ')]
    costs = [int(c_temp) for c_temp in input().strip().split(' ')]
    charged = int(input().strip())
    return data[1], costs, charged

def calc_diff(item, costs, charged):
    total_shared = sum(costs) - costs[item]
    diff = charged - (total_shared /2)
    return int(diff)
    
if __name__ == "__main__":
#     unittest.main()
    main()
    
    
class Test(unittest.TestCase):
    def testABC(self):
        self.assertEqual(5, calc_diff(1, [3,10,2,9],12))
        self.assertEqual(0, calc_diff(1, [3,10,2,9],7))