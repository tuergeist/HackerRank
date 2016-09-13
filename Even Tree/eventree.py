# https://www.hackerrank.com/challenges/even-tree
# Graph Theory

# unfinished
import unittest

def main():
    # read input
    N, M, edges = readFromStdin()
    #N, M, edges = readFromFile('sample.input') 2,4, 11

    #print(edgesToGraph(edges))
    
    nodedict = getSubgraphs(edges)
    #printRoots(nodedict)
        
    while decompose(getRootNodes(nodedict)):
        '' 
        #print('decomposed')
    #printRoots(nodedict)
    print(len(getRootNodes(nodedict))-1)

def printRoots(nodedict):
    roots = getRootNodes(nodedict)
    print('Roots')
    for i in roots:
        print(i, i.getTotalAmountOfChildren())
    
    
class Node: 
    def __init__(self, name, pre=None): 
        self.name = name
        self.pre = pre 
        self.children = []   
        if pre is not None:
            self.pre.addChild(self)
        
    def addChild(self, node):
        #print('[%s] Adding child: %s' %(self.name, node))
        self.children.append(node)
    
    def removeChild(self, node):
        node.pre = None
        self.children.remove(node)
        
    def getChildren(self):
        return self.children
        
    def isRoot(self):
        return self.pre == None

    def getTotalAmountOfChildren(self):
        total = 0
        if self.children:
            total = len(self.children) 
            for c in self.children:
                total = total + c.getTotalAmountOfChildren()
        return total
    
    def __str__(self):
        snext = ""
        if self.children:
            snext = " => {%s}" % ", ".join([str(c) for c in self.children])
        return "(%s)%s" % (self.name,snext)     
    
def readFromFile(fname):
    N=0
    M=0
    edges = []
    with open(fname, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if N == 0:
            N, M = [int(tmp) for tmp in line.split(' ')]
        else:
            edges.append([int(tmp) for tmp in line.split(' ')]) 
    return N, M, edges

def readFromStdin():
    edges = []
    N, M = [int(tmp) for tmp in input().split(' ')]
    for _ in range(M):
        edges.append([int(tmp) for tmp in input().split(' ')])
    return N, M, edges

def edgesToGraph(edges):
    graph = {}
    n = 0
    for edge in edges:
        src = edge[1]
        dst = edge[0]
        if src in graph:
            graph[src].append(dst)
        else:
            graph[src] = [dst]
    return graph

def getSubgraphs(edges):
    '''
    Find lonely nodes or graphs
    '''
    nodedict = {}
    graph = edgesToGraph(edges)
    for node in graph:
        if node not in nodedict:
            nodedict[node] = Node(node)
        for child in graph[node]:
            if child not in nodedict:
                nodedict[child] = Node(child, nodedict[node])
    return nodedict
    

def edgesToNodes(edges):
    nodes = set()
    for edge in edges:
        nodes.add(edge[1])
        nodes.add(edge[0])
    return nodes    
    
def getRootNodes(nodedict):
    roots = []
    for nodeid in nodedict.keys():
        node = nodedict[nodeid]
        if node.isRoot():
            roots.append(node)
    return roots

def decompose(roots):
    removals = True
    anyRemovals = False
    while removals:
        removals = False
        for r in roots:
            #print('decomposing ', r)
            for c in r.getChildren():
                if c.getTotalAmountOfChildren() == 1:
                    # decompose between r and c
                    r.removeChild(c)
                    removals = True
                if c.getTotalAmountOfChildren() == 3:
                    # try to decompose subtree otherwise decompose r, c
                    # decompose if r - c - sc - ssc, ssc
                    if len(c.getChildren()) == 1:
                        r.removeChild(c)
                        removals = True
                    else:
                        removals = decompose([c])
                        
                if c.getTotalAmountOfChildren() > 3:
                    removals = decompose([c])
                if removals:
                    anyRemovals = True
                    
    return anyRemovals    
                
if __name__ == "__main__":
    main() 
    


class Test(unittest.TestCase):
    def testSample1(self):
        # 2,4,11
        self.assertEqual(2, self.doRun('sample.input'))
    
    def testSample2(self):
        self.assertEqual(4, self.doRun('sample2.input'))

    def testSample3(self):
        self.assertEqual(11, self.doRun('sample3.input'))
                
    def doRun(self, fname):
        N, M, edges = readFromFile(fname)
        nodedict = getSubgraphs(edges)
        while decompose(getRootNodes(nodedict)):
            '' 
        return len(getRootNodes(nodedict))-1
