# URL
#


def main():
    # read input
    emails = readFromStdin()
    l = []
    for e in emails:
        r = printNameIfOK(e[0], e[1])
        if r is not None:
            l.append(r)
    for e in sorted(l):
        print(e)
        
def readFromStdin():
    data = []
    n = int(input())
    for _ in range(n):
        data.append( input().strip().split(' ') )
    return data

def printNameIfOK(name, email):
    if '@gmail.com' in email:
        return name
    return None

if __name__ == "__main__":
#     unittest.main()
    main()
    
