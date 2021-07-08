import math
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
d=int(input("Enter a number"))
e=int(input("Enter a number"))
avg=math.ceil((a+b+c+d+e)/5)
print(222010308036,"is my pin number")
print(a)
print(b)
print(c)
print(d)
print(e)
print("Ceil Average of the given numbers is", avg)
if avg%2==0:
 print(avg, "(Ceil average) is even")
else:
 print(avg, "(Ceil average) is odd")