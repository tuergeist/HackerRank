# https://www.hackerrank.com/challenges/even-tree
# Graph Theory

# unfinished

def main():
    # read input
#     N, M, edges = readFromStdin()
    N, M, edges = readFromFile('sample.input')

    print(N,M, edges)
    graph = edgesToGraph(edges)
    nodes = edgesToNodes(edges)
    print(graph)
    print(len(nodes), nodes)
    
    

def readFromFile(fname):
    N=0
    M=0
    edges = []
    with open(fname, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if N == 0:
            N, M = [int(tmp) for tmp in line.split(' ')]
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
    for edge in edges:
        if edge[1] in graph:
            graph[edge[1]].append(edge[0])
        else:
            graph[edge[1]] = [edge[0]]
    return graph

def edgesToNodes(edges):
    nodes = set()
    for edge in edges:
        nodes.add(edge[1])
        nodes.add(edge[0])
    return nodes    
    

if __name__ == "__main__":
    main() 