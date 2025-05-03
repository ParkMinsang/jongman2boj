import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def solution(lt1, rt1, lt2, rt2):
    if lt1 > rt1 or lt2 > rt2:
        return
    root_value = postorder[rt2]
    split_idx = inorder_idx[root_value]
    print(root_value, end = ' ')
    solution(lt1, split_idx - 1, lt2, lt2 + split_idx - 1 - lt1)
    solution(split_idx + 1, rt1, lt2 + split_idx - lt1, rt2 - 1)

if __name__ == "__main__":
    global inorder, postorder, inorder_idx
    n = int(input())
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))
    inorder_idx = {value: idx for idx, value in enumerate(inorder)}
    solution(0, len(inorder) - 1, 0, len(postorder) - 1)