import sys
input = sys.stdin.readline

def init():
    for i in range(2, int(n**0.5) + 1):
        if arr[i]:
            for j in range(i * i, n + 1, i):
                arr[j] = False


if __name__ == '__main__':
    global arr, n
    m, n = map(int, input().split())
    arr = [True] * (n + 1)
    init()

