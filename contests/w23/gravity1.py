import unittest
import math

def main():
    # read input
    nv = int(input().strip())
    tree_raw = [ int(t) for t in input().strip().split(' ')]
    nexperiments = int(input().strip())
    exp = []
    for _ in range(nexperiments):
        exp.append( [ int(t) for t in input().strip().split(' ')] )
    
    nodes = createNodes(tree_raw)
    
def createNodes(tree_raw):
    nodes = {}
    i=2
    nodes[1] = Node(1)
    for n in tree_raw:
        nodes[i] = Node(i, nodes[n])      
        i+=1
        
    return nodes
        
class Graph(object):
    def __init__(self, nodes):
        self.nodes = nodes
        
    def getDistanceBetween(self, a, b):
        na = self.nodes[a]
        nb = self.nodes[b]
        
        if na == nb:
            return 0
        # are a and b direct connected
        if na.hasChild(nb) or na.hasParent(nb):
            return 1

        cd = na.getChildrenDict()
        for dist, children in cd.items():
            if nb in children:
                return dist
        if not nb.isRoot() and nb.pre.hasChild(na):
            return 2
        
        return 9999
        
    def getForce(self, target, activated):
        # list of activated nodes
        cdrn = self.nodes[activated].getAllChildren()
        cdrn.add(self.nodes[activated]) # add activated node as well
        # calc distance from activated nodes to the target node
        force = 0
        for c in cdrn:
            d = self.getDistanceBetween(target, c.name)
            force += math.pow(d,2)
        return force
       
class Node(object): 
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
        
    def hasChild(self, nodeb):
        return nodeb in self.children
    
    def hasParent(self, nodeb):
        return self.pre == nodeb
        
    def getChildren(self):
        return self.children
        
    def getParent(self):
        return self.pre
        
    def isRoot(self):
        return self.pre == None
    
    def getAllChildren(self, dist=1):
        cs = set(self.children)
        cd = set(self.children)
        for c in cs:
            cd.update( c.getAllChildren())
        return cd
        
    def getChildrenDict(self, distance = 1):
        d = {}
        if self.children:
            d[distance] = self.children
            for c in self.children:
                d = merge_two_dicts(c.getChildrenDict(distance + 1), d)
        return d
    
    def getDistance(self):
        total = 0

        return total

    
    
    def getForcesFor(self, n):
        True
    
    def __str__(self):
        snext = ""
        x = ""
        if self.pre is None:
            x = "Root: "
        if self.children:
            snext = " => {%s}" % ", ".join([str(c) for c in self.children])
        return "%s(%s)%s" % (x, self.name, snext)     
           
def merge_two_dicts(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z

if __name__ == '__main__':
    main()
    
class Test(unittest.TestCase):

    def testFirst(self):
        nodes = createNodes([1,2,2,4])
        g = Graph(nodes)
        g.getDistanceBetween(1,2)
        self.assertEqual(7, g.getForce(2, 1))
        self.assertEqual(13, g.getForce(1, 4))
        
        #incomplete
    def testComplex(self):
        nodes = createNodes([1,2,2,4,5,6,7,])
        g = Graph(nodes)
        g.getDistanceBetween(1,2)
        self.assertEqual(7, g.getForce(2, 1))
        self.assertEqual(13, g.getForce(1, 4))
        