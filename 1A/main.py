from math import ceil 
print(ceil((nbs:=list(map(int,input().split())))[0]/nbs[-1]) * ceil(nbs[1]/nbs[-1]))