import sys
input = sys.stdin.readline

def solution(cnt, offset):
    if cnt == k:
        return 0
    if out_of_board(offset // m, offset % m):
        return MIN_VALUE

    ret = MIN_VALUE

    if can_go(offset // m, offset % m):
        visit[offset // m][offset % m] = True
        ret = max(ret, solution(cnt + 1, offset + 1) + board[offset // m][offset % m])
        visit[offset // m][offset % m] = False
    ret = max(ret, solution(cnt, offset + 1))

    return ret

def can_go(r, c):
    if out_of_board(r, c):
        return False
    if not out_of_board(r - 1, c) and visit[r - 1][c]:
        return False
    if not out_of_board(r + 1, c) and visit[r + 1][c]:
        return False
    if not out_of_board(r, c - 1) and visit[r][c - 1]:
        return False
    if not out_of_board(r, c + 1) and visit[r][c + 1]:
        return False
    return True

def out_of_board(r, c):
    if r < 0 or r >= n or c < 0 or c >= m:
        return True
    return False

if __name__ == '__main__':
    global n, m, k, board, visit, MIN_VALUE
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    visit = [[False] * m for _ in range(n)]
    MIN_VALUE = -10001 * n * m
    print(solution(0, 0))
