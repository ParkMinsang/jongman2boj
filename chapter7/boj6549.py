import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution(lt, rt, h):
    if lt == rt:
        return h[lt]
    mt = (lt + rt) // 2
    ret = max(solution(lt, mt, h), solution(mt + 1, rt, h))
    lo = mt
    hi = mt + 1
    height = min(h[lo], h[hi])
    ret = max(ret, height * 2)
    while lt < lo or hi < rt:
        if hi < rt and (lo == lt or h[lo - 1] < h[hi + 1]):
            hi += 1
            height = min(height, h[hi])
        else:
            lo -= 1
            height = min(height, h[lo])
        ret = max(ret, height * (hi - lo + 1))
    return ret

if __name__ == "__main__":
    while True:
        h = list(map(int, input().split()))
        if h[0] == 0:
            sys.exit()
        print(solution(1, len(h) - 1, h))