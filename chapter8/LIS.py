import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution(idx):
    if idx == n:
        return 0
    if dp[idx + 1] != 0:
        return dp[idx + 1]
    ret = 1
    for i in range(idx + 1, n):
        if idx == -1 or arr[i] > arr[idx]:
            ret = max(ret, 1 + solution(i))
    dp[idx + 1] = ret
    return dp[idx + 1]

if __name__ == '__main__':
    global dp, arr, n
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        dp = [0] * (n + 1)
        arr = list(map(int, input().split()))
        print(solution(-1) - 1)