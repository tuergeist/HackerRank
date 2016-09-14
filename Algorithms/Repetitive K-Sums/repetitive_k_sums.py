'''
Created on 09.09.2016

@author: cb
'''
import os
from sys import argv

def calc_gen_seq(N, K, GSEQ):
    '''
    N is len of GSEQ
    K is sum-tuple size
    GSEQ is possible generator sequence
    '''
    
    
def calc_seq(N, K, SUMS):
    print("N=%d K=%d SUMS=%s" %(N,K,SUMS))
    r = []
    for s in reversed(sorted(SUMS)):
        if len(r) != 0:
            for x in r:
                if s % x == 0:
                    continue
                rest = s - K
                
                
        r.append(int(s/K))
    return r

def calc(arg):
    '''
    Takes the number of test cases in the first line and then two consecutive lines as test case
    '''
    lines = arg.split(os.linesep)
    testcases = int(lines[0])
    if len(lines) < 3 or len(lines) % 2 == 0:
        raise Error('Illegeal number of lines')
    tmp = lines[1].split(' ')
    N = tmp[0]
    K = tmp[1]
    SUMS = list(int(x) for x in lines[2].split(' '))
    print(calc_seq(N, K, SUMS))
    return(arg)

if __name__ == '__main__':
    calc(argv)