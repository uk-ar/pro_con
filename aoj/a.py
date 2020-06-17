#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys

def conv(l):
    #l.reverse()
    ret = 0
    for e in l:
        ret = ret*60+e
    return ret

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        exit()
    a = tuple(tuple(sys.stdin.readline().split()) for _ in range(N)) # multi line with single param
    a = [[conv(list(map(int,s.split(":")))), conv(list(map(int,e.split(":"))))] for s,e in a]

    N = 24*60*60
    imos = [0]*(N+1)

    for s,e in a:
        imos[s] += 1
        if e < N+1 : imos[e] -= 1

    cur = 0
    ret = 0
    for i in range(N):
        cur = cur + imos[i]
        ret = max(ret,cur)
    print(ret)
