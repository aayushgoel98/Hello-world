#Python Program to Find LCM
n1 = int(input("Please enter the number 1 "))
n2 = int(input("Please enter the number 2 "))
g=0
lcm=0
if(n1>n2):
	g=n1
else:
	g=n2
while(True):
       if((g % n1 == 0) and (g % n2 == 0)):
           lcm = g
           break
       g =g+ 1

print(g)