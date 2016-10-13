# URL https://www.hackerrank.com/challenges/bigger-is-greater
# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
import unittest

def main():
    words  = readFromStdin()
    for w in words:
        print(findBiggerLexiSolution(w))

def readFromStdin():
    data = []
    n = int(input())
    for _ in range(n):
        data.append( input().strip() )
    return data

def findBiggerLexiSolution(word):
    # find longest non-increasing suffix
    pos = findLongestNonIncr(word)
    piv = findPivotSucc(word, pos)
    if piv is None:
        return 'no answer'
    word = swap(pos-1, piv, word)
    word = reverse(pos, word)
    return word 

def reverse(pos, word):
    return word[:pos] + word[:pos-1:-1]
    
def swap(p1, p2, word):
    word = list(word)
    tmp = word[p1]
    word[p1] = word[p2]
    word[p2] = tmp
    return "".join(word)

def findLongestNonIncr(word):
    last_v = 0
    pos = len(word)
    for s in word[::-1]:
        if last_v > ord(s):
            return pos
        last_v = ord(s)
        pos -= 1
    return 0

def findPivotSucc(word, pos):
    if pos == 0:
        return None
    pivot = word[pos-1]
    pos = len(word) -1
    for s in word[::-1]:
        if ord(pivot) < ord(s):
            return pos
        pos -= 1
    return None
# just a test    
def calcLexi(word):
    ls = 0
    f = 1
    for s in word[::-1]:
        ls += ord(s) * f
        f *= 10
    return ls
        

if __name__ == "__main__":
    main()
    
    
class Test(unittest.TestCase):
    def testCL(self):
        self.assertEqual(97, calcLexi('a'))
        self.assertEqual(970+97, calcLexi('aa'))
        self.assertEqual(9700+970+97, calcLexi('aaa'))
        
    def testCL2(self):
        self.assertEqual(970+98, calcLexi('ab'))
        self.assertEqual(980+97, calcLexi('ba'))
        
    def testBigger(self):
        self.assertEqual('ba', findBiggerLexiSolution('ab'))
        
    def testComplex(self):
        self.assertEqual('dhkc', findBiggerLexiSolution('dhck'))
        
    def testComplex2(self):
        self.assertEqual('hcdk', findBiggerLexiSolution('dkhc'))

    def testFindLNI(self):
        self.assertEqual(3, findLongestNonIncr('0125330'))
        self.assertEqual(5, findPivotSucc('0125330', 3))
        self.assertEqual('0130235', findBiggerLexiSolution('0125330'))
        
    def testNoAnswer(self):
        self.assertEqual('no answer', findBiggerLexiSolution('bb'))