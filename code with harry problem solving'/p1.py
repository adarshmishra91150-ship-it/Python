#write a program to find the gratest of four number enterd by user 
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
d=int(input("d: "))
if (a>b and a>c and a>d):
    print("a is the gratest")
    if (b>a and b>c and b>d):
        print("b is the greatest")
        if (c>a and c>b and c>d):
            print("c is the greatest")
            if (d>a and d>b and d>c):
                print("d is the greatest")

