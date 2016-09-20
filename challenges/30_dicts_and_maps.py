# https://www.hackerrank.com/challenges/30-dictionaries-and-maps
# works, for local tesgin do not forget to end input with Ctrl-D
import fileinput

def main():
    # read input
    nv = int(input().strip())
    pb = {}
    for _ in range(nv):
        raw = input().strip().split(' ')
        pb[raw[0]] = raw[1]
    
    exp = []
    for line in fileinput.input():
        exp.append( line.strip() )
    
    for e in exp:
        if e in pb:
            print("%s=%s" %(e, pb[e]))
        else:
            print("Not found")

main()