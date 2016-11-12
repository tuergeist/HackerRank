# URL
# https://www.hackerrank.com/challenges/sock-merchant
import unittest

def main():
    data = readFromStdin()
    print(sock_pairs(data))

def readFromStdin():
    _ = int(input().strip())
    data = [int(c_temp) for c_temp in input().strip().split(' ')]
    return data

def sock_pairs(data):
    sdic = {}
    pair = 0
    for sock in data:
        if sock in sdic:
            if sdic[sock] == 1:
                sdic[sock] = 0
                pair +=1
            else:
                sdic[sock] = 1
        else:
            sdic[sock] = 1
    return pair

if __name__ == "__main__":
#     unittest.main()
    main()
    
    
class Test(unittest.TestCase):
    def testABC(self):
        self.assertEqual(3, sock_pairs([10,20, 20, 10, 10, 30, 50, 10, 20]))