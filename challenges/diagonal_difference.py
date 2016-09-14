#!/bin/python3


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
    
d1 = 0
d2 = 0
for x in range(n):
    d1 = d1 + a[x][x]
    d2 = d2 + a[x][n-1-x]
print(abs(d1-d2))

