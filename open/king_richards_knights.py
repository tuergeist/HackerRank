import unittest

def main():
    k = Knights()
    k.readFromStdin()
    k.setup()
    k.performCmds()
    k.getPositions()
    
def log(*kwargs):
    print(kwargs)
    
    
class Knights():
    def __init__(self):
        N = 0
        self.m = []
        
    def readFromStdin(self):
        self.N = int(input().strip())
        self.S = int(input().strip())
        self.cmds = []
        for _ in range(self.S):
            self.cmds.append( [int(a_temp) for a_temp in input().strip().split(' ')] )
        self.L = int(input().strip())
        self.knts = []
        for _ in range(self.L):
            self.knts.append(  input().strip() )
        
    def _isAffected(self, r, c, cmd=0):
        a, b, d = self.cmds[cmd]
        ax, bx = a+d, b+d
        return (a<=r<=ax and b<=c<=bx)
        
    def setup(self):
        # calc position for each knight requested
        for k in self.knts:
            c = k % self.N
            r = int((k-c) / self.N)
            affected = self._isAffected(r, c)
            log(k, r, c, affected)
            if not affected:
                return [r,c]
            
            # r,c = x,y
            # apply 1 cmd
            #    x,y          a b d
            # 9: 1,2 -> 1,5 | 1,2,4
            # move x = x+d-1, y = y - b + y
            # 25:3,4 -> 2,3 | 
            #      x = x
            
        #print(self.m)
    
    def performCmds(self):
        return True
    
    def getPositions(self):
        return []
    
if __name__ == "__main__":
    main()
    
    
class Test(unittest.TestCase):
    def testABC(self):
        k = Knights()
        k.N = 7
        k.S = 4
        k.cmds = [[1,2,4],[2,3,3],[3,4,1],[3,4,0]]
        k.L = 7
        k.knts = [7,0,6,9,11,24,25,48]
        
        k.setup()
        k.performCmds()
        self.assertEqual([[1,1],[1,7],[4,6],[3,4],[2,5],[2,4],[7,7]], k.getPositions())