def process(budget, costs):
    count = 0
    costs.sort()

    for cost in costs:
        if budget - cost >= 0:
            count += 1
            budget -= cost
        else:
            break

    return count


if __name__ == "__main__":
    t = int(input())

    for i in range(1, t+1):
        n, b = [int(s) for s in input().split(" ")]
        costs = [int(s) for s in input().split(" ")]

        answer = process(budget=b, costs=costs)
        print("Case #{}: {}".format(i, answer))

