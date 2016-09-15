import re

# https://www.hackerrank.com/challenges/saying-hi
def main():
    n = int(input().strip())
    strings = []
    for _ in range(n):
        t = input().strip()
        strings.append(t)
    
    for s in strings:
        if match(s): 
            print(s)
        
def match(s):
    return re.match('(hi\s[^d])',s,  re.IGNORECASE) is not None


if __name__ == '__main__':
    main()