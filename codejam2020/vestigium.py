# def has_repeat(list):
#     length = len(list)
#     for i in range(1, length//2+1):
#         # print(i)
#         idx = 0
#         while idx + 2*i <= length:
#             # print(list[idx:idx + i], list[idx + i:idx + 2 * i])
#             if list[idx:idx+i] == list[idx+i: idx+2*i]:
#                 return True
#             idx += 1
#     return False

def has_repeat(list):
    if len(set(list)) != len(list):
        return True
    return False


class Vestigium:
    def __init__(self, size, matrix):
        self.size = size
        self.matrix = matrix

    def trace(self):
        sum = 0
        for i in range(self.size):
            sum += self.matrix[i][i]
        return sum

    def row_repeated(self):
        count = 0
        for i in range(self.size):
            if has_repeat(self.matrix[i]):
                count += 1
        return count

    def col_repeated(self):
        count = 0
        for i in range(self.size):
            if has_repeat([row[i] for row in self.matrix]):
                count += 1
        return count


if __name__ == "__main__":
    t = int(input())

    for i in range(1, t + 1):
        n = int(input())
        x = []
        for j in range(n):
            x.append([int(s) for s in input().split(" ")])
        v = Vestigium(n, x)
        print("Case #{}: {} {} {}".format(i, v.trace(), v.row_repeated(), v.col_repeated()))


    # x = [
    #     [2,1,3],
    #     [1,3,2],
    #     [1,2,3],
    # ]
    # v = Vestigium(3, x)
    # print(v.col_repeated())
    # print(v.row_repeated())
    # print(v.trace())


