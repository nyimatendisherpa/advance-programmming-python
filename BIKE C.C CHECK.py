#  NEPAL TAX CALCULATION(USING FUNCTION AND LOOP)

print("\t\t**************DEPARTMENT OF TRANSPORT MANAGEMENT****************")
print("\t\t\t**************BANESWOR,KATHMANDU***************")
print("\t\t**************WELCOME TO  DOTM BIKE RENEWAL SYSTEM*************8")
print("\t\t\t\t*************************FISCAL YEAR=2020/21***********")
i=0
count=int(input("how many of queries you hava"))
while(i<count):
    name=input(" Customer Name:")
    address=input("Address:")
    bike=int(input("Customer bike[cc:]"))
    num=int(input("Phone number:"))
    i=i+1

def calculation(bike):
    total=[]
    if bike<125:
        total=2800
    elif bike>=125and bike<=160:
        total=4500

    elif bike>=161and bike<=250:
        total=5500

    elif bike<=250 and bike>=400:
        total=9000

    elif bike<=401and bike>=650:
        total=20000

    else:
        total=30000
        print(total)
        return total

print("\t\t\t\tDOTM")
print("\t\t\t\t\t\t\tWEL-COME")
print("BIKE HOLDER NAME:{},\t\tADDRESS{}".format(name,address))
print("BIKE CC:{},\t\t\tPHONE NUMBER:{}".format(bike,num))
print("the tax for given {}".format(bike),"is:",calculation(bike))