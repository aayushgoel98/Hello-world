#Count Number of Digits in an Integer using while loop
n= int(input("Please enter the Number whose digits are to be computed "))
nc=n

count=0
while(nc>0):
	count=count+1
	nc=nc//10

print("the nunber of digits in integer number is ", count)
