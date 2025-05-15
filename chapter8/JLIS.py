import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def solution(idx1, idx2):
    if idx1 == n and idx2 == m:
        return 0
    if dp[idx1 + 1][idx2 + 1] != -1:
        return dp[idx1 + 1][idx2 + 1]
    ret = 2
    ca = a[idx1] if idx1 != -1 else -sys.maxsize
    cb = b[idx2] if idx2 != -1 else -sys.maxsize
    cm = max(ca, cb)
    for i in range(idx1 + 1, n):
        if a[i] > cm:
            ret = max(ret, 1 + solution(i, idx2))
    for i in range(idx2 + 1, m):
        if b[i] > cm:
            ret = max(ret, 1 + solution(idx1, i))
    dp[idx1 + 1][idx2 + 1] = ret
    return dp[idx1 + 1][idx2 + 1]

if __name__ == '__main__':
    global a, b, dp, n, m
    tc = int(input())
    for _ in range(tc):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        print(solution(-1, -1) - 2)