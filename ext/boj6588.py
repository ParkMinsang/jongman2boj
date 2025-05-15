import sys
input = sys.stdin.readline

def solution(n):
    for i in range(1, len(primes)):
        p = primes[i]
        if n - p in primes_set:
            return f"{n} = {p} + {n - p}"
    return "Goldbach's conjecture is wrong."

def eratosthenes():
    for i in range(2, int(max_n**0.5) + 1):
        if is_primes[i]:
            for j in range(i * i, max_n + 1, i):
                is_primes[j] = False
    for i in range(2, max_n):
        if is_primes[i]:
            primes.append(i)

if __name__ == '__main__':
    global is_primes, primes, primes_set, ans
    max_n = 100_0000
    is_primes = [True] * (max_n + 1)
    primes = []

    eratosthenes()
    primes_set = set(primes)

    while True:
        n = int(input())
        if n == 0:
            break
        print(solution(n))