from itertools import permutations


class Solution:
    d = {}

    def _setup(self):
        for l in range(2, 7+1):
            item = [i for i in range(1, l+1)]
            for i in list(permutations(item, l)):
                if l not in self.d:
                    self.d[l] = {}

                self.d[l][self.reversort(list(i))] = i
        print(self.d)

    def eng(self, l, v):
        if v not in self.d[l]:
            return "IMPOSSIBLE"
        else:
            return " ".join(map(str, list(self.d[l][v])))

    def reversort(self, nums):
        ans = 0
        for idx in range(0, len(nums)-1):
            min_num = min(nums[idx:])
            min_idx = nums.index(min_num)

            if min_idx != idx:
                nums = sorted(nums[:min_idx+1]) + nums[min_idx+1:]
            # print(idx, min_idx, nums, nums[idx:], min_num, len(nums))
            # print(idx, min_idx, nums)
            ans += min_idx - idx + 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    sol._setup()
    # print(sol.eng(7, 18))

    # t = int(input())
    # for i in range(1, t + 1):
    #     l, v = [int(s) for s in input().split(" ")]
    #     ans = sol.eng(l, v)
    #     print("Case #{}: {}".format(i, ans))
