# 2) SWAPPING
a=10
b=20
c=a
a=b
b=c
print('the  value  of a after swap is:{}'.format(a))
print('the value of b after swap is:{}'.format(b))
num1=int(input("enter the number"))
num2=int(input("enter the number2"))
print('before swap')
print(num1,num2)
a=c
a=b
b=a
print('after swap')
print(num1,num2)
# SWAPPING IN ANOTHER FORM
numa=int(input('enter the number'))
numb=int(input("enter the number "))
print(numa,numb)
a=a+b
b=a-b
a=a-b
print("variables after swap is :")
print(a,b)
#Enter your name and age and add 100 on your age.
name=input("Enter the name of yours")
age=int(input("enter the age what you are"))
year=int(input(2014-age))+100
print(name+"will be 100 years"+age)