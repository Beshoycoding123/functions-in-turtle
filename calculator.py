def add(p,q):
    return p+q
def sub(p,q):
    return p-q
def mul(p,q):
    return p*q
def div(p,q):
    return p/q
print("please select the operation")
print("A.Adition")
print("B.Subtraction")
print("C.Multiplication")
print("D.Division")
choice=input("please enter one of the functions,(a,b,c,d): ")
num1=int(input("please enter the 1st number: "))
num2=int(input("please enter the 2nd number: "))
if choice=="a":
    print(num1+num2)
elif choice=="b":
    print(num1-num2)
elif choice=="c":
    print(num1*num2)
elif choice=="d":
    print(num1/num2)
else:
    print("invalid input")