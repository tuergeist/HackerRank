
def main():
    # read input
    nv = int(input().strip())
    tree_raw = [ int(t) for t in input().strip().split(' ')]
    nexperiments = int(input().strip())
    exp = []
    for _ in range(nexperiments):
        exp.append( [ int(t) for t in input().strip().split(' ')] )
    
    
        