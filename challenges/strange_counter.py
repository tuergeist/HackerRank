'''
Created on 22.10.2016

@author: cb
'''
from math import floor, pow, log



def main():
    t = int(input().strip())
    print(int((pow(2,floor(log((t+2)/3, 2)))*3)*2-t-2))

if __name__ == "__main__":
    main()
    

