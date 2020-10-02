print("WELCOME TO VICTOR's CALCULATOR")
print("ENTER YOUR FIRST NUMBER")
var1 = int(input())
print("WHAT DO YOU WANT TO DO")
print("+" ,"-" ,"/" , "*")
var3 = input()
print("ENTER YOUR SECOND NUMBER")
var2 = int(input())

if var3=="+":
    if var1==56 and var2==9:
        print("Your ans is 77")
    else:
        print("Your ans is" , var1 + var2)
        
        
elif var3=="*":
    if var1==45 and var2==3:
        print("Your ans is 555")
    else:
        print("Your ans is" , var1 * var2)


elif var3=="/":
    if var1==56 and var2==6:
        print("Your ans is 4")
    else:
        print("Your ans is" , var1 / var2)


else:
    print("Your ans is" , var1-var2)
