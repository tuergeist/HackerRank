def number_needed(a, b):
    adict = analyze(a)
    bdict = analyze(b)
    r = 0
    for k in diffKeys(adict, bdict):
        if k in adict:
            r += adict[k]
        else:
            r += bdict[k]
    for k in commonKeys(adict, bdict):
        r += abs(adict[k] - bdict[k])
    return r
    
def analyze(a):
    m = {}
    for c in a:
        try:
            m[c] +=1
        except:
            m[c] = 1
    return m

def diffKeys(x, y):
    xs = set(x.keys())
    ys = set(y.keys())
    return xs.symmetric_difference(ys)

def commonKeys(x, y):
    xs = set(x.keys())
    ys = set(y.keys())
    return xs.intersection(ys)

if __name__ == '__main__':
    a = input().strip()
    b = input().strip()

    print(number_needed(a, b))