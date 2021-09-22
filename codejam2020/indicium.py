# def equal_generate(n, st):
#     row = [st]
#     row.extend([i for i in range(1, n + 1) if i != st])
#
#     for i in range(n):
#         x = row[n - i: n] + row[0: n - i]
#         print(" ".join(map(str, x)))
#
#
# def diff_generate(n):
#     row = [i for i in range(1, n + 1)]
#
#     for i in range(n):
#         x = row[i: n] + row[0: i]
#         print(" ".join(map(str, x)))
#
#
# def sum_to(n):
#     return sum([i for i in range(1, n+1)])
#
#
# def is_possible(n, k):
#     if k <= 0 or k > n*n:
#         return 3, "IMPOSSIBLE"
#
#     if n % 2 == 0:  #짝수
#         if k % n == 0:  # 같은숫자 조합
#         elif : # nC2 2 times
#             a = 1
#         else:
#             return 3, "IMPOSSIBLE"
#
#     else:   #홀수
#         if k == sum_to(n):
#             return 2, "POSSIBLE"
#         else:
#             return 3, "IMPOSSIBLE"


def backtrack(n, m, s, trace):
    if m == 0 and s == 0:
        return trace
    if n == 0:
        return None

    if not backtrack(n-1, m-1, s-n, trace+[n]):
        return
    backtrack(n-1, m, s, trace)




if __name__ == "__main__":
    backtrack(4, 3, 6, [])

    # t = int(input())
    # for i in range(1, t + 1):
    #     n, k = [int(s) for s in input().split(" ")]
    #     possible, val = is_possible(n, k)
    #     print("Case #{}: {}".format(i, val))
    #     if possible == 1:
    #         equal_generate(n, int(k/n))
    #     elif possible == 2:
    #         diff_generate(n)




