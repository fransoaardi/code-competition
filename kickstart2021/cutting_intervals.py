# https://codingcompetitions.withgoogle.com/kickstart/round/00000000004361e3/000000000082b933
class Solution:
    def solve(self, c, intervals):
        # 시작점+1 은 +1, 끝점은 -1 을 할당한 set 을 생성한다.
        # n 개의 interval 에 cut 을 하면 0~n 까지의 cut 이 추가될 수 있다.
        # A0~ An 까지의 list 를 만들고, j 가 큰 값부터, j * Aj 의 합을 더해가다가 답을 내면 된다.
        interv_dict = dict()
        for st, ed in intervals:
            if st+1 in interv_dict:
                interv_dict[st+1] += 1
            else:
                interv_dict[st+1] = 1

            if ed in interv_dict:
                interv_dict[ed] -= 1
            else:
                interv_dict[ed] = -1
        interv_dict_keys = sorted(interv_dict.keys())

        aggregated = dict()
        before = 0
        j = 0
        for v in interv_dict_keys:
            if j in aggregated:
                aggregated[j] += (v - before)
            else:
                aggregated[j] = (v - before)
            before = v
            j += interv_dict[v]

        ag_key = sorted(aggregated.keys(), reverse=True)

        # print(aggregated, ag_key)

        ans = 0
        for v in ag_key:
            ans += v * min(aggregated[v], max(c, 0))
            c -= aggregated[v]
        return ans


if __name__ == "__main__":
    """
    n: number of intervals
    c: number of cuts
    intervals = [(1, 3), (2, 4), (1, 4)]

    Sample Input:
    n = 3
    c = 3
    intervals = [(3, 7), (1, 5), (4, 7)]

    Expected Output:
    Case #1: 7
    """
    s = Solution()

    t = int(input())
    for i in range(1, t+1):
        n, c = [int(s) for s in input().split(" ")]
        intervals = []
        for _ in range(n):
            st, ed = [int(s) for s in input().split(" ")]
            intervals.append((st, ed))

        ans = s.solve(c, intervals)
        print(f"Case #{i}: {ans+n}")
