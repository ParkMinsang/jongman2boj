import sys
input = sys.stdin.readline

def count_max_candies_column(c):
    ret = 1
    cnt = 1
    for i in range(1, n):
        if candies[i][c] == candies[i - 1][c]:
            cnt += 1
            ret = max(ret, cnt)
        else:
            cnt = 1
    return ret

def count_max_candies_row(r):
    ret = 1
    cnt = 1
    for i in range(1, n):
        if candies[r][i] == candies[r][i - 1]:
            cnt += 1
            ret = max(ret, cnt)
        else:
            cnt = 1
    return ret

if __name__ == '__main__':
    global n, candies
    n = int(input())
    candies = [list(input().rstrip()) for _ in range(n)]

    ans = 1

    for i in range(n):
        ans = max(ans, count_max_candies_row(i), count_max_candies_column(i))

    for i in range(n):
        for j in range(n - 1):
            if i == 3 and j == 0:
                a = 10
            if candies[i][j] != candies[i][j + 1]:
                candies[i][j], candies[i][j + 1] = candies[i][j + 1], candies[i][j]
                ans = max(ans, count_max_candies_row(i), count_max_candies_column(j), count_max_candies_column(j + 1))
                candies[i][j], candies[i][j + 1] = candies[i][j + 1], candies[i][j]

            if candies[j][i] != candies[j + 1][i]:
                candies[j][i], candies[j + 1][i] = candies[j + 1][i], candies[j][i]
                ans = max(ans, count_max_candies_column(i), count_max_candies_row(j), count_max_candies_row(j + 1))
                candies[j][i], candies[j + 1][i] = candies[j + 1][i], candies[j][i]
    print(ans)