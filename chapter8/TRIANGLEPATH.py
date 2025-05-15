import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution(r, c):
    if r == n - 1:
        return triangle[r][c]
    if dp[r][c] != -1:
        return dp[r][c]
    dp[r][c] = max(solution(r + 1, c), solution(r + 1, c + 1)) + triangle[r][c]
    return dp[r][c]

if __name__ == '__main__':
    global triangle, n, dp
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        triangle = [list(map(int, input().split())) for _ in range(n)]
        dp = [[-1] * i for i in range(1, n + 1)]
        print(solution(0, 0))
