import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

MAX_SCORE = 100_0000

def solution(idx):
    if idx == len(arr):
        return 0
    if dp[idx] != -1:
        return dp[idx]
    ret = MAX_SCORE
    for i in range(3, 6):
        if idx + i <= len(arr):
            score_value = MAX_SCORE
            if i == 3:
                score_value = score3(arr[idx], arr[idx + 1], arr[idx + 2])
            elif i == 4:
                score_value = score4(arr[idx], arr[idx + 1], arr[idx + 2], arr[idx + 3])
            elif i == 5:
                score_value = score5(arr[idx], arr[idx + 1], arr[idx + 2], arr[idx + 3], arr[idx + 4])
            ret = min(ret, solution(idx + i) + score_value)
    dp[idx] = ret
    return ret

def score3(a, b, c):
    if a == b == c:
        return 1
    if a - b == b - c == 1 or a - b == b - c == -1:
        return 2
    if a == c != b:
        return 4
    if a - b == b - c:
        return 5
    return 10

def score4(a, b, c, d):
    if a == b == c == d:
        return 1
    if a - b == b - c == c - d == 1 or a - b == b - c == c - d == -1:
        return 2
    if a == c and b == d:
        return 4
    if a - b == b - c == c - d:
        return 5
    return 10

def score5(a, b, c, d, e):
    if a == b == c == d == e:
        return 1
    if a - b == b - c == c - d == d - e == 1 or a - b == b - c == c - d == d - e == -1:
        return 2
    if a == c == e and b == d:
        return 4
    if a - b == b - c == c - d == d - e:
        return 5
    return 10

if __name__ == '__main__':
    global arr, dp
    c = int(input())
    for _ in range(c):
        num_str = input().rstrip()
        arr = [int(digit) for digit in num_str]
        dp = [-1] * len(arr)
        print(solution(0))