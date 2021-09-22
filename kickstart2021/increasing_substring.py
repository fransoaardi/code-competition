class Solution:
    def solve(self, inp):
        x = list(inp)
        ans = []
        last = ""
        count = 0
        for w in x:
            if w <= last:
                count = 1
            else:
                count += 1
            last = w
            ans.append(str(count))

        return " ".join(ans)


if __name__ == "__main__":
    s = Solution()
    # print(ans)

    t = int(input())
    for i in range(1, t + 1):
        _ = int(input())
        w = input()
        ans = s.solve(w)
        print(f'Case #{i}: {ans}')
