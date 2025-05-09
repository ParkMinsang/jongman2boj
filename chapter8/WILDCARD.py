import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def solution(pattern_idx, s_idx):
    if pattern_idx == len(pattern) and s_idx == len(s):
        return 1
    if pattern_idx >= len(pattern) or s_idx > len(s):
        return 0
    if dp[pattern_idx][s_idx] != -1:
        return dp[pattern_idx][s_idx]
    ret = 0
    if is_match(pattern[pattern_idx], s[s_idx] if s_idx < len(s) else ''):
        if pattern[pattern_idx] == '*':
            for i in range(s_idx, len(s) + 1):
                ret = max(ret, solution(pattern_idx, i + 1), solution(pattern_idx + 1, i))
        else:
            ret = solution(pattern_idx + 1, s_idx + 1)
    dp[pattern_idx][s_idx] = ret
    return ret


def is_match(pattern_char, s_char):
    if pattern_char == '?' or pattern_char == '*':
        return True
    if pattern_char == s_char:
        return True
    return False

if __name__ == '__main__':
    global pattern, s, dp
    tc = int(input())
    for _ in range(tc):
        pattern = input().rstrip()
        n = int(input())
        ans = []
        for _ in range(n):
            s = input().rstrip()
            dp = [[-1] * (len(s) + 1) for _ in range(len(pattern))]
            if solution(0, 0) > 0:
                ans.append(s)
        ans.sort()
        print('\n'.join(ans))