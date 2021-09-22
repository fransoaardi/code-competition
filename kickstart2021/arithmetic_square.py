import collections


class Solution:
    def solve(self, l_one, l_two, l_three):
        count = 0

        seven, eight, nine = l_one
        four, six = l_two
        one, two, three = l_three

        if four * 2 == seven + one:
            count += 1
        if eight * 2 == seven + nine:
            count += 1
        if six * 2 == nine + three:
            count += 1
        if two * 2 == one + three:
            count += 1

        x_cand = []
        x_cand.extend([(seven+three)/2, (one+nine) /
                      2, (four+six)/2, (two+eight)/2])

        x_filtered = [a for a in x_cand if a*2 == int(a)*2]

        if x_filtered:
            c = collections.Counter(x_filtered)
            count += max(c.values())

        return count


if __name__ == "__main__":
    s = Solution()
    t = int(input())

    for i in range(1, t+1):
        l_one = [int(s) for s in input().split(" ")]
        l_two = [int(s) for s in input().split(" ")]
        l_three = [int(s) for s in input().split(" ")]

        ans = s.solve(l_one, l_two, l_three)
        print("Case #{}: {}".format(i, ans))
