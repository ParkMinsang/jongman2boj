import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def solution(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return 0
    if dp[r][c] != -1:
        return dp[r][c]
    if r == n - 1 and c == n - 1:
        return 1
    if board[r][c] == 0:
        return 0
    dp[r][c] = solution(r + board[r][c], c) + solution(r, c + board[r][c])
    return dp[r][c]

if __name__ == "__main__":
    global dp, board
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-1] * n for _ in range(n)]
    print(solution(0, 0))