# program that prints out a random number 
# between 1 and 10 

import random

x = int (input("Enter number here: "))
y = int (input("Enter number here: "))

number = random.randint (x,y)

print ("Here is a random number {}" .format (number))
