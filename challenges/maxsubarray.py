sample_in = '''2 
4 
1 2 3 4
6
2 -1 2 3 4 -5
'''
def main():
    data = readFromStdIn()
    #data = readFromFile('maxsubarray.data')
    for ds in data:
        print("%s %s" % (maxContSum(ds), maxDiscSum(ds)))
    
def readFromFile(fname):
    data = []
    lnr = -1
    with open(fname, 'r') as f:
        lines = f.readlines()
    for line in lines:
        lnr = lnr + 1
        if lnr == 0 or lnr %2 == 1:
            continue
        b = [int(a_temp) for a_temp in line.split(' ')]
        data.append( b )
    return data

def readFromStdIn():
    data = []
    n = int(input())
    for _ in range(n):
        input()
        data.append( [int(a_temp) for a_temp in input().strip().split(' ')] )
    return data

    
def maxContSum(ain):
    ain2 = sorted(ain)
    if ain2[-1] < 0:
        return ain2[-1]
    
    max_ending_here = max_so_far = 0
    for x in ain:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def maxDiscSum(ain):
    maxv = 0
    ain = sorted(ain)
    if ain[-1] <= 0: 
        return ain[-1]
    
    end = len(ain)
    for i in range(end):
        v = ain[i]
        if v > 0: 
            maxv = maxv + v 
    return maxv 

if __name__ == "__main__":
    main()