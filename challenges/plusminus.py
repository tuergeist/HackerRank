# https://www.hackerrank.com/challenges/plus-minus
# works
import unittest

def main():
    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    r = calc(n, arr)
    for v in r:
        print(v)

def calc(n, arr):
    r = []
    pos = [ x for x in arr if x>0 ]
    neg = [ x for x in arr if x<0 ]
    zer = [ x for x in arr if x==0 ]
    for x in [pos,neg,zer]:
        r.append(float(len(x))/n)
    return r

class Test(unittest.TestCase):
    def testName(self):
        r = calc(6, [-4, 3, -9, 0, 4, 1])
        e = [0.5, 0.3333333333, 0.16666666666]
        for n in range(3):
            self.assertAlmostEqual(r[n], e[n])


if __name__ == "__main__":
    #unittest.main()
    main()