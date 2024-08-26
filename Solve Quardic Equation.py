#Python Program to Solve Quadratic EquatiON

def quarddric_equation():
    import cmath
    # print(math.sqrt(9))

    # ax**2+bx+c=0   {quardric equation}
    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b:"))
    c=int(input("enter the value of c:"))
    if (a==0):
        print("the cofficient a can not be zero")
    else:
        d=b**2-(4*a*c)
        d1=cmath.sqrt(d)

        x1=(-b+d1 )/(a*2)
        x2=(-b-d1 )/(a*2)
        print("the value of the given quardric equations is",x1,"and",x2)
quarddric_equation()
       
