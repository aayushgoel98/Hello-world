#Python Program to Find Factorial of Number Using Recursion

def factorial(x):
	if(x==1):
		return 1
	else:
		return (x*factorial(x-1))


n= int(input("please enter the number for factorial "))
f=factorial(n)
print("the factorial of ",n ,"is ",f )
