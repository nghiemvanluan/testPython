n = int(input())

def sumOfAll(n):
    sum = 0
    for i in range (1, n + 1):
        if (n % i == 0) and i < n:
            sum += i 
    return sum 

print(sumOfAll(n))
