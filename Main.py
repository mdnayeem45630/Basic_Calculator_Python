def addition(a,b):
    c= a+b
    return c

def substraction(a,b):
    c=a-b
    return c

def multiplication(a,b):
    c=a*b
    return c

def division(a,b):
    if (b==0):
        print("Second number can not be zero because you can not devide any number by 0 ")
    else:
        c=a/b
        return c

def modulus(a,b):
    c=a%b
    return c

print("1.Addition\n 2.Substraction\n 3.Multiplication\n 4.Division\n 5.Modulus",)
d=input("Choose a number between 1/2/3/4/5 : ")
d=float(d)
if d in range(1,6):
    a=input("Enter the First number: ")
    a=float(a)
    b=input("Enter the Second number: ")
    b=float(b)
else:
    print("Choose an integer number between 1 to 5")
#global c
if d==1:
    add= addition(a,b)
    print("Addition: ",a ,"+", b, "=",add)
elif d==2:
    sub= substraction(a,b)
    print("Substraction: ",a ,"-", b, "=",sub)
elif d==3:
    mul= multiplication(a,b)
    print("multiplication: ",a ,"*", b, "=",mul)
elif d==4:
    dev= division(a,b)
    print("divition: ",a ,"/", b, "=",dev)
elif d==5:
    mod= modulus(a,b)
    print("modulus: ",a ,"%", b, "=",mod)
