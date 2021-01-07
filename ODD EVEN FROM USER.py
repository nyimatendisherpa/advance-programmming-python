#CHECKING ODD AND EVEN NUMBER FROM USER INPUT

customer1=int(input("Enter a number for checking odd or even number"))

 def nums(customer1):

   even=[]
    odd=[]

         if i %2==0:
            print("it is even number",i)
            even.append(i)
       else:
            print("it is odd number",i)
            odd.append(i)

    print(even)
     print(odd)
 nums(customer1)
# MULTIPLICATION AND ADDITION OF NUMBER BY USING X,AND Y
num=int(input("Enter the number for  multiplication   and addition"))
 menu=int(input("choose '1' for multiplication '2' for addition"))
 for i in range(1,11):
  if(menu==1):
      result=num*i
        print("%d x %d = %d"%(num,i,result))
        #print(menu, "*", i=result)
     elif(menu==2):
         result=num+i
        print(result)
         print("%d + %d=%d"%(num,i,result)