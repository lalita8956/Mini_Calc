n1=int(input("Enter first number = "))
n2=int(input("Enter second number = "))
print("select operation\n"
"1 Addition\n"
"2 subtraction\n"
"3 division\n"
"4 multiplication\n")
c=int(input("select operation = "))

def add(n1,n2):
    return(n1+n2)

def sub(n1,n2):
    return(n1-n2)

def div(n1,n2):
    return(n1/n2)

def mul(n1,n2):
    return(n1*n2)

if(c==1):
    print(n1+n2)
    add(n1,n2)
elif (c==2):
    print(n1-n2)
    sub(n1,n2)
elif (c==3):
    print(n1/n2)
    div(n1,n2)
elif (c==4):
    print(n1*n2)
    mul(n1,n2)

