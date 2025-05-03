import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def solution(lt, rt, arr):
    if lt >= rt:
        return 0
    if lt + 1 == rt:
        if arr[lt] > arr[rt]:
            arr[lt], arr[rt] = arr[rt], arr[lt]
            return 1
        return 0
    mt = (lt + rt) // 2
    ret = 0
    ret += solution(lt, mt - 1, arr)
    ret += solution(mt, rt, arr)
    lo = lt
    hi = mt
    cnt = 0
    while lo < mt and hi <= rt:
        if arr[lo] <= arr[hi]:
            temp[cnt] = arr[lo]
            cnt += 1
            lo += 1
        else:
            temp[cnt] = arr[hi]
            cnt += 1
            ret += mt - lo
            hi += 1
    while lo < mt:
        temp[cnt] = arr[lo]
        cnt += 1
        lo += 1
    while hi <= rt:
        temp[cnt] = arr[hi]
        cnt += 1
        hi += 1

    for i in range(cnt):
        arr[lt + i] = temp[i]
    return ret


if __name__ == "__main__":
    global temp
    n = int(input())
    temp = [0] * n
    arr = list(map(int, input().split()))
    ans = solution(0, n - 1, arr)
    print(ans)