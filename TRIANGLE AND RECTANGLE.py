# MENU ITEM USING  AND CALCULATE TRIANGLE,RECTANGLE AND AREA OF SQUARE
print("\t\t\t\t\t\t\twelcome to my software")
print("\t\t\t\t\t\t\tPlease choose menu")
l=int(input("\t\t\t\tEnter the length"))
b=int(input("\t\t\t\tEnter the breadth"))
h=int(input("\t\t\t\tEnter the height"))
a=int(input("\t\t\t\tEnter the number"))
#menu.append(l,b,h,a)
menu=input("please choose 'a' for triangle , 'b' for rectangle 'c' for area of square")
if menu[0]=='a':
    total=(1/2*b*h)

elif menu[0]=='b':
    total=(h*l)

elif menu[0]=='c':
    total=a*a
print(total)

def simple_interest(p,t,r):

    total=(p*t*r)/100
    return (p * t * r) / 100
p=int(input("Enter the number"))
t=int(input("Enter the time"))
r=int(input("Enter the rate"))
print("The simple interest of this  rate is:",simple_interest(p,t,r))