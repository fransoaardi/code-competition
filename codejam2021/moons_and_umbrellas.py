class Solution:
    def mau(self, s, x, y):
        l = len(s)
        d = [[0, 0] for _ in range(0, len(s))]
        # let C = 0, J = 1
        for idx in range(1, len(s)):
            if s[idx] == '?':
                d[idx][1] = min(d[idx-1][0] + x, d[idx-1][1])
                d[idx][0] = min(d[idx-1][0], d[idx-1][1] + y)
            elif s[idx] == 'C':
                d[idx][0] = min(d[idx-1][0], d[idx-1][1] + y)
                d[idx][1] = 999999
            elif s[idx] == 'J':
                d[idx][1] = min(d[idx-1][0] + x, d[idx-1][1])
                d[idx][0] = 999999
        # print(min(d[l-1][0], d[l-1][1]), d)
        return min(d[l-1][0], d[l-1][1])


if __name__ == "__main__":
    sol = Solution()
    # s.mau(' CJ?CC?', 2, 3)
    # s.mau(' CJCJ', 4, 2)
    # s.mau(' ??J???', 2, 5)
    # s.mau(' ??JJ??', 2, -5)

    t = int(input())
    for i in range(1, t + 1):
        stx, sty, s = [s for s in input().split(" ")]
        ans = sol.mau(' '+s, int(stx), int(sty))
        print("Case #{}: {}".format(i, ans))
