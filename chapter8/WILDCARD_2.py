import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def solution(pattern_idx, s_idx):
    if pattern_idx == len(pattern):
        return 1 if (s_idx == len(s)) else 0
    if dp[pattern_idx][s_idx] != -1:
        return dp[pattern_idx][s_idx]
    if pattern_idx < len(pattern) and s_idx < len(s) and (pattern[pattern_idx] == '?' or pattern[pattern_idx] == s[s_idx]):
        dp[pattern_idx][s_idx] = solution(pattern_idx + 1, s_idx + 1)
        return dp[pattern_idx][s_idx]
    if pattern[pattern_idx] == '*':
        if solution(pattern_idx + 1, s_idx) > 0 or (s_idx < len(s) and solution(pattern_idx, s_idx + 1) > 0):
            dp[pattern_idx][s_idx] = 1
            return dp[pattern_idx][s_idx]
    dp[pattern_idx][s_idx] = 0
    return dp[pattern_idx][s_idx]

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