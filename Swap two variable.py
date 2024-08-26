# Python Program to Swap Two Variables
def swap():
    a= int(input("enter the value of a"))
    b= int(input("enter the value of b"))
    a,b = b,a
    print(a)
    print(b)

swap()