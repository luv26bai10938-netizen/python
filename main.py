import math
print("scientific calculator")
a = (input("enter operator (+,-,/,*,sin,cos,cosec ,power ,square root)"))
if a =="+" :
   b= float(input("enter first number= "))
   c= float (input("enter scrond number= "))
   print("Answe=",b+c)
elif a=="-":
   b=float(input("enter first number "))
   c=float(input("enter second number "))
   print("Answer=",b-c)
elif a=="/":
   b=float(input("enter first number= "))
   c=float(input("enter second number= "))
   print("Answer=",b/c)
elif a=="*":
   b=float(input("enter first number= "))
   c=float(input("enter second number= "))
   print("Answer=",b*c)
elif a=="sin(x)":
   b=float(input("enter first number= "))
   c=float(input("enter second number= "))
   print("Answer=",math.sin(math.radian(b)))
elif a=="cos(x)":
      b=float(input("enter first number= "))
      c=float(input("enter second number= "))
      print("Answer=",math.cos(math.radian(b)))
elif a=="cosec(x)":
    b=float(input("enter first number= "))
    c=float(input("enter second number= "))
    print("Answer=",math.cosec(math.radian(b)))
elif a=="power":
    b=float(input("enter first number= "))
    c=float(input("enter second number= "))
    print("Answer=",b**c)
elif a=="squareroot":
    b=float(input("enter the first number= "))
    c=float(input("enter the second number= "))
    print( "Answer=",math.sqrt(b) )
else:
    print("invalid choice . please try again.")
