# 1)QUADRIC EQUATION
import cmath
a=int(input("Enter the number "))
b=int(input("Enter the number "))
c=int(input("Enter the third number"))
l=(b**2)-(4*a*c)
x1=(-b-cmath.sqrt(l))/(2*a)
y1=(-b+cmath.sqrt(l))/(2*a)
print('the value of x1={0} and y1={1}'.format(x1,y1))
print(x1)
print(y1)