

print('What speed is your car travelling at?')
carSpeed = input()

#Now I change carSpeed into an integer, so I can
#compare it with speedLimit (another integer):
carSpeed = int(carSpeed)

speedLimit = 60

if carSpeed < speedLimit:
    print('The car is going below the speed limit')
if carSpeed > speedLimit:
    print('The car is going over the speed limit')
if carSpeed == speedLimit:
    print('The car is going at exactly the speed limit!')
