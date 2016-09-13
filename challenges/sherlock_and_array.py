
'''NO
NO
YES
YES
YES
YES
NO
YES
NO
NO'''

def main():
    # t tests
    # n elems
    #t, case = readFromFile('sherlock_and_array_sample3.input.txt')
    t, case = readFromStdin()
    for n in range(t):
        #print("processing ", n)
        if findIndex(case[n]): print("YES")
        else: print("NO")


def readFromStdin():
    case = {}
    t = int(input().strip())
    for n in range(t):
        nelem = int(input().strip())
        case[n] = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        assert len(case[n]) == nelem
    return t, case
    
    
def readFromFile(fname):
    t=0
    num = 0
    n=0
    case = {}
    with open(fname, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if t == 0:
            t = int(line.strip())
            continue
        if num == 0:
            num = int(line.strip())
            continue
        
        case[n] = [int(tmp) for tmp in line.split(' ')]
        assert num == len(case[n])
        n+=1
        num = 0
    return t, case
        
def findIndex(elems):
    nelem = len(elems)
    if nelem == 1:
        return True
    lv = 0
    divisor = nelem
    stepper = nelem
    end = nelem
    if nelem >= 500:
        divisor = 100
        stepper = int(nelem/divisor)
        for e in range(0, nelem, stepper):
            lsum = sum(elems[:e-1])
            rsum = sum(elems[e:])
            d = lsum - rsum
            if d > 0:
                end = e
                break
    #print(end)
    diff = -1
    for e in range(end - stepper, end):
        lsum = sum(elems[:e-1])
        rsum = sum(elems[e:])
        diff = lsum-rsum
        if diff == 0:
            #print(e)
            return True
        sign = diff / abs(diff)
        if lv != 0 and lv != sign:
            #print("Vorzeichenwechsel, stop", e)
            return False
        lv = sign
    
    return False
        
main()