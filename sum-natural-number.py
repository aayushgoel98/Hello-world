#Python Program to Find the Sum of Natural Numbers

n=int(input("Please enter the number till which sum to be calculated "))
nd=n
if(n<0):
	print("Please enter a positive number")
else:
	sum = 0
	while(nd>0):
		sum=sum+nd
		nd=nd-1
	print("the sum is", sum)

