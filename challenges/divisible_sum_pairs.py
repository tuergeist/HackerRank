# https://www.hackerrank.com/challenges/divisible-sum-pairs
# works

def main():
    _,k = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    pairs = calc(k, arr)
    print(len(pairs))

def calc(k, arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i]+arr[j]) % k == 0:
                pairs.append([i,j])
    return pairs

if __name__ == "__main__":
    main()