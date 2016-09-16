# https://www.hackerrank.com/challenges/even-tree
# Graph Theory

# done
import unittest
import os.path

def printChildren(children, g, pre="  "):
    #print(children)
    for n in children:
        print(pre, n)
        if n in g:
            printChildren(g[n],g, pre + "  ")
            
def main():
    # read input
    fname = 'sample9.input'
    debug = False
    if os.path.isfile(fname):
        N, M, edges = readFromFile(fname)
        debug = True
    else:
        N, M, edges = readFromStdin()

    if debug: 
        g = edgesToGraph(edges)
        #printChildren([1], g, "")
        
                
    nodedict = getSubgraphs(edges)
    if debug: printRoots(nodedict)
    while decompose(getRootNodes(nodedict)):
        '' 
        #print('decomposed')
    if debug: printRoots(nodedict)
    print(len(getRootNodes(nodedict))-1)

def printRoots(nodedict):
    roots = getRootNodes(nodedict)
    print('Roots')
    for i in roots:
        print(i, i.getTotalAmountOfChildren()+1)
    
    
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
        node.pre = self
    
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
        x = ""
        if self.pre is None:
            x = "Root: "
        if self.children:
            snext = " => {%s}" % ", ".join([str(c) for c in self.children])
        return "%s(%s)%s" % (x, self.name, snext)     
    
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
    assert M == len(edges)
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
            else:
                nodedict[node].addChild(nodedict[child])
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
                ctotal = c.getTotalAmountOfChildren()
                if ctotal == 0:
                    continue
                if ctotal == 1:
                    # decompose between r and c
                    r.removeChild(c)
                    removals = True
                if ctotal == 2:
                    if len(c.getChildren()) == 1:
                        c.removeChild(c.getChildren()[0])
                        removals = True
                if ctotal == 3:
                    # try to decompose subtree otherwise decompose r, c
                    removals = decompose([c])
                    if len(c.getChildren()) >= 1 and removals == False:
                        r.removeChild(c)
                        removals = True
                        
                if ctotal > 3:
                    removals = decompose([c])
                    
                    if removals == False and (ctotal - len(c.getChildren())) >= 0:
                        if ctotal % 2 == 1:
                            # even num of children
                            # detach from r
                            r.removeChild(c)
                            removals = True
                        
                    
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

    def testSample8(self):
        self.assertEqual(23, self.doRun('sample8.input'))

    def testSample9(self):
        self.assertEqual(31, self.doRun('sample9.input'))
                                
    def doRun(self, fname):
        N, M, edges = readFromFile(fname)
        nodedict = getSubgraphs(edges)
        while decompose(getRootNodes(nodedict)):
            '' 
        return len(getRootNodes(nodedict))-1
