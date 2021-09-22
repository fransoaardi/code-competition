class ParentPartnering:
    def __init__(self, input):
        self.input = sorted(input, key=lambda x: x[0])
        self.workers = [[0, 'C'], [0, 'J']]
        self.output = [None for _ in range(len(input)) ]

    def process(self):
        for work in self.input:
            worker = self.workers[self.faster_end_idx()]
            if work[0] >= worker[0]:
                self.output[work[2]] = worker[1]
                worker[0] = work[1]
            else:
                return "IMPOSSIBLE"
        return "".join(self.output)

    def faster_end_idx(self):
        if self.workers[0][0] <= self.workers[1][0]:
            return 0
        else:
            return 1


if __name__ == "__main__":
    t = int(input())

    for i in range(1, t+1):
        schedule = []
        n = int(input())
        for j in range(n):
            st, ed = [int(s) for s in input().split(" ")]
            schedule.append([st, ed, j])
        pp = ParentPartnering(schedule)
        print("Case #{}: {}".format(i, pp.process()))

