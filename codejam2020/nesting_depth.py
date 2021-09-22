class NestingDepth:
    def __init__(self, s):
        self.output = []
        self.s = s

    def process(self):
        depth = 0
        idx = 0
        length = len(s)

        while idx < length:
            num_s = int(s[idx])
            if num_s > depth:
                self.output.append((num_s - depth) * "(")
            else:
                self.output.append((depth - num_s) * ")")

            self.output.append(s[idx])
            depth = num_s
            idx += 1

        self.output.append(depth * ")")
        return "".join(self.output)


if __name__ == "__main__":
    t = int(input())

    for i in range(1, t+1):
        s = [str(s) for s in input()]
        nesting_depth = NestingDepth(s)
        answer = nesting_depth.process()
        print("Case #{}: {}".format(i, answer))
