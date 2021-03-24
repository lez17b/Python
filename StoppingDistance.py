# ***********************
# By: Luciano Zavala   *
# ***********************

# welcome message
print("Welcome to the stoping distance program")
print("----------------------------------------")

# variables and prompt the user
gravity = 9.80
speed = int(input("Please enter the speed (Km/h): "))
friction = float(input("Please enter the coefficient of fiction: "))

# Compute the speed from km.h to m/s
speedms = (speed*0.277778)

# Compute the distance
Distance = ((speedms*speedms)/((2*friction)*gravity))

# Display the results
print("Velocity = ", '%.2f' % speedms, "m/s")
print("Coefficient of friction = ", friction)
print("Stopping distance = ", '%.2f' % Distance, "m")






