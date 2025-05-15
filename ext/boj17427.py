def solution(n):
    ret = 0
    for i in range(1, n + 1):
        ret += i * (n // i)
    return ret

n = int(input())
print(solution(n))