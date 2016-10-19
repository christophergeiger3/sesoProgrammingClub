print("Give me a number and I'll add 5 to it")
number = input()
newnumber = int(number) + 5
print('Your new number is: ' + str(newnumber))
# As Max pointed out the str() cast is only necessary for string
# concatenation
