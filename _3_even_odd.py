# write a program to count the no of even and odd numbers from a series of numbers
# numbers = (1,2,3,4,5,6,7,8,9)
# expected output - 
# number of even numbers - 4
# number of odd numbers - 5


size = int(input("Enter the size:"))

num = []
for i in range(size):
    val = int(input("Enter the number:"))
    num.append(val)

even = 0
odd = 0

for i in range(size):
    if (num[i] %2 == 0):
        even= even +1
    else:
        odd = odd+1
    print("Total even=",even,"Total odd=",odd)   