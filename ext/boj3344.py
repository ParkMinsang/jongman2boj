import sys
input = sys.stdin.readline

def solution(n):
    if n % 6 != 2 and n % 6 != 3:
        return solution_not_mod_2_or_3(n)
    return solution_else(n)

def solution_not_mod_2_or_3(n):
    ans_odd = []
    ans_even = []

    for i in range(1, n + 1):
        if i % 2 == 0:
            ans_even.append(i)
        else:
            ans_odd.append(i)
    return ans_even + ans_odd

def solution_else(n):
    ans_odd = []
    ans_even = []

    for i in range(1, n + 1):
        if i % 2 == 0:
            ans_even.append(i)
        else:
            ans_odd.append(i)

    if n % 6 == 2:
        ans_odd[0] = 3
        ans_odd[1] = 1
        ans_odd.pop(2)
        ans_odd.append(5)
    elif n % 6 == 3:
        ans_even.pop(0)
        ans_even.append(2)
        ans_odd = ans_odd[2:] + ans_odd[:2]
    return ans_even + ans_odd

if __name__ == '__main__':
    n = int(input())
    ans = solution(n)
    for i in ans:
        print(i)