# https://www.hackerrank.com/challenges/matrix-rotation-algo
#
import unittest

def main():
    R, matrix = readFromStdin()
    
    m = MatrixSolver(matrix)
    m.rotate(R)
    print(m)
    
def readFromStdin():
    data = []
    tmp = [int(a_temp) for a_temp in input().strip().split(' ')] 
    m = tmp[0]
    r = tmp[2]
    for _ in range(m):
        data.append( [int(a_temp) for a_temp in input().strip().split(' ')] )
    return r, data

class MatrixSolver():
    def __init__(self, matrix):
        self.mat = matrix
        self.m = len(self.mat)
        self.n = len(self.mat[0])
        self.shortest = min(self.n, self.m)
        self.longest = max(self.n, self.m)
        self.shorthalf = int(self.shortest/2)
        self.mToChains()
        
    def mToChains(self):
        print(self)
        chains = {}
        if self.m == self.shortest: # y
            # waagerechte oben
            for y in range(self.shorthalf):
                chains[y] = []
                for x in range(y, self.n):
                    chains[self.getChain(x,y)].append(self.mat[y][x])
            # senkrechte rechts
            for x in range(self.n - self.shortest,self.n):
                for y in range(self.shorthalf, self.m):
                    print("senkr rechts ",x,y)
                    chains[self.getChain(x,y)].append(self.mat[y][x])
        print(chains)
        
    def rotate(self, r):
        return
    
    def getChain(self, x, y):
        print('testing ',x,y)
        if x == 0 or y == 0 or x == self.n-1 or y == self.m-1:
            return 0 
        for off in range(1, self.shortest): #optimize
            print(off, self.n-off-1,  self.m-off-1)
            if 0 < x and x <= self.n-off-1 and (y == off or y == self.m-off-1):
                print('ok')
                return off
        return -9
    
    def getChainlength(self, chain):
        shortest = self.shortest
        longest = self.longest
        l = 2 * (longest - 2*chain) + 2 * (shortest - 2 - 2*chain)
        return l
    
    def getElem(self, x, y):
        '''
        x = Nth column, y = Mth row
        '''
        print("[%s, %s] = %s in chain %s" % (x, y, self.mat[x][y], self.getChain(x, y)))
    
    def __str__(self):
        o = ""
        for l in self.mat:
            o += " ".join([str(e) for e in l])
            o += '\n'
        return o

if __name__ == "__main__":
#     unittest.main()
    main()
    
    
class Test(unittest.TestCase):
    def testABC(self):
        m = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        r = 1
        solver = MatrixSolver(m)
        solver.rotate(r)
        res = '''2 3 4 8
1 7 11 12
5 6 10 16
9 13 14 15'''

        self.assertEqual(12, solver.getChainlength(0))
        self.assertEqual( 4, solver.getChainlength(1))
        self.assertEqual(res, str(solver).strip())

