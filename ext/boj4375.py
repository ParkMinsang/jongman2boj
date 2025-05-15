import sys
input = sys.stdin.readline

def solution(n):
    count = 1
    num = 1
    while True:
        if num % n == 0:
            return count
        else:
            num = (num % n) * 10 + 1
            count += 1

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            print(solution(n))
        except:
            break