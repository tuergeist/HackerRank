import os

'''
the way I solved it (lighthouse problem) was basically, standing on each element and checking on each direction if there was a free cell, then I would add +1 to the initial radius and ask again, if at any point I'd hit an obstacle or the end of the map, then I'd have the answer. I'd do this for every element and the one that gave me the biggest radius in all directions was the answer.
To debug I printed how things looked for each cell:
5
**.**
*...*
*...*
**..*
*...*
1
so I'd go for every cell and this was my debug output:
[x][x][0][x][x]
[x][0][1][0][x]
[x][0][1][0][x]
[x][x][0][0][x]
[x][0][0][0][x]
'''

def main():
    
    # read input
    fname = 'lighthouse.sample9.input'
    debug = False
    if os.path.isfile(fname):
        n, matrix = readFromFile(fname)
    else:
        n = int(input().strip())
        matrix = []
        for _ in range(n):
            t = list(input().strip())
            matrix.append(t)
    
    print(matrix)
    m = Matrix(matrix, n)
    m.process()

def readFromFile(fname):
    matrix = []
    lnr = True
    n = 0
    with open(fname, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if lnr == True:
            n = int(line.strip())
            lnr = False
            continue
        t = list(line.strip())
        matrix.append(t)
    return n, matrix

class Matrix(object):
    def __init__(self, matrix, n):
        self.matrix = matrix
        self.n = n
        self.free = []
   
    
    def process(self):
        for y in range(self.n):
            # find free places
            for x in range(self.n):
                if self.matrix[x][y] == ".":
                    self.free.append((x,y))
    
        print(self.free)
        # calc free places
        
#         for y in range(self.n):
            # find free places
#             for x in range(self.n):
                #self.hasFreeNeighbors((x,y))
        self.maxRad((4, 4))
                
    def hasFreeNeighbors(self, pos):
        x, y = pos
        n = 0
        m = int(self.n / 2)# radius
        # top left
        for rx in range(-m,m+1):
            for ry in range(-m,m+1):
                if (x+rx, y+ry) in self.free:
                    n += 1
        if n >= 29: print(pos, n)


    def maxRad(self, pos):
        # (r - 0,5*sqrt(2))/sqrt(2) = no of cubes
        px, py = pos
        n = {}
        m = int(self.n / 2) # radius
        
#         rad1 = { (-1,-1),(-1,0),(-1,1),
#                  (1,-1), (1,0), (1,1),
#                  (0,-1), (0,1)}
#         rad2 = { (-2, -2..2),
#                  ( 2, -2..2),
#                  ( -1..1, 2),
#                  ( -1..1, -2)}
        n[1] = True
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if (x,y) == (0, 0):
                    continue
                if (x+px, y+py) not in self.free:
                    n[1] = False
                
        n[2] = True
        for x in [-2, 0, 2]:
            for y in [-2,-1, 0, 1, 2]:
                if (x,y) == (0, 0):
                    continue
                if (x+px, y+py) not in self.free:
                    n[2] = False
                
        for x in [-1, 0, 1]:
            for y in [-2, 2]:
                if (x,y) == (0, 0):
                    continue
                if (x+px, y+py) not in self.free:
                    n[2] = False
        
        print(pos, n)

if __name__ == '__main__':
    main()
    
    # 3 = 7 x 7 
    # 2 = 5 x 5
    # 1 = 3 x 3
    # 0 = 1
    