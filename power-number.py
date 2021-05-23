#Calculate power of a number using a while loop
n= int(input("the number of which is to be computed "))
p= int(input("the enter what should be the power "))
pn=1
while p!=0:
	pn=pn*n
	p=p-1
print("the answer is ",pn)
