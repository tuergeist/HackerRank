
def main():
    
    arr = []
    for _ in range(6):
        arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        arr.append(arr_t)
       
    print(maxHourglassSum(arr))
    
    
def maxHourglassSum(arr):
    maxi = -6*6*9
    for x in range(4):
        for y in range(4):
            r = calcHGat(arr, x, y)
            if r > maxi:
                maxi = r
    return maxi


def calcHGat(arr, x, y):
    s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
    return s
    
    
main()