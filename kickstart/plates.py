class Global:
    def __init__(self, number):
        self.sum_max = -1
        self.sum_list = [[] for _ in range(number)]


def backtrack(n, sum, ans, K, g):
    if n == 0 and sum == 0:
        ps = 0
        for idx, a in enumerate(ans):
            ps += g.sum_list[idx][a]

        if ps > g.sum_max:
            g.sum_max = ps

        return True

    if n == 0:
        return False

    if sum == 0:
        ps = 0
        for idx, a in enumerate(ans):
            ps += g.sum_list[idx][a]

        if ps > g.sum_max:
            g.sum_max = ps

        return True

    for digit in reversed(range(K+1)):
        if sum - digit >= 0:
            backtrack(n-1, sum-digit, ans+[digit], K, g)


def partial_sum(stacks):
    ps = [0]
    sum = 0

    for val in stacks:
        sum += val
        ps.append(sum)
    return ps


if __name__ == "__main__":
    t = int(input())

    for i in range(1, t+1):
        n, k, sum = [int(s) for s in input().split(" ")]

        g = Global(number=n)
        for idx in range(n):
            g.sum_list[idx] = partial_sum([int(s) for s in input().split(" ")])

        backtrack(n=n, sum=sum, ans=[], K=k, g=g)

        print("Case #{}: {}".format(i, g.sum_max))
