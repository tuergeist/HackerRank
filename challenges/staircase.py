# https://www.hackerrank.com/challenges/staircase
# works

def main():
    n = int(input().strip())
    printStaircase(n)

def printStaircase(n):
    for m in range(n,0,-1):
        print((m-1)*' '+(n-m+1)*"#")

if __name__ == "__main__":
    #unittest.main()
    main()