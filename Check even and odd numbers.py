# Python Program to Check if a Number is Odd or Even
num= int(input("Enter the number:"))
if num>=0:
    if  num%2==0:
        print(f"The entered number {num} is an even number")
    else:    
        print(f"The entered number {num} is an odd number")
        

else :
    print("Enter a valid input")    