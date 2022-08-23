s = str(input())

def format(s):
    n = len(s)
    a = list(s)
    if len(a) >= 3:
        x = a[n-3:n]
        if x[0] != "i":
            s += "ing"
        if x[0] == "i" and x[1] == "n" and x[2] == "g":
            s += "ly"
    print(s)

format(s)