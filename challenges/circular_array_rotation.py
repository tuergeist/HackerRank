import collections

def main():
    # n elems
    # k shifts
    # q queries
    queries = []
    n, k, q = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    elems = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    for _ in range(q):
        queries.append(int(input().strip()))
    
    d = collections.deque(elems)
    d.rotate(k)
    for q in queries:
        print(d[q])    
    
main()