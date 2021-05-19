# Python Program for compound interest

principle = int(input("Please enter the amount for interst to be calculated anually "))
time = int(input("please enter the time in years "))
rate = int(input("please enter the rate of interest "))

ci = ((principle*(pow((1+(rate/100)),time))) - principle)

print("the interest of the given amount is ",ci)
