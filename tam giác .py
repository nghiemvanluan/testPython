a = int(input())
b = int(input())
c = int(input())

if a+b>c and a+c>b and b+c>a:
    if a == b and b == c:
        print("Equilateral triangle")
    elif a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b:
        print("Scalene triangle")
    elif a==b or a==c or b==c:
        print("Isosceles triangle")
else:
    print("Khong phai tam giac")