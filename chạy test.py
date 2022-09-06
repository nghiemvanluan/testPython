res = []

leng = int(input())

for i in range(leng):
    n = int(input())
    res.append(n)


def evenNum(res):
    return [c for c in res if c%2 == 0]

print(evenNum(res))