import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution(s):
    global pointer
    c = s[pointer]
    pointer += 1
    if c == 'b' or c == 'w':
        return c
    upper_left = solution(s)
    upper_right = solution(s)
    lower_left = solution(s)
    lower_right = solution(s)
    return 'x' + lower_left + lower_right + upper_left + upper_right

if __name__ == "__main__":
    global pointer
    tc = int(input())

    for _ in range(tc):
        s = input().rstrip()
        pointer = 0
        print(solution(s))