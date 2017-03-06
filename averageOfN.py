print('How many numbers would you like to average?')
# take in the amount of numbers to be averaged
n = int(input())


# create a variable to store the sum of all numbers
mySum = 0

# create a counter
numbersProcessed = 0


print('Enter those numbers: ')
#loop runs 'n' times
while(numbersProcessed < n):
    mySum = mySum + float(input())
    numbersProcessed = numbersProcessed + 1

average = mySum/n
print(float(average))
