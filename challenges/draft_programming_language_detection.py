# https://www.hackerrank.com/challenges/programming-language-detection
import unittest

def main():
    n = int(input().strip())
    strings = []
    for _ in range(n):
        t = input().strip()
        strings.append(t)
    
    for s in strings:
        print(findHackerrank(s))
        
def findHackerrank(s):
    HR = 'hackerrank'
    rea = { True:   {True:0, False: 1}, 
           False:   {True:2, False: -1}}

    starts = ends = False

    if s == HR:
        starts = ends = True
    
    if s[:11] == HR + ' ':
        starts = True
    if s[-11:] == ' ' + HR:
        ends = True
    
    return rea[starts][ends]


if __name__ == '__main__':
    main()

class Test(unittest.TestCase):
    
    def setUp(self):
        ""
        
    def testStart(self):
        self.assertEquals(1, findHackerrank('hackerrank is great'))
        
    def testEnd(self):
        self.assertEquals(2, findHackerrank('i love hackerrank'))

    def testStartsEnds(self):
        self.assertEquals(0, findHackerrank('hackerrank is the greatest ever. I love hackerrank'))

    def testSingleWord(self):
        self.assertEquals(0, findHackerrank('hackerrank'))
    
    def testSingleWordNotHackerrank(self):
        self.assertEquals(-1, findHackerrank('hackerranki'))    
    
    def testSomewhere(self):
        self.assertEquals(-1, findHackerrank('I love hackerrank very much'))