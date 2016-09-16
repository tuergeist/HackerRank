
def main():
    n = int(input().strip())
    gears = []
    for _ in range(n):
        t = int(input().strip())
        gears.append(t)
    
    for s in gears:
        if s % 2 == 0:
            print('Yes')
        else:
            print('No')
        

if __name__ == '__main__':
    main()
