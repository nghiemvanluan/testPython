res = []

lengths = int(input())

for i in range(lengths):
    n = int(input())
    res.append(n)


def evenNum(res):
    return [c for c in res if c%2 == 0]

print(evenNum(res))