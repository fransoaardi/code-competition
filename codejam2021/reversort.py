class Solution:
    def reversort(self, nums):
        ans = 0
        for idx in range(0, len(nums)-1):
            min_num = min(nums[idx:len(nums)])
            min_idx = nums.index(min_num)
            # print('bf', nums)
            if min_idx != idx:
                tmp = sorted(nums[0:min_idx+1])
                if min_idx+1 < len(nums):
                    tmp += nums[min_idx+1:]
                nums = tmp
            # print(idx, min_idx, nums, nums[idx:], min_num, len(nums))
            # print(idx, min_idx, nums)
            ans += (min_idx - idx + 1)
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.reversort([4, 2, 1, 3]))
    print(sol.reversort([1, 8, 7, 2]))
    print(sol.reversort([7, 6, 5, 4, 3, 2, 1]))
    print(sol.reversort([7, 5, 4, 3, 2, 1, 6])) # 6 1 1 1 1 2
    print(sol.reversort([1, 2, 3]))
    print(sol.reversort([1, 3, 2]))
    print(sol.reversort([2, 1, 3]))
    print(sol.reversort([2, 3, 1]))
    print(sol.reversort([3, 1, 2]))
    print(sol.reversort([3, 2, 1]))
    print(sol.reversort([5, 6, 7, 1, 2, 3, 4]))
    print(sol.reversort([7, 1, 2, 3, 4, 5, 6]))
    print(sol.reversort([4, 3, 2, 1]))

    # t = int(input())
    # for i in range(1, t + 1):
    #     n = int(input())
    #     nums = [int(s) for s in input().split(" ")]
    #     ans = sol.reversort(nums)
    #     print("Case #{}: {}".format(i, ans))
